from app.templating import render_file
from fbtftp.base_handler import StringResponseData
import os

TFTP_ROOT = '/opt/ztp/tftproot'

staging_user = os.environ.get('ZTP_STAGING_USER')
staging_password = os.environ.get('ZTP_STAGING_PASS')


class TftpData:

    def __init__(self, filename):
        path = os.path.join(TFTP_ROOT, filename)
        self._size = os.stat(path).st_size
        self._reader = open(path, 'rb')

    def read(self, data):
        return self._reader.read(data)

    def size(self):
        return self._size

    def close(self):
        self._reader.close()


def request_dispatcher(file_path):

    if file_path == 'network-confg':
        config = render_file(file_path, staging_user=staging_user,
                             staging_password=staging_password)
        return StringResponseData(config)
    else:
        return TftpData(file_path)
