#include<iostream>
using namespace std;
#define max 100
template<class T>
class Queue
{
    public:
    T arr[max];
    int front;
    int rear;
    Queue()
    {
        front=-1;
        rear=-1;    
    }
    void push_back(T element)
    {
        if(rear==max-1)
        {
            cout<<"Queue is full!!"<<endl;
            return;
        }
        if(front==-1) front=0;
        rear++;
        arr[rear]=element;
    }
    T pop_rear()
    {
        if(rear==-1)
        {
            cout<<"Queue is empty!!"<<endl;
        }
        else
        {
            char x=arr[rear];
            rear--;
            return x;
        }
    }
    void push_front(T value)
    {
        if(rear==max-1)
        {
            cout<<"Queue is Full!!"<<endl;
            return;
        }
        else if(front==-1)
        {
            front=0;
            rear=0;
            arr[front]=value;
        }
        else
        {
            rear++;
            for(int i=rear;i>front;i--)
            {
                arr[i]=arr[i-1];
            }
            arr[front]=value;
        }
    }
    T pop_front()
    {
        if(rear==-1)
        {
            cout<<"Queue is empty"<<endl;
        }
        else
        {
            char x=arr[front];
            rear--;
            for(int i=front;i<=rear;i++)
            {
                arr[i]=arr[i+1];
            }
            return x;
        }
    }
    void display()
    {
        if(rear==-1)
        {
            cout<<"Queue is empty!!"<<endl;
        }
        else
        {
            for(int i=front;i<=rear;i++)
            {
                cout<<arr[i]<<" ";
            }
            cout<<endl;
        }
    }
    bool isempty()
    {
        if((front=rear+1) || front==-1 || rear==-1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
int main()
{
    Queue<int> obj;
    while(true)
    {
        cout<<"---------MENU---------"<<endl;
        cout<<"1.Insert at front"<<endl;
        cout<<"2.Insert at rear"<<endl;
        cout<<"3.Delete from front"<<endl;
        cout<<"4.Delete from rear"<<endl;
        cout<<"5.Exit"<<endl;
        cout<<"----------------------"<<endl;
        int choice;
        cout<<"Enter your choice : ";
        cin>>choice;
        if(choice==1)
        {
            int value;
            cout<<"Enter the value to insert : ";
            cin>>value;
            obj.push_front(value);
            obj.display();
        }
        else if(choice==2)
        {
            int value;
            cout<<"Enter the value to insert : ";
            cin>>value;
            obj.push_back(value);
            obj.display();
        }
        else if(choice==3)
        {
            obj.pop_front();
            obj.display();
        }
        else if(choice==4)
        {
            obj.pop_rear();
            obj.display();
        }
        else if(choice==5)
        {
            break;
        }
    }
    
    return 0;
}