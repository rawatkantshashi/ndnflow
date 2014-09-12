#!/usr/bin/env python
from ndn_flow import FlowProducer

import os
import os.path
import sys
import signal
import socket

def main():
    #ip = get_ip_address("en0")
    
    hostname = socket.gethostname().strip()
    producername = ""
    if hostname == "Shock-MBA.local" or hostname == "shockair.local":
        producername = "local"
    elif hostname == "shock-vb":
        producername = "guoao"
    elif hostname == "j06":
        producername = "j06"
    elif hostname == "zhaogeng-OptiPlex-780":
        producername = "l07"
    elif hostname == "ndngateway2":
        producername = "tbed"
    elif hostname == "R710":   
        producername = "super"
    elif hostname == "user-virtual-machine":
        producername = "telcom"
    elif hostname == "shock-pc":
        producername = "h243"
    elif hostname == "ndn":
        producername = "h242"
    elif hostname == "ubuntuxyhu":
        producername = "seu"
    elif hostname == "clarence-VirtualBox": #node is down
        producername = "vt"
    else:
        producername = "local"
        print "!!!! unknown hostname: %s. We just use the producer prefix: local" %(hostname)
        #return
    
    #producer = Producer(name="/%s/chunksize/dir/x" %(producername), path="./dir/c", is_dir=False)
    #producer.start()
    media_path = os.path.dirname(__file__)
    media_path = os.path.join(media_path, "dir/")
    producer = Producer(name="/%s/chunksize/dir" %(producername), path=media_path, is_dir=True)
    producer.start()
    
class Producer(FlowProducer):
    def __init__(self, name, path, is_dir=True):
        FlowProducer.__init__(self, name=name, path=path, is_dir=is_dir)
    
    def start(self):
        print "start producer"
        FlowProducer.start(self)
        
def signal_handler(signal, frame):
        print "--------------YOU PRESS CTRL+C, PROGRAM QUITE!--------------"
        sys.exit(0)

if __name__=="__main__":
    signal.signal(signal.SIGINT, signal_handler)
    #testEstimator()
    #testFlowConsumer()
    #testFlowConsumer()
    main()
    #testFlowConsumer()
