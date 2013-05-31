// This autogenerated skeleton file illustrates how to build a server.
// You should copy it to another filename to avoid overwriting it.

#include "BenchService.h"
#include <thrift/concurrency/ThreadManager.h>
#include <thrift/concurrency/PosixThreadFactory.h>

#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/server/TNonblockingServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TBufferTransports.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;
using namespace ::apache::thrift::concurrency;

using boost::shared_ptr;

//using namespace  ;

class BenchServiceHandler : virtual public BenchServiceIf {
 public:
  BenchServiceHandler() {
    // Your initialization goes here
  }

  int32_t test(const int32_t v) {
    // Your implementation goes here
    //printf("test\n");
    return 0;
  }

};

int main(int argc, char **argv) {
  int port = 54343;
  shared_ptr<BenchServiceHandler> handler(new BenchServiceHandler());
  shared_ptr<TProcessor> processor(new BenchServiceProcessor(handler));
  shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  shared_ptr<TTransportFactory> transportFactory(new TFramedTransportFactory());
  shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  printf("Starting server\n");
  int workerCount = 10;
  shared_ptr<ThreadManager> threadManager =  ThreadManager::newSimpleThreadManager(workerCount);
  shared_ptr<ThreadFactory> threadFactory(new PosixThreadFactory());
  threadManager->threadFactory(threadFactory);
  threadManager->start();

  TNonblockingServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}

