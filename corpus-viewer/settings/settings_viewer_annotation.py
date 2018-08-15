def load_data(item_handle):
    #put import statements inside this Function
    #import json or Csv
    import csv
    import random

    with open('../corpora/csv-alles.csv', newline='') as csvfile:
    #with open('../corpora/testbatch1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            obj={}
            obj['Input.hit'] = row[1]
            obj['item'] = row[2]
            obj['prediction'] = row[3]
            #obj['anno'] = row[4]
            item_handle.add(obj)

#    for x in range(0,100):
#        obj={}
#        obj['id'] = x
#        obj['Input.hit'] = x
#        obj['item'] = str(x)
#        obj['prediction'] = 'no or yes' + str(x)
        #register item to viewer
#        item_handle.add(obj)

#this is the main dictionary containing the necessary information to load and display your corpus
DICT_SETTINGS_VIEWER = {
    'name': 'Annotation',
    'description': 'This Corpus contains Webpages and their Annotation',
    'data_type': 'csv-file',
    'load_data_function': load_data,
    'data_path': '../corpora/csv-alles.csv',
    #'data_path': '../corpora/testbatch1.csv',
    #'data_path':'../../../web-archive-page-annotation/data/error-annotation/batch1-mace-prediction-before-review.csv', #path to json or csv
    'data_structure': ['Input.hit','item','prediction'],

    'data_fields': {
        #'id': {
        #    'type': 'number',
        #    'display_name': 'ID'
        #},
        'Input.hit': {
            'type': 'number',
            'display_name': 'HitID'
        },
        'item': {
            'type': 'string',
            'display_name': 'TaskID'
        },
        'prediction': {
            'type': 'string',
            'display_name': 'Mace'
        }
    },
    'id': 'Input.hit',
    'displayed_fields': [
        'Input.hit', 'item', 'prediction'
    ],
    'page_size': 25,
    'secret_token': 'test',
    'secret_token_editing': '',
    'template': '../corpora/index.html',
    'secret_token_help': None,


}
