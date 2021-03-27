
#include<iostream>
using namespace std;

//读取文件1.txt到文件 n.txt，写入文件result.txt（逐个字符读取）
//第一行存帧编号
void fileTest1(int n)
{
	string b = ".txt";
	ofstream outfile("result.txt", ios::app);
	int frame = 1;  //记录帧编号
	for (int i = 1;i <= n;i++)
	{
		string a = to_string(i);
		string c = a + b;
		ifstream myfile(c, ios::in);
		char temp;
		string no;
		myfile >> noskipws;  //不跳过任意的空格和换行
		if (!myfile.is_open() || !outfile.is_open())
		{
			cout << "未成功打开文件" << endl;
			exit(0);
		}
		getline(myfile, no);
		if (stoi(no) == frame)
		{
			frame++;
			while (!myfile.eof())
			{
				myfile >> temp;
				outfile << temp;
			}
		}
		myfile.close();
		outfile << endl;
	}
	outfile.close();
	cout << "文件已写入！\n";
}


