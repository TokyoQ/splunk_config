import configparser
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


def parse_file(filepath):
    config = configparser.ConfigParser()
    config.read(filepath)

    sections = config.sections()

    for section in sections:
        for key in config[section]:
            value = config[section][key]
            print('{}| {}:{}'.format(section, key, value))


def validate_inputs_conf():
    return 0


server_conf_file = 'C:\Program Files\Splunk\etc\system\local\server.conf'
parse_file(server_conf_file)
