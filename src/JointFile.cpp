#include<iostream>
using namespace std;


//读取文件1.txt到文件 n.txt，写入文件result.txt（逐个字符读取）
//第一行存帧编号
void fileJoint(int n)
{
	string fileNameTail = ".txt";
	ofstream outfile("result.txt", ios::app);
	int frameNo = 1;  //记录帧编号
	for (int i = 1;i <= n;i++)
	{
		string fileNameNo = to_string(i);
		string fileName = fileNameNo + fileNameTail;
		ifstream infile(fileName, ios::in);
		char temp;
		string no;
		infile >> noskipws;  //不跳过任意的空格和换行
		if (!infile.is_open() || !outfile.is_open())
		{
			cout << "未成功打开文件" << endl;
			exit(0);
		}
		getline(infile, no);  //no获取帧编号
		if (stoi(no) == frameNo)
		{
			frameNo++;
			while (!infile.eof())
			{
				infile >> temp;
				outfile << temp;
			}
		}
		infile.close();
		outfile << endl;
	}
	outfile.close();
	cout << "文件已写入！\n";
}
