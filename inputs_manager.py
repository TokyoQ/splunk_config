import configparser
import os


def get_inputs():

    inputConfig.read(inputsFile)

    if not os.path.isfile(inputsFile):
        print("No inputs.conf - no custom indexes.")
        return None

    inputs = inputConfig.sections()
    print(inputs)

    return inputs


def get_index_details(index_name):
    index_config = configparser.ConfigParser()
    index_config.read(indexesFile)

    if not os.path.isfile(indexesFile):
        print("ERROR - No indexes.conf.")
        return None

    try:
        index_config[index_name]
    except KeyError:
        print("ERROR - Index doesn't exist.")
        return


def add_index(index_name):
    if not os.path.isfile(indexesFile):
        print("No indexes.conf - creating it.")
        file = open(indexesFile, "w+")
        file.close()

    index_config = configparser.ConfigParser()
    index_config.read(indexesFile)

    indexes = index_config.sections()
    if index_name in indexes:
        print("ERROR - Index already exists.")
        return

    index_config[index_name] = {
        'homePath': '$SPLUNK_DB\\{}\\db'.format(index_name),
        'coldPath': '$SPLUNK_DB\\{}\\colddb'.format(index_name),
        'thawedPath': '$SPLUNK_DB\\{}\\thaweddb'.format(index_name)
    }

    with open(inputsFile, 'w') as configfile:
        index_config.write(configfile)
    print('Created index {}.'.format(index_name))



### MAIN
SPLUNK_HOME = 'C:\\Program Files\\Splunk'
inputsFile = '{}\\etc\\system\\local\\inputs.conf'.format(SPLUNK_HOME)
inputConfig = configparser.ConfigParser()
inputConfig.optionxform = lambda option: option

get_inputs()
#add_index('destiny')
