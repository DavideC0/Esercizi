from scapy.all import *
from scapy.layers.http import HTTPRequest
from scapy.layers.http import HTTPResponse
from scapy.layers.inet import IP
ipkt = 0
def process_pkt(pkt):
    global ipkt
    ipkt += 1
    print(f"Ho ricevuto pacchetto {ipkt} lungo {str(pkt[IP].len)} mittente {pkt[IP].src} destinatario {pkt[IP].dst}")

sniff(iface="eth0", filter="tcp", prn=process_pkt)