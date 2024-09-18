from scapy.all import *
from scapy.layers.inet import IP,TCP
from scapy.layers.tls.record import TLS
import scapy.layers.http
from scapy.layers.http import HTTPRequest
from scapy.layers.http import HTTPResponse
from datetime import datetime
import csv
from os.path import exists

def get_tls_sni(pkt):
    try:
        return pkt[TLS].msg[0].ext[0].servernames[0].servername.decode()
    except (IndexError, AttributeError):
        return ""
    
def process_pkt(pkt):
    if IP in pkt and TCP in pkt:
        if pkt[TCP].dport in [80, 443] or pkt[TCP].sport in [80, 443]:
            host = ""
            if HTTPRequest in pkt:
                if pkt[HTTPRequest].Host:
                    host = pkt[HTTPRequest].Host.decode()
                elif TLS in pkt:
                    host = get_tls_sni(pkt)
                if 443 in [pkt[TCP].sport, pkt[TCP].dport]:
                    protocol = "HTTPS" 
                else:
                    protocol = "HTTP"
    if host != "":
        if exists("log.csv"):
            with open("log.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([datetime.now().strftime('%d-%m-%Y %H:%M:%S'), pkt[IP].src, pkt[TCP].sport, pkt[IP].dst, pkt[TCP].dport, host, protocol])
        else:
            with open("log.csv", "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["datetime", "src", "sport", "dst", "dport", "host", "protocol"])
                writer.writerow([datetime.now(), pkt[IP].src, pkt[TCP].sport, pkt[IP].dst, pkt[TCP].dport, host, protocol])    
        
sniff(iface="eth0", filter="tcp port 80 or tcp port 443", prn=process_pkt)

