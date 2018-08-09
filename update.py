import json
import os
import requests
from pprint import pprint

config = {
    'owner': os.environ['BB_OWNER'],
    'repo': os.environ['BB_REPO'],
    'user': os.environ['BB_USER'],
    'pass': os.environ['BB_PASS'],
}


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

msg_queued = '''
{"id":"83a6f7f6-aae8-4c9b-8fbf-9876aa7c4471","projectId":"c4-order-management","status":"QUEUED","source":{"repoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","branchName":"master"}},"steps":[{"name":"debian","args":["ls"]},{"name":"debian","args":["cal"]}],"createTime":"2018-08-09T11:21:12.597253221Z","timeout":"600s","logsBucket":"gs://657212652564.cloudbuild-logs.googleusercontent.com","sourceProvenance":{"resolvedRepoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","commitSha":"fb92e1d38809676b71a677dfef4d953e639106f4"}},"buildTriggerId":"310e28d0-08f3-4ca0-b0c4-ed230c4baa38","options":{"substitutionOption":"ALLOW_LOOSE"},"logUrl":"https://console.cloud.google.com/gcr/builds/83a6f7f6-aae8-4c9b-8fbf-9876aa7c4471?project=657212652564","tags":["event-303ee07b-8e3d-4e61-b3d1-3120c6905d72","trigger-310e28d0-08f3-4ca0-b0c4-ed230c4baa38"]}
'''

msg_working = '''
{"id":"83a6f7f6-aae8-4c9b-8fbf-9876aa7c4471","projectId":"c4-order-management","status":"WORKING","source":{"repoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","branchName":"master"}},"steps":[{"name":"debian","args":["ls"]},{"name":"debian","args":["cal"]}],"createTime":"2018-08-09T11:21:12.597253221Z","startTime":"2018-08-09T11:21:13.893111478Z","timeout":"600s","logsBucket":"gs://657212652564.cloudbuild-logs.googleusercontent.com","sourceProvenance":{"resolvedRepoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","commitSha":"fb92e1d38809676b71a677dfef4d953e639106f4"}},"buildTriggerId":"310e28d0-08f3-4ca0-b0c4-ed230c4baa38","options":{"substitutionOption":"ALLOW_LOOSE"},"logUrl":"https://console.cloud.google.com/gcr/builds/83a6f7f6-aae8-4c9b-8fbf-9876aa7c4471?project=657212652564","tags":["event-303ee07b-8e3d-4e61-b3d1-3120c6905d72","trigger-310e28d0-08f3-4ca0-b0c4-ed230c4baa38"]}
'''

msg_fail = '''
{"id":"83a6f7f6-aae8-4c9b-8fbf-9876aa7c4471","projectId":"c4-order-management","status":"FAILURE","source":{"repoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","branchName":"master"}},"steps":[{"name":"debian","args":["ls"],"timing":{"startTime":"2018-08-09T11:21:19.512566401Z","endTime":"2018-08-09T11:21:20.495784224Z"},"status":"SUCCESS"},{"name":"debian","args":["cal"],"timing":{"startTime":"2018-08-09T11:21:20.495800332Z","endTime":"2018-08-09T11:21:20.806879594Z"},"status":"FAILURE"}],"results":{"buildStepImages":["","sha256:a0cd2c88c5cc65499e959ac33c8ebab45f24e6348b48d8c34fd2308fcb0cc138"],"buildStepOutputs":[]},"createTime":"2018-08-09T11:21:12.597253221Z","startTime":"2018-08-09T11:21:13.893111478Z","finishTime":"2018-08-09T11:21:21.498455840Z","timeout":"600s","logsBucket":"gs://657212652564.cloudbuild-logs.googleusercontent.com","sourceProvenance":{"resolvedRepoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","commitSha":"fb92e1d38809676b71a677dfef4d953e639106f4"}},"buildTriggerId":"310e28d0-08f3-4ca0-b0c4-ed230c4baa38","options":{"substitutionOption":"ALLOW_LOOSE"},"logUrl":"https://console.cloud.google.com/gcr/builds/83a6f7f6-aae8-4c9b-8fbf-9876aa7c4471?project=657212652564","tags":["event-303ee07b-8e3d-4e61-b3d1-3120c6905d72","trigger-310e28d0-08f3-4ca0-b0c4-ed230c4baa38"],"timing":{"BUILD":{"startTime":"2018-08-09T11:21:19.512547689Z","endTime":"2018-08-09T11:21:20.853589829Z"},"FETCHSOURCE":{"startTime":"2018-08-09T11:21:16.654064926Z","endTime":"2018-08-09T11:21:19.495646441Z"}}}
'''

# pprint(json.loads(msg_queued))
# pprint(json.loads(msg_working))
pprint(json.loads(msg_fail))
