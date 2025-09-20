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