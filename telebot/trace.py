from icmplib import traceroute, Hop

def trace(ip):
    answer = '\ttracerout {0:s}\n'.format(ip)
    try:
        hops = traceroute(ip, max_hops=100)

        header = '{0:^3} {1:^39} {2:^8}\n'.format('TTL', 'Address', 'RTT (ms)')
        answer += header + '-'* (len(header) - 1) + "\n"
        last_distance = 0

        for hop in hops:  
            if last_distance + 1 != hop.distance:
                answer += 'Some gateways are not responding\n'

            # See the Hop class for details
            answer += '{0:<3} {1:<39} {2:<8}\n'.format(hop.distance, hop.address, hop.avg_rtt)

            last_distance = hop.distance  

    except Exception as e:
        answer = "Something went wrong with your address: " + str(e)

    return answer
