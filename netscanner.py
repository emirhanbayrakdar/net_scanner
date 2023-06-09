import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ip", dest="ip_address", help="Enter IP Address")
    (user_input, arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter IP Address")
    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()
user_ip_address=get_user_input()
scan_my_network(user_ip_address.ip_address)

# run this code in terminal 
# echo 1 > /proc/sys/net/ipv4/ip_forward
# this code allows you ip forwarding while performing a man-in-the-middle attack
