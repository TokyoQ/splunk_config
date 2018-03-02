import configparser
import os
import shutil

SPLUNK_HOME = 'C:\\Program Files\\Splunk'
indexesFile = '{}\\etc\\system\\local\\indexes.conf'.format(SPLUNK_HOME)


def get_indexes():
    index_config = configparser.ConfigParser()
    index_config.read(indexesFile)

    if not os.path.isfile(indexesFile):
        print("No indexes.conf - no custom indexes.")
        return None

    indexes = index_config.sections()
    print(indexes)

    return indexes


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

    with open(indexesFile, 'w') as configfile:
        index_config.write(configfile)
    print('Created index {}.'.format(index_name))



### MAIN
#get_indexes()
#add_index('destiny')
