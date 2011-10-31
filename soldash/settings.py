HOSTS = [
    {
        'hostname': 'localhost',
        'port': 8983,
        'auth': {}
    }
]

INDEXES = [None]

TIMEOUT = 1

JS_REFRESH = 2

HIDE_STATUS_MSG_SUCCESS = 2

HIDE_STATUS_MSG_ERROR = 5

DEBUG = True

RESPONSEHEADERS = {0: 'ok'}

COMMANDS = [
    {'command': 'fetchindex', 'title': 'Fetch Index', 'reverse': 'abortfetch'},
    {'command': 'enablepoll', 'title': 'Polling', 'reverse': 'disablepoll'},
    {'command': 'enablereplication', 'title': 'Replication', 'reverse': 'disablereplication'}, 
    {'command': 'details', 'title': False}, 
    {'command': 'filelist', 'title': 'File List'},
    {'command': 'backup', 'title': 'Backup'},
    {'command': 'restart', 'title': 'Restart Solr'}
]
