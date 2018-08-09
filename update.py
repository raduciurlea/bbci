import base64
import json
import os
import requests
from dateutil.parser import parse

# config = {
#     'owner': os.environ['BB_OWNER'],
#     'repo': os.environ['BB_REPO'],
#     'user': os.environ['BB_USER'],
#     'pass': os.environ['BB_PASS'],
# }


def make_status(url, description, state):
    return {
        'key': 'GCPBUILD',
        'name': 'Cloud Build',
        'url': url,
        'description': description,
        'state': state,
    }


def post_status(commit, status, config):
    url = 'https://api.bitbucket.org/2.0/repositories/{}/{}/commit/{}/statuses/build'.format(config['owner'], config['repo'], commit)
    requests.post(url, auth=(config['user'], config['pass']), json=status)


# post_status('645816c785e4b5ec1dd35237f10632f36e3e5405', build_status, config)


STATES = {
    'WORKING': 'INPROGRESS',
    'SUCCESS': 'SUCCESSFUL',
    'FAILURE': 'FAILED',
}


def process(msg):
    status = STATES.get(msg['status'])
    if not status:
        return
    url = msg['logUrl']
    commit = msg['sourceProvenance']['resolvedRepoSource']['commitSha']
    steps = len(msg['steps'])
    if status == 'INPROGRESS':
        description = 'Build started ({} steps)'.format(steps)
    else:
        duration = (parse(msg['finishTime']) - parse(msg['startTime'])).seconds
        if status == 'SUCCESSFUL':
            description = 'Build succeeded in {}s ({} steps)'.format(duration, steps)
        else:
            description = 'Build failed in {}s ({} steps)'.format(duration, steps)

    print(commit, url, description, status)


def handle_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    process(pubsub_message)
