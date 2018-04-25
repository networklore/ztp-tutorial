from app.network import get_napalm_connection
from app.notifications import notify_slack


def ztp_start(host, file):
    msg = '{} downloaded {}'.format(host, file)
    notify_slack(msg)
    dev = get_napalm_connection(host, 'ios')

    if dev:
        notify_slack('{} connection established'.format(host))
    else:
        notify_slack('{} connection failed, giving up'.format(host))
        return

    facts = dev.get_facts()

    notify_slack('{}: {}/{}'.format(host, facts['model'],
                                    facts['serial_number']))

    lldp = dev.get_lldp_neighbors()
    for interface in lldp:
        for neighbor in lldp[interface]:
            notify_slack('{}:{} -> {}: {}'.format(
                host, interface, neighbor['hostname'],
                neighbor['port']))

    dev.close()
