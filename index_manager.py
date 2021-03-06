import configparser
import os


def get_indexes():
    indexConfig.read(indexesFile)

    if not os.path.isfile(indexesFile):
        print("No indexes.conf - no custom indexes.")
        return None

    indexes = indexConfig.sections()
    print(indexes)

    return indexes


def get_index_details(index_name):
    indexConfig.read(indexesFile)

    if not os.path.isfile(indexesFile):
        print("ERROR - No indexes.conf.")
        return None

    try:
        indexConfig[index_name]
    except KeyError:
        print("ERROR - Index doesn't exist.")
        return



def add_index(index_name):
    if not os.path.isfile(indexesFile):
        print("No indexes.conf - creating it.")
        file = open(indexesFile, "w+")
        file.close()

    indexConfig.read(indexesFile)

    indexes = indexConfig.sections()
    if index_name in indexes:
        print("ERROR - Index already exists.")
        return

    indexConfig[index_name] = {
        'homePath': '$SPLUNK_DB\\{}\\db'.format(index_name),
        'coldPath': '$SPLUNK_DB\\{}\\colddb'.format(index_name),
        'thawedPath': '$SPLUNK_DB\\{}\\thaweddb'.format(index_name)
    }

    with open(indexesFile, 'w') as configfile:
        indexConfig.write(configfile)
    print('Created index {}.'.format(index_name))



### MAIN
SPLUNK_HOME = 'C:\\Program Files\\Splunk'
indexesFile = '{}\\etc\\system\\local\\indexes.conf'.format(SPLUNK_HOME)
indexConfig = configparser.ConfigParser()
indexConfig.optionxform = lambda option: option

#get_indexes()
add_index('destiny6')
