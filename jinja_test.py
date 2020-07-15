from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Template


example = [
    {
       "date": "31.12.2020",
       "user": "Егор",
       "text": "Задача1",
       "status": True
    },
    {
       "date": "31.12.2020",
       "user": "Егор",
       "text": "Задача2",
       "status": False
    },
    {
       "date": "31.12.2020",
       "user": "Егор",
       "text": "комментарий"
    }
]


class S(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # template = Template('Hello {{ name }}!')
        # html = template.render({"name": "egor"})

        with open('example.html') as file_:
            template = Template(file_.read())
            html = template.render({"name": "egor"})

        self.wfile.write(html.encode('utf-8'))


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, S)
    print('Starting httpd... http://localhost:8000/\n')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()