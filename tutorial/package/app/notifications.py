import json
import requests
from app import configuration as C


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'ZTP Server'
}


def notify_slack(msg):
    url = 'https://hooks.slack.com/services/' + C.SLACK_TOKEN
    data = {}
    data['text'] = msg
    requests.post(url, headers=headers, data=json.dumps(data))
