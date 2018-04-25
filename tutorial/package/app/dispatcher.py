from app.inventory import devices
from app.templating import render_file
from fbtftp.base_handler import StringResponseData
import os
from app import configuration as C


class TftpData:

    def __init__(self, filename):
        path = os.path.join(C.TFTP_ROOT, filename)
        self._size = os.stat(path).st_size
        self._reader = open(path, 'rb')

    def read(self, data):
        return self._reader.read(data)

    def size(self):
        return self._size

    def close(self):
        self._reader.close()


def request_dispatcher(file_path):

    if "__" in file_path:
        neighbor_host, neighbor_if = file_path.split('__')
        neighbor_if = neighbor_if.split('.')[0]
        for interface in devices[neighbor_host]['links']:
            if neighbor_if == interface['interface_brief']:
                ztp_host = interface['neighbor']

        ztp_device = {}
        ztp_device['hostname'] = ztp_host
        ztp_device['staging_user'] = C.STAGING_USER
        ztp_device['staging_password'] = C.STAGING_PASS
        ztp_device.update(devices[ztp_host])

        config = render_file("base-configuration",
                             **ztp_device)

        return StringResponseData(config)

    elif file_path == 'network-confg':
        config = render_file(file_path, staging_user=staging_user,
                             staging_password=staging_password)
        return StringResponseData(config)
    else:
        return TftpData(file_path)
