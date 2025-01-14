import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    products = []

    def _set_response(self, code=200, content_type='application/json'):
        self.send_response(code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/products':
            self._set_response()
            self.wfile.write(json.dumps(self.products).encode('utf-8'))
        elif self.path.startswith('/products/'):
            product_id = int(self.path.split('/')[-1])
            product = next((p for p in self.products if p['id'] == product_id), None)
            if product:
                self._set_response()
                self.wfile.write(json.dumps(product).encode('utf-8'))
            else:
                self._set_response(404)
                self.wfile.write(json.dumps({'message': 'Товар не найден'}).encode('utf-8'))

    def do_POST(self):
        if self.path == '/products':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_product = json.loads(post_data)

            # Добавление нового товара в список
            self.products.append(new_product)

            self._set_response(201)
            self.wfile.write(json.dumps(new_product).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    with open('products.json', 'r', encoding='utf-8') as f:
        handler_class.products = json.load(f)

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
