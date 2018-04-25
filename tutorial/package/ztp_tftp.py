from fbtftp.base_handler import BaseHandler
from fbtftp.base_server import BaseServer
from app.broker import trigger_job
from app.dispatcher import request_dispatcher


LISTEN_ON = '0.0.0.0'
SERVER_PORT = 69
RETRIES = 3
TIMEOUT = 5


class DynamicHandler(BaseHandler):

    def get_response_data(self):
        return request_dispatcher(self._path)


class TftpServer(BaseServer):

    def get_handler(self, server_addr, peer, path, options):
        return DynamicHandler(
            server_addr, peer, path, options, session_stats)


def session_stats(stats):
    print('')
    print('#' * 60)
    print('Peer: {} UDP/{}'.format(stats.peer[0], stats.peer[1]))
    print('File: {}'.format(stats.file_path))
    print('Sent Packets: {}'.format(stats.packets_sent))
    print('#' * 60)

    if stats.packets_sent > 0:
        trigger_job(stats.peer[0], stats.file_path)


def main():
    server = TftpServer(LISTEN_ON, SERVER_PORT, RETRIES, TIMEOUT)
    try:
        server.run()
    except KeyboardInterrupt:
        server.close()


if __name__ == '__main__':
    main()
