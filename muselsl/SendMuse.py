import socket
import argparse
import time
import os

from muselsl import record,list_muses
from pythonosc import udp_client

eeg_file = 'sample_eeg_data.csv'
record(60,'./sample_eeg_data.csv')
#os.system("muselsl record -d 60 -f ./sample_eeg_data.csv")

data_array = []
with open(eeg_file) as f:
    for line in f:
        data = line.split()
        data_array.append(data[0])
#print(data_array)]
file_len = len(data_array)

UDP_IP = "127.0.0.1"
UDP_PORT = 1234

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=1234,
    help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

count = 1
while True:
    s = " ".join(data_array[count].split(","))
    client.send_message("/filter", s)
    print(s)
    if count >= file_len-1:
        count = 1
    else:
        count += 1
