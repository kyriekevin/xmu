#ifndef RECEIVER_H
#define RECEIVER_H

#include <iostream>
#include <WinSock2.h>
#include <vector>
#include <WS2tcpip.h>
#pragma comment(lib,"ws2_32.lib")
using namespace std;

#define SERVER_IP "192.168.1.104"  // Ĭ�Ϸ�������IP��ַ
#define SERVER_PORT 8307 // �������˿ں�

class Server {
private:
	int listener; // �����׽���
	sockaddr_in serverAddr; // IPV4��ַ
	vector<int> socNum; // ��Ŵ������׽���

public:
	Server();
	void init();
	void process();
	vector<string> split(char* str);
};

#endif // !RECEIVER_H
