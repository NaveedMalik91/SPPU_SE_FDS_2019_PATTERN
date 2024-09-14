// C++ program for Simple or Job Queue
#include <iostream>
#include <unistd.h>
using namespace std;
 //............Class Definition
class JobQueue
{
 int Que[5];
 int rear;
 int front;
 int size;

 public:
 //......Constructor
 JobQueue()
 {
 rear = -1;
 front = -1;
 size = 5;
 for(int i=0; i<size; i++)
 Que[i] = 0;
 }
 //......Function1
 int QueFull()
 {
 if(rear == size-1)
 return 1;
 else
 return 0;
 }
 //......Function2
 int QueEmpty()
 {
 if(rear == front)
 return 1;
 else
 return 0;
 }
 //......Function3
 void add_Job(int Val)
 {
 if(!QueFull())
 {
 rear++;
 Que[rear] = Val;
 cout<<"\n\n\t Add Job "<<Que[rear];
 }
 else
 cout<<"\n\n\t Overflow: The Queue is Full....!!!";
 }
 //......Function4
 void show_Que()
 {
 cout<<"\n Job Queue: ";
 for(int i=0; i<size; i++)
 cout<<Que[i]<<", ";
 }
 //......Function5
 void del_Job()
 {
 if(!QueEmpty())
 {
 front++;
 cout<<"\n\n\t Processing Job: "<<Que[front];
 Que[front] = 0;
 sleep(3);
 }
 else
 cout<<"\n\n\t Underflow: The Queue is Empty....!!!";
 }
};

int main()
{
 cout <<"\n .........C++ program for Simple or Job Queue.........";

 JobQueue J1;

 cout<<"\n\n Initially: ";
 J1.show_Que();

 J1.add_Job(101);
 J1.show_Que();
 J1.add_Job(102);
 J1.show_Que();
 J1.add_Job(103);
 J1.show_Que();
 J1.add_Job(104);
 J1.show_Que();
 J1.add_Job(105);
 J1.show_Que();
 J1.add_Job(106);
 J1.show_Que();

 J1.del_Job();
 J1.show_Que();
 J1.del_Job();
 J1.show_Que();
 J1.del_Job();
 J1.show_Que();
 J1.del_Job();
 J1.show_Que();
 J1.del_Job();
 J1.show_Que();
 J1.del_Job();
 J1.show_Que();

 return 0;
}