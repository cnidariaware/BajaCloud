from GetSchedulePackager import getSchedulePackager
from postSelectAppointment import SelectAppointment
import json
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define request handler
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Handle GET requests and route based on path"""
        if self.path == '/appointments':
            self._send_response(doNothing())
        elif self.path == '/interview_data':
            self.wfile.write(doNothing())
        else:
            self._send_error()

    def do_POST(self):
        """Handle POST requests to '/appointments' or '/interview_data'"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Try to parse JSON data from the request body
        try:
            json_data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self._send_response(400, "Invalid Request")
            return

        if self.path == '/appointments':
            self._send_response(SelectAppointment(json_data))
        elif self.path == '/nothing':
            self._send_response(doNothing())
        else:
            self._send_error(404)

    # def do_DELETE(self):
    #     """Handle DELETE requests to '/appointments' or '/interview_data'"""
    #     content_length = int(self.headers['Content-Length'])
    #     delete_data = self.rfile.read(content_length)

    #     # Try to parse JSON data from the DELETE request body
    #     try:
    #         json_data = json.loads(delete_data.decode('utf-8'))
    #     except json.JSONDecodeError:
    #         self.send_error(400, "Invalid JSON")
    #         return

    #     if self.path == '/appointments':
    #         self.handle_appointments_delete(json_data)
    #     elif self.path == '/interview_data':
    #         self.handle_interview_data_delete(json_data)
    #     else:
    #         self.send_error(404, "Not Found")

    def _send_response(self, response):
        """Send the response body, status code, and headers directly"""
        status_code = response['statusCode']
        headers = response['headers']
        body = json.dumps(response['body']).encode('utf-8')  # Encoding happens here

        # Set the response status code
        self.send_response(status_code)

        # Set the response headers
        for header, value in headers.items():
            self.send_header(header, value)

        # End the headers
        self.end_headers()

        # Send the response body
        self.wfile.write(body)
    
    def _send_error(self):
        {"statusCode": 404,
        "isBase64ENcoded": "false",
        "headers": {
            "Content-Type": "application/json",  # Specify content type
            "X-IsBase64Encoded": "false"  # Indicating that the body is not base64 encoded
        },
        "body": "Invalid Response"}
        self._send_response


def doNothing():
    
    return json.dumps({"statusCode": 200,
        "isBase64ENcoded": "false",
        "headers": {
            "Content-Type": "application/json",  # Specify content type
            "X-IsBase64Encoded": "false"  # Indicating that the body is not base64 encoded
        },
        "body": ""})

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
    print(getSchedulePackager())
    print(SelectAppointment("10:00 am"))
