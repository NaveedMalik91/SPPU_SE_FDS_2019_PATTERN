#include <iostream>
#include <string>
using namespace std;

class Stack
{
private:
    static const int MAX_SIZE = 100; // Define maximum size of the stack
    char arr[MAX_SIZE];
    int top;

public:
    Stack()
    {
        top = -1; // Initialize top to -1 (empty stack)
    }

    void push(char bracket)
    {
        if (top >= MAX_SIZE - 1)
        {
            cout << "Stack Overflow\n";
            return;
        }
        arr[++top] = bracket; // increment and assign top with new value
    }

    void pop()
    {
        if (isEmpty())
        {
            cout << "Stack Underflow\n";
            return;
        }
        --top; // decrement top while popping
    }

    char Top()
    {
        if (isEmpty())
        {
            cout << "Stack is empty\n";
            return '\0'; // Return null character in case of an empty stack
        }
        return arr[top];
    }

    bool isEmpty()
    {
        return (top == -1);
    }
};

bool isWellParenthesized(const string &expression)
{
    Stack bracketStack; // Using Stack class instead of std::stack
    for (char temp : expression)
    {
        if (temp == '(' || temp == '{' || temp == '[')
        {
            bracketStack.push(temp);
        }
        else if (temp == ')' || temp == '}' || temp == ']')
        {
            if (bracketStack.isEmpty())
            {
                return false;
            }
            else if ((temp == ')' && bracketStack.Top() != '(') ||
                     (temp == '}' && bracketStack.Top() != '{') ||
                     (temp == ']' && bracketStack.Top() != '['))
            {
                return false;
            }
            else
            {
                bracketStack.pop();
            }
        }
    }
    return bracketStack.isEmpty();
}

int main()
{
    int choice;
    string expression;
    while (true)
    {
        cout << "<-----------------Menu----------------->" << endl;
        cout << " 1. Enter an Expression:" << endl;
        cout << " 2. Check if an expression is well parenthesized" << endl;
        cout << " 3. Exit" << endl;
        cout << "Enter your choice: " << endl;

        cin >> choice;
        cin.ignore();

        if (choice == 1)
        {
            cout << "Enter an Expression" << endl;
            getline(cin, expression);
        }
        else if (choice == 2)
        {
            if (expression.empty())
            {
                cout << "Expression is empty, Enter an expression first" << endl;
            }
            else
            {
                if (isWellParenthesized(expression))
                {
                    cout << "The Entered expression is well parenthesized" << endl;
                }
                else
                {
                    cout << "The Enterred Expression not parenthesized" << endl;
                }
            }
        }
        else
        {
            cout << "You entered a wrong choice" << endl;
            break;
        }
    }
    return 0;
}
