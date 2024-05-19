import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, World')


class ListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class QueryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument('num')
        if (num.isdigit()):
            result = 'odd' if int(num) & 1 else 'even'
            self.write(f'The integer {num} is {result}')
        else:
            self.write(f'{num} is not a valid integer')


class ResourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, student_name, course_id):
        self.write(f'Welcome {student_name} the course you are viewing is {course_id}')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', BasicRequestHandler),
        (r'/animal', ListRequestHandler),
        (r'/isEven', QueryParamRequestHandler),
        (r'/students/([A-Za-z]+)/([0-9]+)', ResourceParamRequestHandler),
    ])

    port = 8008
    app.listen(port)

    print(f'Listining on {port = }')

    tornado.ioloop.IOLoop.current().start()
