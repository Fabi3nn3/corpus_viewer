DICT_SETTINGS_VIEWER = {
    'name': 'Database Annotation',
    'description': 'This corpus gets its data from a database',
    'data_type': 'database',
    'app_label': 'web_page_annotation',
    'model_name': 'Annotation_Model',
    'database_prefetch_related': [
    ],
    'database_select_related': [
    ],
    'database_filters': {
    },

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
    'secret_token_editing': '',
    'cards': [
        {
            'name': 'Load dummy data',
            'content': '''
                <div class="mb-2">
                    Press the button below to load the dummy data
                </div>
                <div class="">
                    <button type="button" id="button_index_dummy_data" class="btn btn-sm btn-primary">Load</button>
                </div>
                <script>
                    $(document).ready(function()
                    {
                        $(document).on('click', '#button_index_dummy_data', function(e) {
                            $.ajax({
                                url: '/web_page_annotation',
                                contentType: 'application/json',
                                success: function(result) {
                                    load_current_page();
                                }
                            })
                        });

                    });
                </script>
            '''
        }
    ],
    # 'secret_token': 'test',
    # 'secret_token': 'test',
    'secret_token_editing': '',
    # 'template': '../corpora/index.html'
}
