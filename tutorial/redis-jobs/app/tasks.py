from app.notifications import notify_slack
import time


def ztp_start(host, file):
    msg = '{} downloaded {}'.format(host, file)
    notify_slack(msg)
    time.sleep(360)
