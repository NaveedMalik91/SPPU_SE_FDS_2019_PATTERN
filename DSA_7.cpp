#include <iostream>
using namespace std;

class Node {
private:
    int data;
    Node *next;

public:
    Node() {
        this->data = 0;
        this->next = nullptr;
    }
    Node(int x) {
        this->data = x;
        this->next = nullptr;
    }
    friend class linked_list;
};

class linked_list {
    Node *head;

public:
    linked_list() {
        this->head = nullptr;
    }

    void push_back(int data) {
        Node *node1 = new Node(data);
        if (head == nullptr) {
            head = node1;
        } else {
            Node *temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = node1;
        }
    }

    void push_front(int data) {
        Node *node1 = new Node(data);
        if (head == nullptr) {
            head = node1;
        } else {
            node1->next = head;
            head = node1;
        }
    }

    Node *getStart() {
        return head;
    }

    void display_list() {
        Node *temp = head;
        while (temp->next != nullptr) {
            cout << temp->data<<" "<<endl;
            temp = temp->next;
        }
        cout << endl;
    }

    linked_list Intersection(Node *set1, Node *set2) {
        linked_list set3;
        Node *temp1 = set1;
        while (temp1 != nullptr) {
            Node *temp2 = set2;
            bool found = false;
            while (temp2 != nullptr) {
                if (temp1->data == temp2->data) {
                    found = true;
                    break;
                }
                temp2 = temp2->next;
            }
            if (found) {
                set3.push_back(temp1->data);
            }
            temp1 = temp1->next;
        }
        return set3;
    }

    linked_list Union(Node *set1, Node *set2) {
        linked_list set3;
        Node *temp1 = set1;
        Node *temp2 = set2;

        while (temp1 != nullptr) {
            set3.push_back(temp1->data);
            temp1 = temp1->next;
        }

        while (temp2 != nullptr) {
            bool present = false;
            Node *temp3 = set3.getStart();
            while (temp3 != nullptr) {
                if (temp3->data == temp2->data) {
                    present = true;
                    break;
                }
                temp3 = temp3->next;
            }
            if (!present) {
                set3.push_back(temp2->data);
            }
            temp2 = temp2->next;
        }
        return set3;
    }

    linked_list Difference(Node *set1, Node *set2) {
        linked_list set3;
        Node *temp1 = set1;

        while (temp1 != nullptr) {
            Node *temp2 = set2;
            bool found = false;

            while (temp2 != nullptr) {
                if (temp1->data == temp2->data) {
                    found = true;
                    break;
                }
                temp2 = temp2->next;
            }

            if (!found) {
                set3.push_back(temp1->data);
            }
            temp1 = temp1->next;
        }
        return set3;
    }
};

int main() {
    linked_list obj1, obj2, obj3;

    while (true) {
        cout << "1. Give input as total students and roll no of students" << endl;
        cout << "2. Students who like both vanilla and Butterscotch" << endl;
        cout << "3. Students who like either vanilla and Butterscotch" << endl;
        cout << "4. Students who like neither vanilla and Butterscotch" << endl;
        cout << "Exit" << endl;

        int choice;
        cin >> choice;

        if (choice == 1) {
            int num1;
            cout << "Enter the total number of students" << endl;
            cin >> num1;

            for (int i = 0; i < num1; i++) {
                cout << "Enter the roll no:" << endl;
                int roll_no;
                cin >> roll_no;
                obj3.push_front(roll_no); // Total students
            }
            cout << "-----------------------------------------------" << endl;

            int num2;
            cout << "Number of students who like Vanilla" << endl;
            cin >> num2;

            for (int i = 0; i < num2; i++) {
                int vanilla;
                cout << "Enter the Roll number: ";
                cin >> vanilla;
                obj1.push_front(vanilla); // Linked list1 students
            }
            cout << "-----------------------------------------------" << endl;

            int num3;
            cout << "Number of students who like Butterscotch" << endl;
            cin >> num3;

            for (int i = 0; i < num3; i++) {
                int Butterscotch;
                cout << "Enter the Roll no: ";
                cin >> Butterscotch;
                obj2.push_front(Butterscotch); // Linked list 2 students
            }
            cout << "-----------------------------------------------" << endl;
            cout << endl << endl;
        } else if (choice == 2) {
            cout << "Students who like both Vanilla and Butterscotch" << endl;
            linked_list Intersection_set = obj3.Intersection(obj1.getStart(), obj2.getStart());
            Intersection_set.display_list();
            cout << endl;
        } else if (choice == 3) {
            cout << "Students who like Either Vanilla or Butterscotch but not both" << endl;
            linked_list union_list = obj1.Union(obj1.getStart(), obj2.getStart());
            linked_list intersection_list = obj2.Intersection(obj1.getStart(), obj2.getStart());
            linked_list Either_Or = union_list.Difference(obj3.getStart(), intersection_list.getStart());
            Either_Or.display_list();
            cout << endl;
        } else if (choice == 4) {
            cout << "Students who like Neither Vanilla or Butterscotch but not both" << endl;
            linked_list union_list = obj1.Union(obj1.getStart(), obj2.getStart());
            linked_list Neither_nor = union_list.Difference(obj3.getStart(), union_list.getStart());
            Neither_nor.display_list();
            cout << endl;
        } else if (choice == 5) {
            cout << "Invalid choice!!!!" << endl;
            break;
        }
    }
    return 0;
}
