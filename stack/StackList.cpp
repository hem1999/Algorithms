#include <bits/stdc++.h>
using namespace std;

class StackNode{
    public:
        int data;
        StackNode* next;
    public:
        StackNode(int d){
            data = d;
            next = NULL;
        }
            
};

StackNode* newNode(int data){
    StackNode* stackNode = new StackNode( data);
    return stackNode;
}
int isEmpty(StackNode* root){

    return !root;
}
void push(StackNode** root, int data){
    StackNode* stackNode = new StackNode(data);
    stackNode->next = *root;
    *root = stackNode;
}
int pop(StackNode** root){
    if(isEmpty(*root)){
        return INT_MIN;
    }
    StackNode* temp = *root;
    *root = (*root)->next;
    int popped = temp->data;
    free(temp);
    return popped;}
    
int peek(StackNode* root){
    if(isEmpty(root)){
        cout << "Stack is Empty" << endl;
        return INT_MIN;
    }
    return root->data;
}
int main(){
    StackNode* root = NULL;
    push(&root,10);
    push(&root,20);
    push(&root,30);
    cout << pop(&root) << "popped from stack" << endl;
    cout << "Peek: "<< peek(root) << endl;
    
    return 0;
}


