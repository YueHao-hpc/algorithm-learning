#include <iostream>
#include <cstring>
using namespace std;
// 最后一个节点的地址域为空
// 链表的优势在于 不需要利用连续的内存空间 每个节点存储数据域和地址域
/*
struct Node{
int data;
Node *next;
}
*/
// 单链表的地址域是存储的下一个节点的地址 即每个节点只能向后遍历，不能向前遍历
// 双向链表的地址域存储了前后各自的地址
#if 0
struct Node
{
    Node(int data = 0) : data_(data), next_(nullptr) {};
    int data_;
    Node *next_;
};
class Clink
{
public:
    Clink()
    {
        head_ = new Node(); // 给head_初始化指向头节点
    }
    ~Clink()
    {
        // 节点的释放
    }
    void InserTail(int val) // 插入链表尾部
    {
        Node *p = head_;
        while (p->next_ != nullptr)
        {
            p = p->next_;
        }

        // 先找到当前链表的末尾节点
        // 生成新节点
        Node *node = new Node(val);
        p->next_ = node;
    }

private:
    Node *head_; // 指向链表的头节点
};
#endif
// 双向链表节点
struct DNode {
    int val;
    DNode* prev;
    DNode* next;
    DNode(int x) : val(x), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList {
public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}

    ~DoublyLinkedList() {
        DNode* cur = head;
        while (cur) {
            DNode* temp = cur;
            cur = cur->next;
            delete temp;
        }
    }

    // 头插
    void push_front(int val) {
        DNode* node = new DNode(val);
        if (!head) { // 空链表
            head = tail = node;
        } else {
            node->next = head;
            head->prev = node;
            head = node;
        }
    }

    // 尾插
    void push_back(int val) {
        DNode* node = new DNode(val);
        if (!tail) { // 空链表
            head = tail = node;
        } else {
            tail->next = node;
            node->prev = tail;
            tail = node;
        }
    }

    // 删除第一次出现的值
    void erase(int val) {
        DNode* cur = head;
        while (cur) {
            if (cur->val == val) {
                if (cur->prev) cur->prev->next = cur->next;
                else head = cur->next;  // 删除头节点

                if (cur->next) cur->next->prev = cur->prev;
                else tail = cur->prev;  // 删除尾节点

                delete cur;
                return;
            }
            cur = cur->next;
        }
    }

    // 从头到尾打印
    void print_forward() {
        DNode* cur = head;
        while (cur) {
            cout << cur->val << " ";
            cur = cur->next;
        }
        cout << endl;
    }

    // 从尾到头打印
    void print_backward() {
        DNode* cur = tail;
        while (cur) {
            cout << cur->val << " ";
            cur = cur->prev;
        }
        cout << endl;
    }

private:
    DNode* head;
    DNode* tail;
};

int main() {
    DoublyLinkedList dll;

    dll.push_back(1);
    dll.push_back(2);
    dll.push_back(3);
    dll.print_forward();    // 1 2 3
    dll.print_backward();   // 3 2 1

    dll.push_front(0);
    dll.print_forward();    // 0 1 2 3

    dll.erase(2);
    dll.print_forward();    // 0 1 3
    dll.print_backward();   // 3 1 0

    return 0;
}