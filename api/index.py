import json
import os

def handler(request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json"
    }

    try:
        with open(os.path.join(os.path.dirname(__file__), "marks.json")) as f:
            data = json.load(f)

        query = request.get("query", {})
        names = query.get("name", [])

        if isinstance(names, str):
            names = [names]

        marks = [data.get(name, 0) for name in names]

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"marks": marks})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": str(e)})
        }
