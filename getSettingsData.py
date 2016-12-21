import json
import os


def get_label_dict():
    return json.loads(open(os.getcwd() + '/resources/settings/labelDict.json', 'r').read())
