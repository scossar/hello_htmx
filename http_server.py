import http.server
import socketserver
import sys

Handler = http.server.SimpleHTTPRequestHandler

PORT = 8888


def run(port: int):
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Serving at port", port)
        httpd.serve_forever()


if __name__ == "__main__":
    port = int(sys.argv[1]) if sys.argv[1] else PORT
    run(port)
