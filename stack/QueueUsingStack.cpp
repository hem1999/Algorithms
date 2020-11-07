#include <iostream>
#include <bits/stdc++.h>

using namespace std;
class Queue{
    public:
        stack<int> s1,s2;
    public:
        void enQueue(int x){
            while(!s1.empty() ){
                s2.push(s1.top());
                s1.pop();
            }
            s1.push(x);   
            while(!s2.empty()){
                s1.push(s2.top());
                s2.pop();
            }
       }
       int deQueue(){
           if(s1.empty()){
               return INT_MIN;
           }
         int popped =  s1.top();
         s1.pop();
         return popped;


       }


    };


int main(){
    Queue q;
    q.enQueue(10);
    q.enQueue(20);
    q.enQueue(30);
    q.deQueue();
    return 0;
}
