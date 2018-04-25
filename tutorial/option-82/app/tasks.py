from app.inventory import devices
from app.network import get_napalm_connection
from app.notifications import notify_slack


def ztp_start(host, file):
    if '__' in file:
        neighbor_host, neighbor_if = file.split('__')
        neighbor_if = neighbor_if.split('.')[0]
        ztp_device = False
        for interface in devices[neighbor_host]['links']:
            if neighbor_if == interface['interface_brief']:
                ztp_device = interface['neighbor']
                ztp_interface = interface['neighbor_if']
                ztp_platform = devices[ztp_device]['platform']
                mgmt_ip = devices[ztp_device]['management_ip']
        if ztp_device:
            msg = '{}/{} connected {}, expecting {}/{} ({})'.format(
                neighbor_host, neighbor_if, host, ztp_device,
                ztp_interface, ztp_platform)
        else:
            msg = "{}/{} connected {}, that doesn't look right...".format(
                neighbor_host, neighbor_if, host)

        host = mgmt_ip
        notify_slack(msg)

    else:
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
