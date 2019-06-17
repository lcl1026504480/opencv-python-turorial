/*
* @Author: lcl1026504480
* @Date:   2019-06-14 21:39:26
* @Last Modified by:   lcl1026504480
* @Last Modified time: 2019-06-15 12:51:02
*/
#include <iostream>
using namespace std;

class TestLib
{
    public:
        void display();
        void display(int a);
};
void TestLib::display() {
    cout<<"First display"<<endl;
}

void TestLib::display(int a) {
    cout<<"Second display:"<<a<<endl;
}
extern "C" {
    TestLib obj;
    void display() {
        obj.display();
      }
    void display_int() {
        obj.display(2);
      }
}