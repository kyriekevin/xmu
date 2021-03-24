#include<fstream>
#include <iostream>
using namespace std;
double aa[42][42];
int a[42][42];
int version=0,z,sum;//z起始位,sum总和
char c='\0'; 
bool solve1()//处理版本信息
{
    int num1=0,num2=0,num3=0;z=256;
    for(int i=34;i<=36;i++)
    {
        for(int j=39;j<=41;j++,z=z/2)
        {
            if(a[i][j]) num1+=z;
        }
    }
    z=256;
    for(int i=39;i<=41;i++)
    {
        for(int j=34;j<=36;j++,z=z/2)
        {
            if(a[i][j]) num2+=z;
        }
    }
    z=256;
    for(int i=39;i<=41;i++)
    {
        for(int j=39;j<=41;j++,z=z/2)
        {
            if(a[i][j]) num3+=z;
        }
    }
    if(num1==num2&&num2==num3) 
    {
        version=num1;return true;
    }
    return false;
}
void solve2_1(int x,int y,std::fstream&out,std::fstream&vout)//4*5小块
{
    if(((1^a[x][y]^a[x][y+1]^a[x][y+2]^a[x][y+3])==a[x][y+4])&&((1^a[x+1][y]^a[x+1][y+1]^a[x+1][y+2]^a[x+1][y+3])==a[x+1][y+4]))
    {
        z=128,sum=0;
        for(int i=0;i<=1;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<1;out<<c;
    }
    else 
    {
        z=128,sum=0;
        for(int i=0;i<=1;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<0;out<<c;
    }
}
void solve2(std::fstream&out,std::fstream&vout)//处理正上信息
{
    for(int i=1;i<=5;i=i+4)
    {
        for(int j=9;j<=29;j=j+5)
        {
            solve2_1(i,j,out,vout);
            solve2_1(i+2,j,out,vout);
        }
    }
}
void solve3_1(int x,int y,std::fstream&out,std::fstream&vout)//4*5小块
{
    if(((1^a[x][y]^a[x+1][y]^a[x+2][y]^a[x+3][y])==a[x+4][y])&&((1^a[x][y+1]^a[x+1][y+1]^a[x+2][y+1]^a[x+3][y+1])==a[x+4][y+1])&&((1^a[x][y+2]^a[x+1][y+2]^a[x+2][y+2]^a[x+3][y+2])==a[x+4][y+2])&&((1^a[x][y+3]^a[x+1][y+3]^a[x+2][y+3]^a[x+3][y+3])==a[x+4][y+3]))
    {
        z=128,sum=0;
        for(int i=0;i<=1;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<1;out<<c;
        z=128,sum=0;
        for(int i=2;i<=3;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<1;out<<c;
    }
    else 
    {
        z=128,sum=0;
        for(int i=0;i<=1;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<1;out<<c;
        z=128,sum=0;
        for(int i=2;i<=3;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<0;out<<c;
    }
}
void solve3(std::fstream&out,std::fstream&vout)//处理正左信息
{
    for(int i=9;i<=29;i=i+5)
    {
        for(int j=1;j<=5;j=j+4)
        {
            solve3_1(i,j,out,vout);
        }
    }
}
void solve4_1(int x,int y,std::fstream&out,std::fstream&vout)//4*5小块
{
    if(((1^a[x][y]^a[x][y+1]^a[x][y+2]^a[x][y+3])==a[x][y+4])&&((1^a[x+1][y]^a[x+1][y+1]^a[x+1][y+2]^a[x+1][y+3])==a[x+1][y+4])&&((1^a[x][y]^a[x+1][y]^a[x+2][y]^a[x+3][y])==a[x+4][y])&&((1^a[x][y+1]^a[x+1][y+1]^a[x+2][y+1]^a[x+3][y+1])==a[x+4][y+1])&&((1^a[x][y+2]^a[x+1][y+2]^a[x+2][y+2]^a[x+3][y+2])==a[x+4][y+2])&&((1^a[x][y+3]^a[x+1][y+3]^a[x+2][y+3]^a[x+3][y+3])==a[x+4][y+3]))
    {
        z=128,sum=0;
        for(int i=0;i<=1;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<1;out<<c;
        z=128,sum=0;
        for(int i=2;i<=3;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<1;out<<c;
    }
    else 
    {
        z=128,sum=0;
        for(int i=0;i<=1;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<1;out<<c;
        z=128,sum=0;
        for(int i=2;i<=3;i++)
        {
            for(int j=0;j<=3;j++,z=z/2)
            {
                if(a[x+i][y+j]) sum+=z;
            }
        }
        c=sum;vout<<0;out<<c;
    }
}
void solve4(std::fstream&out,std::fstream&vout)//处理正中信息
{
    for(int i=9;i<=29;i=i+5)
    {
        for(int j=9;j<=29;j=j+5)
        {
            solve4_1(i,j,out,vout);
        }
    }
}
void solve5(std::fstream&out,std::fstream&vout)//处理正右信息
{
    for(int i=9;i<=29;i=i+5)
    {
        for(int j=34;j<=38;j=j+4)
        {
            solve3_1(i,j,out,vout);
        }
    }
}
void solve6(std::fstream&out,std::fstream&vout)//处理正下信息
{
    for(int i=34;i<=38;i=i+4)
    {
        for(int j=9;j<=29;j=j+5)
        {
            solve2_1(i,j,out,vout);
            solve2_1(i+2,j,out,vout);
        }
    }
}
int main()
{
    fstream in,out,vout;
    in.open("C:\\Users\\Lenovo1\\Desktop\\001.txt",ios::in);
    out.open("C:\\Users\\Lenovo1\\Desktop\\out.bin",ios::out);
    vout.open("C:\\Users\\Lenovo1\\Desktop\\vout.bin",ios::out);
	for(int i=1;i<=41;i++)
    {
        for(int j=1;j<=41;j++)
		{
            in>>aa[i][j];a[i][j]=(int)aa[i][j];
        }
    }
	if(solve1())//处理版本信息
    {
        solve2(out,vout);//处理正上信息
        solve3(out,vout);//处理正左信息
        solve4(out,vout);//处理正中信息
        solve5(out,vout);//处理正右信息
        solve6(out,vout);//处理正下信息
    }
    else 
    {
        for(int i=1;i<=130;i++)
        {
            out<<0;vout<<0;
        }
    }
	in.close();
	out.close();
    vout.close();
    system("pause");
    return 0;
}
