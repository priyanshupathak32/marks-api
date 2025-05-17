import os
import json

def get_file_path(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

# Usage:
json_path = get_file_path('q-vercel-python.json')
with open(json_path) as f:
    data = json.load(f)
