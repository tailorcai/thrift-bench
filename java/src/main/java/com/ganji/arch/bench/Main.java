package com.ganji.arch.bench;

import java.net.InetSocketAddress;
import java.net.UnknownHostException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.Random;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TBinaryProtocol.Factory;
import org.apache.thrift.server.TThreadedSelectorServer;
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TNonblockingServerSocket;
import org.apache.thrift.transport.TTransportException;


public class Main implements BenchService.Iface{

	public static void main(String[] args) {
		String host ="0.0.0.0";
		Integer port = 54343;
		
		TNonblockingServerSocket socket = null;
		try {
			socket = new TNonblockingServerSocket(new InetSocketAddress(host, port));
		} catch (TTransportException e) {
			//e.printStackTrace();
			System.exit(-1);
		}
		
		TThreadedSelectorServer.Args arg = new TThreadedSelectorServer.Args(socket);
		
		Main m = new Main();
		BenchService.Processor<BenchService.Iface> processor = new BenchService.Processor<BenchService.Iface>(m);
		arg.processor(processor);

		Factory protocolFactory = new TBinaryProtocol.Factory(false, false);
		arg.protocolFactory(protocolFactory);
		arg.outputTransportFactory(new TFramedTransport.Factory());
		arg.inputTransportFactory(new TFramedTransport.Factory());

		TThreadedSelectorServer server = new TThreadedSelectorServer(arg);
		server.serve();
	}

	public int test(int v) throws org.apache.thrift.TException
	{
		return 0;
	}
}
