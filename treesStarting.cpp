#include<iostream>
using namespace std;

class Node{
    public:
int data;
struct Node *left,*right;
};

int height(Node* ptr);
void trlayer(Node* ptr,int layer);

void tralllayer(Node* ptr){
int h=height(ptr);
for(int i=1;i<=h;i++){
    trlayer(ptr,i);
}
}
void trlayer(Node* ptr,int layer){
if(ptr==NULL){
    return;
}
if(layer==1){
    cout<<ptr->data<<endl;
}
else if(layer>1){
    trlayer(ptr->left,layer-1);
    trlayer(ptr->right,layer-1);
}
}
int height(Node* ptr){
if(ptr==NULL){
    return 0;
}
int lheight=height(ptr->left);
int rheight=height(ptr->right);

if(lheight>rheight)
    return(lheight+1);
else
    return(rheight+1);
}

Node* newNode(int d1){
Node* nNode=new Node();
nNode->data=d1;
nNode->left=NULL;
nNode->right=NULL;
return(nNode);
};



int main(){

    Node* root=newNode(10);
    root->left=newNode(20);
    root->right=newNode(30);
    root->left->left=newNode(40);
    cout<<"\t\t\t"<<root->data<<endl;
    cout<<"\t"<<root->left->data<<"\t\t\t"<<root->right->data<<endl;
    cout<<root->left->left->data<<endl;
    tralllayer(root);

}
