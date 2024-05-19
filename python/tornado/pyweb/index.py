import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, World')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', BasicRequestHandler)
    ])

    port = 8008
    app.listen(port)

    print(f'Listining on {port = }')

    tornado.ioloop.IOLoop.current().start()
