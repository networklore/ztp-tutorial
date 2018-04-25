import time
from napalm import get_network_driver


def get_napalm_connection(host, device_type, attempts=360, timeout=1):
    driver = get_network_driver(device_type)
    device = driver(hostname=host, username='staging',
                    password='DeploymentK3y')

    for _ in range(attempts):
        try:
            device.open()
            return device
        except:
            time.sleep(timeout)

    return False
