#define _WINSOCK_DEPRECATED_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#include "sender.h"
using namespace std;

string serialNumber; // �û���������к�
bool status = false; // false��ʾ������û�б�����true��ʾ����������

// ���ÿͻ�����Ϣ
Client::Client() : user{ 0 }, writing{ 0 } {
	serverAddr.sin_family = PF_INET; // ipv4
	serverAddr.sin_port = SERVER_PORT; // host to net  unsigned short �������˿ں�
	serverAddr.sin_addr.s_addr = inet_addr(SERVER_IP); // ��������ַ
}

// ���г�ʼ��������0��ʾ��ʼ���ɹ�������-1��ʾ��ʼ��ʧ�ܣ���Ҫ�������ӷ�����
int Client::init() {
	int iRet;
	WORD ver = MAKEWORD(2, 2); // ʹ�ð汾2.2
	WSADATA data; // ���ڳ�ʼ���׽��ֻ���
	iRet = WSAStartup(ver, &data);

	if (iRet == SOCKET_ERROR) {
		cerr << "WSAStartup() fail " << iRet << endl;
		WSACleanup();
	}
	else cout << "WSAStartup success" << endl;

	// �����׽���
	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0); // ����ipv4,TCP����
	user = sock;

	if (sock <= 0) {
		cerr << "connect fail " << WSAGetLastError() << endl;
		exit(-1);
	}

	// ����ʽ�صȴ�����������
	iRet = connect(sock, (sockaddr*)&serverAddr, sizeof sockaddr_in);
	if (iRet < 0) {
		cerr << "connect fail " << WSAGetLastError() << endl;
		return -1;
	}

	cout << "connect IP: " << SERVER_IP << " Port: " << SERVER_PORT << " success" << endl;
	return 0;
}

void Client::process() {
	char recvBuf[1024] = {};
	fd_set fdRead, fdWrite;
	FD_ZERO(&fdRead);
	FD_ZERO(&fdWrite);

	int flag = init();
	if (flag == -1) {
		Sleep(10000); // 10������������ӷ�����
		return;
	}

	while (true) {
		FD_SET(user, &fdRead);
		if (writing == 0)
			FD_SET(user, &fdWrite);
		struct timeval timeout = { 1, 0 }; // ����ÿ��1��selectһ��
		switch (select(0, &fdRead, &fdWrite, nullptr, &timeout)) {
		case -1: {
			cerr << "error: " << WSAGetLastError() << endl;
			break;
		}
		case 0:
			break;
		default: {
			// ���շ���˷��ͻص���Ϣ
			if (FD_ISSET(user, &fdRead)) {
				int size = recv(user, recvBuf, sizeof(recvBuf) - 1, 0);
				if (size > 0) {
					cerr << "Server reply: " << recvBuf << endl;
					memset(recvBuf, '\0', sizeof recvBuf);
				}
				else {
					cout << "The server is closed and waiting for the server to start" << endl;
					Sleep(10000);
					cout << "Begin trying to reconnect to the server" << endl;
					status = true;
					return;
				}
			}
			if (FD_ISSET(user, &fdWrite)) {
				FD_ZERO(&fdWrite);
				writing = 1; // ��ʾд״̬
				sendData();
			}
			break;
		}
		}
	}
}

// ���������Ϣ���ݿո���зָ�
vector<string> Client::split(char* str) {
	vector<string> item;
	const char* blank = " ";
	char* ch = strtok(str, blank);
	while (ch) {
		item.emplace_back(ch);
		ch = strtok(nullptr, blank);
	}

	return item;
}

// �ж�������ַ����Ƿ�ȫ����������ɣ�����Ƿ���true�����򷵻�false
bool Client::isNum(string str) {
	bool flag = true;
	for (auto ch : str) {
		if (ch < '0' || ch > '9') {
			flag = false;
			break;
		}
	}

	return flag;
}

void Client::getInfo(string& input, vector<string>& info) {
	getline(cin, input);
	info.clear();
	// ���û��������Ϣ�н�ȡ�����кţ��û���������
	info = split((char*)input.c_str());

	return;
}

void Client::sendData() {
	string input;
	vector<string> info;
	getInfo(input, info);

	// ���������Ϣ����У�飬û�д����������˷�����Ϣ
	while (true) {
		if (info.size() < 2 || info.size() > 3) {
			cerr << "Please enter at least a username and password" << endl;
			cerr << "And please enter the serial number, username, password or username, password in the order separated by Spaces" << endl;
			getInfo(input, info);
			continue;
		}
		// ��������Ϊ�����������������кţ���Ҫ�����кŽ��м���
		else if (info.size() == 3) {
			serialNumber = info[0];
			if (serialNumber.size() != 10) {
				cerr << "The serial number should be 10 in length.Please re-enter all information: " << endl;
				getInfo(input, info);
				continue;
			}
			else if (!isNum(serialNumber)) {
				cerr << "The serial number was incorrectly entered.Please re-enter all information:" << endl;
				getInfo(input, info);
				continue;
			}
			else break;
		}
		else break; // ��������Ϊ�������û�����кţ�����Ҫ���м���
	}

	// ���ͻ�����������кŷ��͸������������֤
	string str;
	if (info.size() == 3) str = info[0] + " " + info[1] + " " + info[2];
	else str = info[0] + " " + info[1];

	send(user, str.c_str(), sizeof str, 0);
	writing = 0;

	return;
}

int main() {
	Client user;
	while (true) user.process();

	return 0;
}