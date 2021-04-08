from icmplib import ping, multiping, traceroute, resolve, Host, Hop

"""
import ipaddress

def validate_ip(msg):
    try:
        ip = ipaddress.ip_address(msg)
        return str(ip) + ' is a correct IP' + str(ip.version) + ' address.'
    except ValueError as e:
        return 'Error in IP: ' + str(e)
"""

def trace(ip):
    answer = '\ttracerout {0:s}\n'.format(ip)
    try:
        hops = traceroute(ip, max_hops=100)

        dist_header = "Distance/TTL"
        addr_header = "Address"
        rtt_header = "Average round-trip time"

        answer += '{0:^3} {1:^39} {2:^8}\n'.format('TTL', 'Address', 'RTT (ms)')
        last_distance = 0

        for hop in hops:  
            if last_distance + 1 != hop.distance:
                answer += 'Some gateways are not responding\n'

            # See the Hop class for details
            answer += '{0:<3} {1:<39} {2:<8}\n'.format(hop.distance, hop.address, hop.avg_rtt)

            last_distance = hop.distance  

    except Exception as e:
        answer = str(e)

    return answer
    
