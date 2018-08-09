import requests
import json
from pprint import pprint

config = {
    'owner': 'tremend',
    'repo': 'carrefour-order-management-system-coms',
    'user': 'radu.ciurlea@tremend.com',
    'pass': 'Iq86KEwr4Isx',
}

build_status = {
    'key': 'MEH',
    'name': 'unit tests',
    'url': 'https://console.cloud.google.com/cloud-build/builds/332b20c2-ca10-4462-96d1-86616620486c?project=c4-order-management',
    'description': 'things went south',
    'state': 'FAILED',
}


def post_status(commit, status, config):
    url = 'https://api.bitbucket.org/2.0/repositories/{}/{}/commit/{}/statuses/build'.format(config['owner'], config['repo'], commit)
    requests.post(url, auth=(config['user'], config['pass']), json=status)


# post_status('645816c785e4b5ec1dd35237f10632f36e3e5405', build_status, config)

msg_queued = '''
{"id":"5fc807a2-9eca-401c-be2d-9c4102795394","projectId":"c4-order-management","status":"QUEUED","source":{"repoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","branchName":"master"}},"steps":[{"name":"debian","args":["ls"]},{"name":"debian","args":["cal"]}],"createTime":"2018-08-09T09:28:28.995517074Z","timeout":"600s","logsBucket":"gs://657212652564.cloudbuild-logs.googleusercontent.com","sourceProvenance":{"resolvedRepoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","commitSha":"1e0362169c99ad9b3f292849d17f0831db7c01b1"}},"buildTriggerId":"310e28d0-08f3-4ca0-b0c4-ed230c4baa38","options":{"substitutionOption":"ALLOW_LOOSE"},"logUrl":"https://console.cloud.google.com/gcr/builds/5fc807a2-9eca-401c-be2d-9c4102795394?project=657212652564","tags":["event-95c8e408-21e6-4925-81f5-336c0e259314","trigger-310e28d0-08f3-4ca0-b0c4-ed230c4baa38"]}
'''

msg_working = '''
{"id":"5fc807a2-9eca-401c-be2d-9c4102795394","projectId":"c4-order-management","status":"QUEUED","source":{"repoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","branchName":"master"}},"steps":[{"name":"debian","args":["ls"]},{"name":"debian","args":["cal"]}],"createTime":"2018-08-09T09:28:28.995517074Z","timeout":"600s","logsBucket":"gs://657212652564.cloudbuild-logs.googleusercontent.com","sourceProvenance":{"resolvedRepoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","commitSha":"1e0362169c99ad9b3f292849d17f0831db7c01b1"}},"buildTriggerId":"310e28d0-08f3-4ca0-b0c4-ed230c4baa38","options":{"substitutionOption":"ALLOW_LOOSE"},"logUrl":"https://console.cloud.google.com/gcr/builds/5fc807a2-9eca-401c-be2d-9c4102795394?project=657212652564","tags":["event-95c8e408-21e6-4925-81f5-336c0e259314","trigger-310e28d0-08f3-4ca0-b0c4-ed230c4baa38"]}
'''

msg_fail = '''
{"id":"5fc807a2-9eca-401c-be2d-9c4102795394","projectId":"c4-order-management","status":"FAILURE","source":{"repoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","branchName":"master"}},"steps":[{"name":"debian","args":["ls"],"timing":{"startTime":"2018-08-09T09:28:34.430974158Z","endTime":"2018-08-09T09:28:35.491113196Z"},"status":"SUCCESS"},{"name":"debian","args":["cal"],"timing":{"startTime":"2018-08-09T09:28:35.491125954Z","endTime":"2018-08-09T09:28:35.794238355Z"},"status":"FAILURE"}],"results":{"buildStepImages":["","sha256:a0cd2c88c5cc65499e959ac33c8ebab45f24e6348b48d8c34fd2308fcb0cc138"],"buildStepOutputs":[]},"createTime":"2018-08-09T09:28:28.995517074Z","startTime":"2018-08-09T09:28:30.420300939Z","finishTime":"2018-08-09T09:28:36.575417001Z","timeout":"600s","logsBucket":"gs://657212652564.cloudbuild-logs.googleusercontent.com","sourceProvenance":{"resolvedRepoSource":{"projectId":"c4-order-management","repoName":"github-raduciurlea-bbci","commitSha":"1e0362169c99ad9b3f292849d17f0831db7c01b1"}},"buildTriggerId":"310e28d0-08f3-4ca0-b0c4-ed230c4baa38","options":{"substitutionOption":"ALLOW_LOOSE"},"logUrl":"https://console.cloud.google.com/gcr/builds/5fc807a2-9eca-401c-be2d-9c4102795394?project=657212652564","tags":["event-95c8e408-21e6-4925-81f5-336c0e259314","trigger-310e28d0-08f3-4ca0-b0c4-ed230c4baa38"],"timing":{"BUILD":{"startTime":"2018-08-09T09:28:34.430954145Z","endTime":"2018-08-09T09:28:35.842827651Z"},"FETCHSOURCE":{"startTime":"2018-08-09T09:28:31.432970549Z","endTime":"2018-08-09T09:28:34.414738029Z"}}}
'''

pprint(json.loads(msg_queued))
# pprint(json.loads(msg_working))
# pprint(json.loads(msg_fail))
