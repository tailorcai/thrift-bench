#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from bench import BenchService
from bench.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket

class BenchHandler:
  def __init__(self):
    self.log = {}

  def test(self,v):
    return 0

handler = BenchHandler()
processor = BenchService.Processor(handler)
transport = TSocket.TServerSocket(port=54343)
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()
print "done!"

