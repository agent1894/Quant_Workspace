#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
    cout << "Hello World" << endl;
    cout << fixed; // 避免科学记数法
    cout << setprecision(2); // 设置精度
    double number;
    number = 10.0/3*100000;
    /*
    * VS Code下Code Runner编译运行会出现中文乱码
    * CMD运行可正常显示
    */
    cout << "保留两位小数数值为：" << number << endl; 
    return 0;
} 
