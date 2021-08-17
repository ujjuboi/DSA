#include<iostream>
using namespace std;

class Node{

public: 
  string Data;
  Node* Next;
  Node(string data){
    Data = data;
    Next = NULL;
  }
};

void insertion(string data, Node* &head){
  Node* newNode = new Node(data);
  if (head==NULL){
    newNode = head;
  }
  Node* itr = head;
  while(itr->Next != NULL){
    itr = itr->Next;
  }
  itr->Next = newNode;
}

void display(Node* head){
  Node* itr = head;
  while(itr != NULL){
    cout << itr->Data << " ";
    itr = itr->Next;
  }
  cout << endl;
}

int main(){;
  Node* head = NULL;
  string data;
  bool check = true;
  cout << "Press q to exit" << endl;
  while(check){
    if (data == "q")
      break;
    cout << endl << "Enter data: ";
    cin >> data;
    insertion(data, head);
  }
  display(head);
  return 0;
}