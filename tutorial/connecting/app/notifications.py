import json
import os
import requests


slack_token = os.environ.get('SLACK_TOKEN')
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'ZTP Server'
}


def notify_slack(msg):
    url = 'https://hooks.slack.com/services/' + slack_token
    data = {}
    data['text'] = msg
    requests.post(url, headers=headers, data=json.dumps(data))
