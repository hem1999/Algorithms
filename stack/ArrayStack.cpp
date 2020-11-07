#include <iostream>
using namespace std;

#define MAX 1000

class Stack{
    public:
        int a[MAX];
        int top = -1;
    public:
        Stack(){ top = -1; }

        bool push(int x){
            if(top>=MAX-1){
                cout << "Stack Overflow" << endl;
                return false;
            }
            a[++top]=x;
            cout << x << " is pushed into stack" << endl;
            return true;
        }

        int pop(){
            if(top==-1){
                cout << "Stack Underflow" << endl;
                return 0;
            }
            int x = a[top--];
            return x;
        }
        int peek(){
            if(top<0){
                cout << "Stack is Empty" << endl;
            }
            return a[top];
        }
        bool isEmpty(){
            if(top < 0){
                cout << "Stack is Empty" << endl;
                return true;
            }
            return false;
        }
            

        
        


};


int main(){
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.pop() << endl;

    return 0;
}
