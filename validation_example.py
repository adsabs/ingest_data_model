import json
import os
from glob import glob
from jsonschema import Draft7Validator, RefResolver


schema_path = os.path.abspath('./json_schema')

class LoadResolverException(Exception):
    pass


class LoadSchemaException(Exception):
    pass


class ValidationTool(object):

    def __init__(self):
        try:
            foo = 'file://%s/' % schema_path
            self.resolver = RefResolver(foo, None)
        except Exception as err:
            raise LoadResolverException('problem loading resolver: %s' % err)
        else:
            try:
                schema_loc = os.path.join(schema_path,'Document.json')
                with open(schema_loc,'r') as fs:
                    self.schema = json.load(fs)
            except Exception as err:
                raise LoadSchemaException('problem loading schema: %s' % err)
            else:
                self.validator = Draft7Validator(schema=self.schema, resolver=self.resolver)

    def test(self, data):
        try:
            self.validator.validate(data)
        except Exception as err:
            return ('Validation failed:\n\tError: %s' % (err))
        else:
            return ('Validation passed')


def main():

    test_dir = os.path.abspath('./test_data')
    test_files = glob(test_dir+'/*.json')
    test_failures = glob(test_dir+'/failure_examples/*.json')
    try:
        validator = ValidationTool()
    except Exception as err:
        print('Cannot validate, problem loading schema: %s' % err)
    else:
        print("Tests that should all pass:")
        for f in test_files:
            print('Testing PASSING file %s' % f)
            with open(f, 'r') as fj:
                print("%s\n" % validator.test(json.load(fj)))

        print("\n\nTests that should all fail:")
        for f in test_failures:
            print('Testing FAILING file %s' % f)
            with open(f, 'r') as fj:
                print("%s\n" % validator.test(json.load(fj)))

if __name__ == '__main__':
    main()
