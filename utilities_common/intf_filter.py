# Interface filtering functions
import re
from swsscommon.swsscommon import FRONT_PANEL_PORT_PREFIX_REGEX

SONIC_LAG_NAME_PREFIX = "PortChannel"

def parse_interface_in_filter(intf_filter):
    intf_fs = []

    if intf_filter is None:
        return intf_fs

    fs = intf_filter.split(',')
    for x in fs:
        if '-' in x:
            # handle range
            if not re.search(FRONT_PANEL_PORT_PREFIX_REGEX, x) and not x.startswith(SONIC_LAG_NAME_PREFIX):
                continue
            if x.startswith(SONIC_PORT_NAME_PREFIX):
                intf = SONIC_PORT_NAME_PREFIX
            if x.startswith(SONIC_IB_PORT_NAME_PREFIX):
                intf = SONIC_IB_PORT_NAME_PREFIX
            if x.startswith(SONIC_LAG_NAME_PREFIX):
                intf = SONIC_LAG_NAME_PREFIX
            start = x.split('-')[0].split(intf,1)[1]
            end = x.split('-')[1]

            if not start.isdigit() or not end.isdigit():
                continue
            for i in range(int(start), int(end)+1):
                intf_fs.append(intf+str(i))
        else:
            intf_fs.append(x)

    return intf_fs

def interface_in_filter(intf, filter):
    if filter is None:
        return True

    intf_fs = parse_interface_in_filter(filter)
    if intf in intf_fs:
        return True

    return False

