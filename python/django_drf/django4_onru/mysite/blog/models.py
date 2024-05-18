from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
                        .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """
    | MODEL                      | TABLE DB                         |
    | Post                       | blog_post                        |
    | ---------------------------|----------------------------------|
    | id        BigAutoField     | id    integer        Primary Key |
    | title     CharField        | title varchar(250)               |
    | slug      SlugField        | slug  varchar(250)               |
    | author    ForeignKey       | author  integer      ForeignKey  |
    | body      TextKey          | body  text                       |
    | publish   DateTimeField    | publish  datetime                |
    | created   DateTimeField    | created  datetime                |
    | updated   DateTimeField    | updated  datetime                |
    | status    CharField        | status  varcahr(10)              |

    """

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)  # VARCHAR
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # VARCHAR
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_post'
    )
    body = models.TextField()  # Text
    publish = models.DateTimeField(default=timezone.now)  # DATETIME
    created = models.DateTimeField(auto_now_add=True)  # DATETIME (auto_now_add: save on creation)
    updated = models.DateTimeField(auto_now=True)  # DATETIME (auto_now: save on update)
    status = models.CharField(max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    objects = models.Manager()  # the default manager.
    published = PublishedManager()  # our custom manager.
    tags = TaggableManager()


    # Sorting
    class Meta:
        # ordering = ['publish']  # sort ASCending (no prefix) by `publish` field
        ordering = ['-publish']  # sort DESCending (- prefix) by `publish` field

        # DB indexing
        indexes = [
            models.Index(fields=['-publish'])  # DESCending
            # DESCending indexes not supported by MySQL, if you will use - for
            # DESC in MySQL, it'll create noraml indexing. (i.e. ASC)
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
