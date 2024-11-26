import json
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from django.http import HttpResponse


# Function to generate the response
def send_funct():
    to_send = {  
        "body": "Hello this is a test"
    }
    return json.dumps(to_send)

# Define request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Send the response body (the JSON data)
        self.wfile.write(send_funct().encode('utf-8'))

# Graceful shutdown handler
def signal_handler(sig, frame):
    print("\nShutting down server gracefully...")
    sys.exit(0)

# Set up and start the server
if __name__ == "__main__":
    # Register signal handler for graceful shutdown (e.g., Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    # Set the server address (localhost) and port (8080)
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)

    print("Server started on port 8080")
    try:
        # Start the server and listen for requests
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Server shutdown is handled in signal_handler
        pass
