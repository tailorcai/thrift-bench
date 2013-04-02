#!/usr/bin/env python
#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

import sys,time
sys.path.append("../python/gen-py/bench")
import pprint
from urlparse import urlparse
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol

import BenchService
from ttypes import *

from threading import Thread

HOST = "127.0.0.1"
PORT = 54343
REPEAT = 1000
CONCURRENCY = 10

class BenchWorker(Thread):
  def run(self):
    for i in range(0,REPEAT):
      c,t = self.create()
      c.test(1)
      self.close(t)

  def __init__(self):
    Thread.__init__(self)

  def create(self):
    socket = TSocket.TSocket(HOST, PORT)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = BenchService.Client(protocol)
    transport.open()
    return (client,transport)

  def close(self,transport):
    transport.close()


threads = [ BenchWorker() for i in range(0,CONCURRENCY)]
t = time.time()
for i in threads:
  i.start()

for i in threads:
  i.join()
print "Concurrency=", CONCURRENCY, ", Repeat=",REPEAT
print time.time() - t , "s"