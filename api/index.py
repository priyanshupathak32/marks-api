from http.server import BaseHTTPRequestHandler
import json
import os
from urllib.parse import parse_qs, urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get absolute file path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(current_dir, 'q-vercel-python.json')
            
            # Verify file exists
            if not os.path.exists(json_path):
                raise FileNotFoundError(f"JSON file not found at {json_path}")
            
            # Load data
            with open(json_path) as f:
                marks_data = json.load(f)
            
            # Process request
            query = parse_qs(urlparse(self.path).query
            names = query.get('name', [])
            results = [next((s['mark'] for s in marks_data 
                          if s['name'].lower() == name.lower()), None)
                     for name in names]
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"marks": results}).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({
                "error": str(e),
                "path": os.path.abspath(__file__),
                "cwd": os.getcwd()
            }).encode())
