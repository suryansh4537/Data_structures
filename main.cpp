#include <iostream>

using namespace std;
class Node{
public:
int data;
Node* next=NULL;
};
class LinkedList{
public:
    Node* head=NULL;
    int append(int d1){
        Node* newNode=new Node();
        newNode->data=d1;
        if(head==NULL){
            head=newNode;
            return 0;
        }
        Node* tr;
        tr=head;
        while(tr->next!=NULL){
            tr=tr->next;
        }
        tr->next=newNode;
        return 0;
    }
    int deletenode(int d1){
    Node* tr=head;
    if(tr->data==d1){
        head=tr->next;
        free(tr);
        return 0;
    }
    Node* prev;
    prev=tr;
    while(tr->data!=d1){
        prev=tr;
        tr=tr->next;

    }
    prev->next=tr->next;
    free(tr->next);

    return 0;
    }
    void reverseprint(Node* ptr){
    if(ptr!=NULL){
        reverseprint(ptr->next);
        cout<<ptr->data<<endl;
    }
    }
    void searchkey(Node* ptr,int d1,int index){
    if(ptr->data==d1){
        cout<<"key found at "<<index<<endl;
    }
    if(ptr->next==NULL){
        return;
    }
    searchkey(ptr->next,d1,index+1);

    }
    int countO(Node* ptr,int d1,int x){
        if(ptr->data==d1){
            x++;
        }
        if(ptr->next==NULL){
            return x;
        }
        countO(ptr->next,d1,x);
    }
    void printall(Node* ptr){
    cout<<ptr->data<<endl;
    if(ptr->next==NULL){
        return;
    }
    printall(ptr->next);
    }
    void mid(Node* ptr){
    Node* ptr1=ptr;
    while(ptr){
        ptr=ptr->next->next;
        ptr1->next;
    }
    cout<<ptr1->data<<endl;
    }
    void findl(Node* ptr,int len){
    if(ptr->next==NULL){
            cout<<len;
        return ;
    }
    findl(ptr->next,len+1);
    }
    /*void printall(){
    Node* tr;
    tr=head;
    while(tr){
        cout<<tr->data<<endl;
        tr=tr->next;
    }
    }*/
};

int main()
{
    LinkedList l1;
    l1.append(56);
    l1.append(78);
    l1.append(89);
    l1.append(44);
    l1.append(78);
    l1.printall(l1.head);
    cout<<l1.countO(l1.head,78,0);
    cout<<endl;
    l1.findl(l1.head,1);
    //l1.mid(l1.head);
    //l1.searchkey(l1.head,78,0);
    //l1.reverseprint(l1.head);
    //l1.deletenode(89);
    //l1.printall();
    return 0;
}
