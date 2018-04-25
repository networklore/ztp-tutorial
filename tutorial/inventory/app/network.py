import os
import time
from napalm import get_network_driver

staging_user = os.environ.get('ZTP_STAGING_USER')
staging_password = os.environ.get('ZTP_STAGING_PASS')


def get_napalm_connection(host, device_type, attempts=360, timeout=1):
    driver = get_network_driver(device_type)
    device = driver(hostname=host, username=staging_user,
                    password=staging_password)

    for _ in range(attempts):
        try:
            device.open()
            return device
        except:
            time.sleep(timeout)

    return False
