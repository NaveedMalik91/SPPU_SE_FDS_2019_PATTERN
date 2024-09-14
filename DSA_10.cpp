#include <iostream>
using namespace std;

class Stack
{
    int top;       // Top of stack
    char arr[100]; // character array to store expression

public:
    // Default Constructor
    Stack()
    {
        top = -1;
    }
    // Push onto stack
    void push(char x)
    {
        if (top == 99)
        {
            cout << ">> Stack is full." << endl;
            return;
        }
        top++;
        arr[top] = x;
    }

    // Pop from Stack
    char pop()
    {
        char x = arr[top];
        top--;
        return x;
    }
    // Check Empty stack
    bool empty()
    {
        return (top == -1);
    }
    // Get top of stack
    char TOP()
    {
        return arr[top];
    }
};

class Expression
{
    string str;

public:
    Expression(string str)
    {
        this->str = str;
    }
    // Preceedence function
    int priority(char x)
    {
        if (x == '+' || x == '-')
            return 1;
        else
            return 2;
    }

    //<----------------- Convert infix to postfix----------------------->
    string convert()
    {
        Stack obj;          // to use stack class functions
        string infix = str; // Expressio stored in infix string

        string postfix = ""; // Empty string to store postfix expression

        // Iterate over enterred expression
        for (int i = 0; i < infix.size(); i++)
        {
            // When brackets encounterred
            if (infix[i] == '(')
            {
                obj.push(infix[i]);
            }
            else if (infix[i] == ')')
            {
                while (obj.TOP() != '(')
                {
                    // pop and store untill opening bracket not found
                    postfix += obj.TOP();
                    obj.pop();
                }
                obj.pop();
            }

            // When operators Encounterred
            else if (infix[i] == '+' || infix[i] == '-' || infix[i] == '/' || infix[i] == '*')
            {
                if (obj.empty())
                {
                    obj.push(infix[i]);
                }
                else if (obj.TOP() == '(')
                {
                    obj.push(infix[i]);
                }
                // Handling Operator Preceedence
                else
                {
                    // If current operator preceedence is higher then push onto stack
                    if (priority(infix[i]) > priority(obj.TOP()))
                    {
                        obj.push(infix[i]);
                    }
                    // current operator has lower or equal preceedence then pop from stack and store in postfix
                    else
                    {
                        while (!obj.empty() && priority(infix[i]) <= priority(obj.TOP()))
                        {
                            postfix += obj.TOP(); // Append higher or equal preceedence opeartors
                            obj.pop();            // Pop operators from stack
                        }
                        obj.push(infix[i]);
                    }
                }
            }
            else
            {
                postfix += infix[i]; // Append operators directly
            }
        }
        // Process remaining operators
        while (!obj.empty())
        {
            postfix += obj.TOP(); // append to postfix string
            obj.pop();            // Pop remaining operators
        }
        // Display operators
        cout << "Postfix expression is: " << postfix << endl;
        return postfix;
    }

    //<------------------------Expression Evaluation--------------------->
    void evaluate(string postfix)
    {
        Stack obj;
        for (int i = 0; i < postfix.size(); i++)
        {
            if (postfix[i] == '+' || postfix[i] == '-' || postfix[i] == '/' || postfix[i] == '*')
            {
                // ' 0 ' -> conver digit to corresponding interger(ASCCI Value)
                int second = (obj.TOP() - '0');
                obj.pop();
                int first = (obj.TOP() - '0');
                obj.pop();
                if (postfix[i] == '-')
                {
                    int result = first - second;
                    obj.push(result + '0');
                }
                else if (postfix[i] == '+')
                {
                    int result = first + second;
                    obj.push(result + '0');
                }
                else if (postfix[i] == '/')
                {
                    int result = first / second;
                    obj.push(result + '0');
                }
                else if (postfix[i] == '*')
                {
                    int result = first * second;
                    obj.push(result + '0');
                }
            }
            else
            {
                obj.push(postfix[i]);
            }
        }
        cout << "The result of the expression is: " << (obj.TOP() - '0') << endl;
    }
};

int main()
{
    string s;
    while (true)
    {
        cout << "1. Enter expression." << endl;
        cout << "2. Convert to postfix." << endl;
        cout << "3. Evaluate" << endl;
        cout << "0. Exit" << endl;
        int choice;
        cin >> choice;
        if (choice == 1)
        {
            cout<<"Enter the expression: ";
            cin >> s;
            cout<<endl;
        }
        else if (choice == 2)
        {
            cout<<"--------------------------"<<endl;
            Expression obj(s);
            string postfix = obj.convert();
            cout<<"--------------------------"<<endl;
            cout<<endl;
        }
        else if (choice == 0)
        {
            cout << "invalid choice" << endl;
            break;
        }
        else if (choice == 1000)
        {
            cout << s << endl;
        }
        else if (choice == 3)
        {
            cout<<"----------------------------"<<endl;
            Expression obj(s);
            string postfix = obj.convert();
            obj.evaluate(postfix);
            cout<<"-----------------------------"<<endl;
            cout<<endl;
        }
        else
        {
            cout << "Invalid input." << endl;
        }
    }
    return 0;
}
