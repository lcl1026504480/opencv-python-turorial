/*
* @Author: lcl1026504480
* @Date:   2019-06-15 15:03:46
* @Last Modified by:   lcl1026504480
* @Last Modified time: 2019-06-15 15:54:19
*/

#include <iostream>
using namespace std;
int test()
{
    int a = 10, b = 5;
    return a+b;
}
int main()
{
    cout<<"---begin---"<<endl;
    int num = test();
    cout<<"num="<<num<<endl;
    cerr<<"---end---"<<endl;
}