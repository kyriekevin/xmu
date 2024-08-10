#ifndef SERVER_H
#define SERVER_H

#include <iostream>
#include <WinSock2.h>
#include <vector>
#include <queue>
#include <map>
#include <WS2tcpip.h>
#include <thread>
#include <string>
#include <sstream>
#pragma comment(lib, "WS2_32.lib")
#define CK_MSG WM_USER+100
using namespace std;

// ����ӿͻ��˽��յ���Ϣ��������Ϣ�͵�ַ
struct messageData {
	string msg;
	sockaddr_in addr;
	messageData(string m, sockaddr_in a) : msg(m), addr(a) {}
};

// ����ͻ�����Ϣ
struct clientData {
	sockaddr_in clientAddr;
	string username, password, serialNum;
	thread* corrThread;
	clientData() : username{ "" }, password{ "" }, serialNum{ "" }, corrThread{ nullptr } {
		clientAddr = sockaddr_in();
	}

	clientData(sockaddr_in& Addr, string name, string pwd, string num, thread* thr)
		: clientAddr{ Addr }, username{ name }, password{ pwd }, serialNum{ num }, corrThread{ thr }{}
};

// ���¶��е�Ԫ��
struct updateTuple {
	sockaddr_in clientAddr;
	bool status;
	updateTuple(sockaddr_in addr, bool flag) :clientAddr{ addr }, status{ flag }{}
};

class Server {
	SOCKET socket1;
	sockaddr_in serverAddr;
	void init();
public:
	Server();
	void sendToClient(sockaddr_in* clientAddr, string msg);
	void receieveFromClient();
	queue<messageData> msgBuf;
};


#endif // !SERVER_H

