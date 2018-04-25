from fbtftp.base_handler import BaseHandler
from fbtftp.base_server import BaseServer

import os


LISTEN_ON = '0.0.0.0'
SERVER_PORT = 69
TFTP_ROOT = '/opt/ztp/tftproot'
RETRIES = 3
TIMEOUT = 5


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


class StaticHandler(BaseHandler):

    def get_response_data(self):
        return TftpData(self._path)


class TftpServer(BaseServer):

    def get_handler(self, server_addr, peer, path, options):
        return StaticHandler(
            server_addr, peer, path, options, session_stats)


def session_stats(stats):
    print('')
    print('#' * 60)
    print('Peer: {} UDP/{}'.format(stats.peer[0], stats.peer[1]))
    print('File: {}'.format(stats.file_path))
    print('Sent Packets: {}'.format(stats.packets_sent))
    print('#' * 60)


def main():
    server = TftpServer(LISTEN_ON, SERVER_PORT, RETRIES, TIMEOUT)
    try:
        server.run()
    except KeyboardInterrupt:
        server.close()


if __name__ == '__main__':
    main()
