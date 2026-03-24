import json
import os
from jsonschema import Draft7Validator, RefResolver

def ads_schema_validator():
    schema_dir = os.path.dirname(__file__)
    top_schema_file = os.path.join(schema_dir, 'Document.json')
    with open(top_schema_file, 'r') as f:
        schema = json.load(f)

    resolver = RefResolver('file://' + schema_dir + '/', schema)

    validator = Draft7Validator(schema=schema, resolver=resolver)

    return validator
