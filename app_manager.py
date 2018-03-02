import configparser
import os
import shutil

SPLUNK_HOME = 'C:\\Program Files\\Splunk'
appFolder = '{}\\etc\\apps'.format(SPLUNK_HOME)


def get_apps():
    apps = os.listdir(appFolder)
    return apps


def get_app_label(app_name):
    app_config_file = '{}\\{}\\default\\app.conf'.format(appFolder, app_name)
    if not os.path.isfile(app_config_file):
        print("ERROR - app.conf doesn't exist.")
        return

    app_config = configparser.ConfigParser()
    app_config.read(app_config_file)

    try:
        label = app_config['ui']['label']
    except KeyError:
        print('ERROR - label not set in app.conf')
        return

    return label


def update_app_label(app_name, label):
    app_config_file = '{}\\{}\\default\\app.conf'.format(appFolder, app_name)
    if not os.path.isfile(app_config_file):
        print("ERROR - app.conf doesn't exist.")
        return

    app_config = configparser.ConfigParser()
    app_config.read(app_config_file)

    try:
        old_label = app_config['ui']['label']
        app_config['ui']['label'] = label

        with open(app_config_file, 'w') as configfile:
            app_config.write(configfile)
            print('Updated the label for {} from "{}" to "{}"'.format(app_name, old_label, label))

    except KeyError:
        print('ERROR - label not set in app.conf')
        return


def add_app_folder(app_name):
    apps = os.listdir(appFolder)

    if 'test_app' not in apps:
        print("ERROR - test_app doesn't exist.")
        return

    if app_name in apps:
        print("ERROR - App already exists.")
        return

    shutil.copytree('{}\\test_app'.format(appFolder), '{}\\{}'.format(appFolder, app_name))
    print('App {} created.'.format(app_name))


def create_app(app_name, app_label):
    add_app_folder(app_name)
    update_app_label(app_name, app_label)


### MAIN
create_app('app1', 'APP1')
#print(get_app_label('blastoff'))
#update_app_label('blastoff', 'Blastoff forever!')