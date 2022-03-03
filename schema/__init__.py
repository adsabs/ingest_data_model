import json
import os

def ads_schema():
    top_schema_file = os.path.join(os.path.dirname(__file__), 'Document.json')
    with open(top_schema_file, 'r') as f:
        schema = json.load(f)

    return schema