from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_GET, require_POST


def index(request):
    return HttpResponse('HHHHHHHHHHHHHHHHhh')


@require_GET
def pull(request):
    name = request.GET['name']
    return HttpResponse(name)
