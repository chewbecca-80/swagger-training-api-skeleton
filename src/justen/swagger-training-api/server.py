import importlib.resources

import connexion
import ruamel.yaml

from servaites.python_demo_api import echo


YAML = ruamel.yaml.YAML(typ='safe')
with importlib.resources.path('servaites.python_demo_api', 'api.yaml') as f:
    openapi_dict = YAML.load(f)

def get_health():
    return {'message': 'Everything is A-OK'}

def get_echo(message: str):
    new_message = echo.make_echo(message)
    data = {'echo': new_message}
    return data

def main(port: int = 9090):
    app = connexion.FlaskApp(__name__, port=9090)
    app.add_api(openapi_dict, arguments={'title': 'Echo Chamber'})
    app.run()

if __name__ == '__main__':
    main()

