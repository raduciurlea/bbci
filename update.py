import requests

config = {
    'owner': 'tremend',
    'repo': 'carrefour-order-management-system-coms',
    'user': 'radu.ciurlea@tremend.com',
    'pass': 'Iq86KEwr4Isx',
}

build_status = {
    'key': 'BBS',
    'name': 'Test Bitbucket Build Status',
    'url': 'https://bitbucket.org/tpettersen/bitbucket-build-status',
    'description': 'A test Bitbucket build status',
    'state': 'FAILED',
}


def post_status(commit, status, config):
    url = 'https://api.bitbucket.org/2.0/repositories/{}/{}/commit/{}/statuses/build'.format(config['owner'], config['repo'], commit)
    requests.post(url, auth=(config['user'], config['pass']), json=status)


post_status('645816c785e4b5ec1dd35237f10632f36e3e5405', build_status, config)
