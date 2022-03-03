import json

def ads_schema():
    top_schema_file = 'Document.json'
    with open(top_schema_file, 'r') as f:
        schema = json.load(f)

    return schema