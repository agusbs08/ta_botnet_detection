#!/usr/bin/env python
"""Run `snort -A console` and print each alert as soon as it is generated using pty."""
import os
import pty
import pyparsing as pyp
import re
import numpy as np
import pandas as pd
from datetime import datetime
import json
from subprocess import Popen, STDOUT
from kafka import KafkaProducer


# initialize kafka producer
bootstrap_servers = ['localhost:9092']
topicName = 'snortlog'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

# start snort process
master_fd, slave_fd = pty.openpty()  # provide tty to enable
                                     # line-buffering on snort's side
snort_process = Popen(['snort', '-A', 'console', '-c', '/etc/snort/snort.conf', '-y'],
                      stdout=slave_fd, stderr=STDOUT, close_fds=True)
os.close(slave_fd)
with os.fdopen(master_fd, 'Ur') as pipe:
    try:
        for line in iter(pipe.readline, ''):
            # detect alert based on the output and run the script here
	    try:
	    	result = re.search("^(\d+/\d+/\d+-\d+:\d+:\d+.+\d).+?\]\s+\[([\d:]+)\]\s+(.+?)\s+\[.+?Classification:\s+(.+?)\].+?Priority:\s+(\d+)\]\s+\{(.+?)\}\s+(\d+\.\d+\.\d+\.\d+):?(\d+)?\s+->\s+(\d+\.\d+\.\d+\.\d+):?(\d+)?", line)
		strDate = result.group(1)
		date = pd.to_datetime(strDate ,format='%m/%d/%y-%H:%M:%S.%f')
		ts = np.float64(date.timestamp())
		
		x = {
			"timestamp" : ts,
			"ipSource" : result.group(7),
			"portSource" : str(result.group(8)),
			"ipDestination" : result.group(9),
			"portDestination" : str(result.group(10)),
			"label" : result.group(4)
		}
		resultJson = json.dumps(x)
  	    	producer.send(topicName, resultJson)
		print(resultJson)
            except Exception as e:
		print(e)
    except KeyboardInterrupt:
        pass
#NOTE: no need to handle EIO -- there is no EOF (snort runs forever)
