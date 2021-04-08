from icmplib import traceroute, Hop
import os
import subprocess

ROOT_PRIVILEGES = os.getuid() == 0
if not ROOT_PRIVILEGES:
    print('No root privileges. Will be use tracepath instead of traceroute')

def trace(message):
    # filter message (allowed digits, alphabet, ",", ":", "/")
    ip = "".join([character for character in message 
                                        if character.isalnum() or character in ":./"])

    if ROOT_PRIVILEGES:
        return trace_traceroute(ip)

    return trace_tracepath(ip)

def trace_tracepath(ip):
    answer = ""
    try:
        action = subprocess.run(['tracepath', '-n', ip], capture_output=True, text=True)
        answer = action.stdout
        if not answer:
            answer = action.stderr
    except:
        # tracepath is supported only by Unix systems 
        answer = "System is not ready, please contact later"

    return answer

def trace_traceroute(ip):
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
