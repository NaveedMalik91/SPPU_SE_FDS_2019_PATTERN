#include <iostream>
using namespace std;

class Node
{
private:
    int data;
    Node *next;
    Node *previous;

public:
    Node(int x)
    {
        this->data = x;
        this->next = NULL;
        this->previous = NULL;
    }
    friend class Doubly_LL;
};

class Doubly_LL
{
private:
    Node *head;
    Node *tail;

public:
    Doubly_LL()
    {
        this->head = NULL;
        this->tail = NULL;
    }

    //<-----------------Insertion function------------------>
    void insert_End(int data)
    {
        Node *node1 = new Node(data);
        if (head == NULL)
        {
            head = tail = node1;
        }
        else
        {
            node1->previous = tail;
            tail->next = node1;
            tail = node1;
        }
    }

    //<--------------------Display--------------------------->
    void display_list()
    {
        Node *temp = head;
        while (temp != NULL)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    //<------------------------One's Complement--------------->
    void ones_complement()
    {
        Node *temp = head;
        while (temp != NULL)
        {
            temp->data = temp->data ^ 1; // Computing 1's complement
            temp = temp->next;
        }
    }

    //<-------------------------Two's Complement---------------->
    void twosComplement()
    {
        ones_complement(); // Get 1's complement first

        Node *temp = tail;
        bool carry = true;

        while (temp != NULL && carry)
        {
            temp->data += 1; // Adding 1 to the least significant bit (2's complement)
            if (temp->data > 1)
            {
                temp->data = 0;
            }
            else
            {
                carry = false;
            }
            temp = temp->previous;
        }

        if (carry)
        {
            insert_End(1); // If carry is still true, add an additional 1 to the MSB
        }
    }

    //<----------------------Convert to Binary------------------->
    void Convert_binary(int number)
    {
        while (number > 0)
        {
            insert_End(number % 2); // Storing binary digits in the list
            number /= 2;
        }
    }

    //<---------------------Add Binary--------------------------->
    void Add_Binary(Doubly_LL list1, Doubly_LL list2)
    {
        Node *temp1 = list1.head;
        Node *temp2 = list2.head;
        int carry = 0;

        while (temp1 != NULL || temp2 != NULL || carry)
        {
            int sum = carry;
            if (temp1 != NULL)
            {
                sum += temp1->data;
            }

            if (temp2 != NULL)
            {
                sum += temp2->data;
            }

            insert_End(sum % 2);
            carry = sum / 2;

            if (temp1)
            {
                temp1 = temp1->next;
            }
            if (temp2)
            {
                temp2 = temp2->next;
            }
        }
    }
};
//----------Main function--------------
int main()
{
    Doubly_LL binaryList;

    while (true)
    {
        cout << "1. Enter decimal number." << endl;
        cout << "2. 1's compliment" << endl;
        cout << "3. 2's compliment" << endl;
        cout << "4. Add two binary numbers." << endl;
        cout << "5. Exit" << endl;
        int choice;
        cin >> choice;
        
        if (choice == 1)
        {
            cout<<"---------------------"<<endl;
            int number;
            cout << "Enter number: ";
            cin >> number;
            binaryList.Convert_binary(number);
            cout << "Binary Representation: ";
            binaryList.display_list();
            cout << "Decimal number converted to binary." << endl;
            cout<<"---------------------"<<endl;
            cout<<endl<<endl;
        } 

        else if (choice == 2)
        {
            binaryList.ones_complement();
            cout << "1's Complement: ";
            binaryList.display_list();
            cout<<endl<<endl;
        }

        else if (choice == 3)
        {
            binaryList.twosComplement();
            cout << "2's Complement: ";
            binaryList.display_list();
            cout<<endl<<endl;
        }

        else if (choice == 4)
        {
            cout<<"-----------------------"<<endl;
            Doubly_LL binaryList1, binaryList2;
            cout << "Enter first binary number: ";
            int num1;
            cin >> num1;
            binaryList1.Convert_binary(num1);

            cout << "Enter second binary number: ";
            int num2;
            cin >> num2;
            binaryList2.Convert_binary(num2);

            Doubly_LL result;
            result.Add_Binary(binaryList1, binaryList2);

            cout << "Result of addition: ";
            result.display_list();
            cout<<"-----------------------"<<endl;
            cout<<endl<<endl;
        }
        
        else if (choice == 5)
        {
            cout << "Invalid choice! Please try again." << endl;
            break;
        }
    }


    return 0;
}