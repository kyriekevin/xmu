#ifndef SENDER_H
#define SENDER_H

#define WIN32_LEAN_AND_MEAN // ����һЩ�����������
#include <conio.h>
#include <iostream>
#include <string>
#include <WinSock2.h>
#include <WS2tcpip.h>
#include <vector>
#pragma comment(lib, "WS2_32.lib")
using namespace std;

#define SERVER_IP "192.168.1.104"  // Ĭ�Ϸ�������IP��ַ
#define SERVER_PORT 8307 // �������˿ں�

class Client {
private:
	int user;
	int writing;
	sockaddr_in serverAddr;
	void sendData();
public:
	Client();
	int init();
	void process();
	void getInfo(string& input, vector<string>& info);
	bool isNum(string str);
	vector<string> split(char* str);
};

#endif // !SENDER_H
