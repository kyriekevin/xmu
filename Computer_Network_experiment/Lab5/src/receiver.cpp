#define _CRT_SECURE_NO_WARNINGS
#define _WINSOCK_DEPRECATED_NO_WARNINGS

#include "receiver.h"

// ���캯�������÷������Ϣ
Server::Server() : listener{ 0 } {
	serverAddr.sin_family = PF_INET;
	serverAddr.sin_port = SERVER_PORT;
	serverAddr.sin_addr.s_addr = inet_addr(SERVER_IP);
}

// ��ʼ�����������������׽��֣��󶨶˿ڲ����м���
void Server::init() {
	int iRet;
	WORD ver = MAKEWORD(2, 2); // ʹ�ð汾2.2
	WSADATA data; // ���ڳ�ʼ���׽��ֻ���
	iRet = WSAStartup(ver, &data);

	// ��ʼ��WinSock����
	if (iRet == SOCKET_ERROR) {
		cerr << "WSAStartup fail " << iRet << endl;
		WSACleanup();
	}
	else cout << "WSAStartup success" << endl;

	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0); // ����ipv4,TCP����
	listener = sock;

	if (sock == INVALID_SOCKET) {
		cerr << "SOCKET fail " << WSAGetLastError() << endl;
		exit(-1);
	}
	else cout << "SOCKET success" << endl;

	unsigned long ul = 1;
	iRet = ioctlsocket(sock, FIONBIO, (unsigned long*)&ul);
	if (iRet == -1) {
		cerr << "ioctlsocket fail" << endl;
		exit(-1);
	}
	else cout << "ioctlsocket success" << endl;

	// ������˿�
	iRet = bind(sock, (sockaddr*)&serverAddr, sizeof sockaddr_in);
	if (iRet == SOCKET_ERROR) {
		cerr << "bind fail" << endl;
		exit(-1);
	}
	else cout << "bind success" << endl;

	// listen����
	iRet = listen(sock, 6);
	if (iRet == SOCKET_ERROR) {
		cerr << "listen fail" << endl;
		exit(-1);
	}
	else cout << "listen success" << endl;

	socNum.emplace_back(listener);
	return;
}

void Server::process() {
	int cnt = 0;
	fd_set fds;
	FD_ZERO(&fds);

	// ��ʼ���������˽�������
	init();

	cout << "Waiting for client information......" << endl;
	while (true) {
		cnt = socNum.size();
		for (int i = 0; i < cnt; ++i)
			FD_SET(socNum[i], &fds);
		struct timeval timeout = { 1, 0 };

		switch (select(0, &fds, nullptr, nullptr, &timeout)) {
		case -1: {
			cerr << "select error: " << WSAGetLastError() << endl;
			Sleep(1000);
			break;
		}
		case 0: break;
		default: {
			// �������е�ÿһ���׽��ֶ���ʣ����׽��ֽ��бȽ�
			for (int i = 0; i < cnt; ++i) {
				// �����һ�����׽��ֿɶ�����Ϣ����ֱ�ӽ�������
				if (i == 0 && FD_ISSET(socNum[i], &fds)) {
					struct sockaddr_in clientAddress;
					socklen_t clientAddrLen = sizeof(struct sockaddr_in);
					// ����һ���û����׽���
					SOCKET csock = accept(listener, (struct sockaddr*)&clientAddress, &clientAddrLen);
					if (csock == INVALID_SOCKET)
						cerr << "accept fail" << endl;
					else {
						cout << "accept success" << endl;
						int clientfd = csock;
						// ����û�������������ʾ��Ϣ����֪ͨ�û����ӳɹ�
						socNum.emplace_back(clientfd);
						cout << "Client " << clientfd << " successfully connected to the server" << endl;
						char ID[1024];
						sprintf(ID, "Hello, your ID is %d", clientfd);

						// ����������ID�����͸��ͻ����ÿͻ���֪���Լ���ID
						send(clientfd, ID, sizeof(ID) - 1, 0); // �۵����һ��������
					}
				}
				if (i != 0 && FD_ISSET(socNum[i], &fds)) {
					char buf[1024]{};
					memset(buf, '\0', sizeof buf);
					int size = recv(socNum[i], buf, sizeof(buf) - 1, 0);
					// ����Ƿ���ֶ������
					if (size == 0 || size == -1) {
						cerr << "Client " << socNum[i] << " is offline" << endl;
						// �ر��ѵ��ߵ��׽��֣������б��������ɾ��
						closesocket(socNum[i]);
						FD_CLR(socNum[i], &fds);
						socNum.erase(socNum.begin() + i);
						cnt--;
					}
					else {
						cout << "Client " << socNum[i] << " said " << buf << endl;
						// ���û����͹�������Ϣ���зָ��ȡ�������кţ��û�������
						vector<string> info = split(buf);
						string str;
						if (info.size() == 2) {
							info[0] = "username: " + info[0];
							info[1] = "password: " + info[1];
							str = info[0] + " " + info[1];
						}
						else {
							info[0] = "serial number: " + info[0];
							info[1] = "username: " + info[1];
							info[2] = "password: " + info[2];
							str = info[0] + " " + info[1] + " " + info[2];
						}

						/*
							��ȡ��Ϣ�����У�飬У�鷽����Ҫ���������
						*/

						// ����Ϣ���͸�������Ϣ�Ŀͻ���
						char client[1024];
						sprintf(client, " Client %d", socNum[i]);
						strcat(client, str.c_str());
						send(socNum[i], client, sizeof(client) - 1, 0);
					}
				}
			}
			break;
		}
		}
	}
}

// ���������Ϣ���ݿո���зָ�
vector<string> Server::split(char* str) {
	vector<string> item;
	const char* blank = " ";
	char* ch = strtok(str, blank);
	while (ch) {
		item.emplace_back(ch);
		ch = strtok(nullptr, blank);
	}

	return item;
}

int main() {
	Server server;
	server.process();

	return 0;
}