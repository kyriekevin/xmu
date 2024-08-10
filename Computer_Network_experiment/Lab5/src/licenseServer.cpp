#include "server.h"
#pragma warning(disable : 4996)
using namespace std;

Server myServer;
queue<updateTuple> updateBuf; // �ݴ�����еĸ���
map<sockaddr_in, clientData> clientInfo; // ʹ�ÿͻ��˵�ַ���ҿͻ�����Ϣ

bool operator<(const sockaddr_in& l, const sockaddr_in& r) {
	return l.sin_port < r.sin_port;
}

void readLicenseData() {
	// ��ȡ֤���е���Ϣ
	return;
}

void connectClient(sockaddr_in clientAddr) {
	// ���Ӧ�Ŀͻ��˽���
	// �趨һ����ʱ��һ��ʱ��û�յ�check��ر��߳�
	MSG msg;
	while (true) {
		if (PeekMessage(&msg, nullptr, 0, 0, PM_REMOVE)) {
			if (msg.message == CK_MSG) {
				// ���ü�ʱ��
			}
			if (msg.message == WM_QUIT) {
				return;
			}
		}
	}
}

bool checkInfo(string name, string pwd, string serialNum) {
	// ȷ�ϵ�¼��Ϣ

	return true;
}

void updateLicense(updateTuple tuple) {
	// ��֤���ļ����ݽ��и���
	string status;
	if (tuple.status)
		status = "login";
	else status = "logout";
	cout << "user " << inet_ntoa(tuple.clientAddr.sin_addr) << "\t" << status << endl;
}

void handleMessage(messageData data) {
	// �������Կͻ��˵���Ϣ
	cout << inet_ntoa(data.addr.sin_addr) << "\t" << data.msg << endl;
	stringstream ss;
	ss.str(data.msg);
	string input;
	cin >> input;

	// ������Ϣָ��,login��¼,check��ʱ�㱨,quit�˳�
	if (input == "login") {
		string username, password, serialNum;
		cin >> username >> password >> serialNum;

		if (checkInfo(username, password, serialNum)) {
			// ȷ����Ϣ������ͻ��˷��������¼ָ��
			// �����µ��̹߳�����ͻ��˵����ӣ��������Ӧ�ͻ��˵���Ϣ,����¶�����Ӹ���ָ��
			myServer.sendToClient(&(data.addr), "permit");
			thread* thr = new thread(connectClient, data.addr);
			clientInfo[data.addr] = clientData(data.addr, username, password, serialNum, thr);
			updateBuf.push(updateTuple(data.addr, true));
		}
		else myServer.sendToClient(&(data.addr), "Error message, login failed");
	}
	else if (input == "check") {
		// ���ݵ�ַ�ҵ���Ӧ���̣߳������߳�ʱ��
		thread* tr = clientInfo.at(data.addr).corrThread;
		DWORD gtid = GetThreadId(tr->native_handle());
		while (!PostThreadMessage(gtid, CK_MSG, 0, 0));
	}
	else if (input == "quit") {
		// �رն�Ӧ�̣߳�����¶�����Ӹ���ָ��
		thread* tr = clientInfo.at(data.addr).corrThread;
		DWORD gtid = GetThreadId(tr->native_handle());
		while (!PostThreadMessage(gtid, WM_QUIT, 0, 0));
		clientInfo.erase(data.addr);
		updateBuf.push(updateTuple(data.addr, false));
	}
	else myServer.sendToClient(&(data.addr), "Please enter the correct instructions");
}

int main() {
	readLicenseData();
	thread recvThread(&Server::receieveFromClient, &myServer);

	while (true) {
		if (!myServer.msgBuf.empty()) {
			// �����Ϣ���в�Ϊ�գ�����ȡ��һ����Ϣ���д���
			handleMessage(myServer.msgBuf.front());
			myServer.msgBuf.pop();
		}
		if (!updateBuf.empty()) {
			// ������¶��в�Ϊ�գ��ͽ���һ�θ���
			updateLicense(updateBuf.front());
			updateBuf.pop();
		}
	}

	recvThread.join();

	return 0;
}