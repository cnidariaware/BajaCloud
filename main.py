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
        if self.path == '/getAppointments':
            self._send_response(getSchedulePackager())
        elif self.path == '/interview_data':
            self._send_response(doNothing())  # If you want to return an empty response
        else:
            self._send_error(404, "Not Found")

    def do_POST(self):
        """Handle POST requests to '/selectAppointment' or '/'"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Try to parse JSON data from the request body
        try:
            json_data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self._send_error(400, "Invalid Request")
            return

        if self.path == '/selectAppointment':
            self._send_response(SelectAppointment(json_data))  # Use SelectAppointment directly
        elif self.path == '/':
            self._send_response(doNothing())  # Empty response for the root route
        else:
            self._send_error(404, "Not Found")

    def _send_response(self, res):
        """Send the response body with the given status code"""
        if isinstance(res, dict):
            # Ensure res has all the required keys
            body = res.get("body", "")  # Default to empty string if no body is provided
            baseEncoded = res.get("isBase64ENcoded", "false")  # Default to "false" if not provided
            status_code = res.get("statusCode", 200)  # Default to 200 if no statusCode is provided

            # Convert body to string if it's not already
            if isinstance(body, dict):
                body = json.dumps(body)

            # If body is base64 encoded, we would handle that differently, but currently we treat all as 'false'
        
        response = {
            "statusCode": status_code,
            "isBase64Encoded": baseEncoded,
            "headers": {
                "Content-Type": "application/json",  # Specify content type
                "X-IsBase64Encoded": baseEncoded  # Indicating if the body is base64 encoded
            },
            "body": body
        }

        # Send the status code and headers
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        # Write the JSON response body, ensuring it's encoded to utf-8
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def _send_error(self, status_code=404, message="Not Found"):
        """Send error response with the same structure as normal responses"""
        res = {
            "statusCode": status_code,
            "body": json.dumps({"message": message})
        }
        # Return the error response in the same format
        self._send_response(res)

def doNothing():
        """Return an empty JSON response"""
        return {
            "statusCode": 200,
            "isBase64ENcoded": "false",
            "body": json.dumps({"message": ""})
        }


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
        pass
