#include <iostream>
#include <cstring>
using namespace std;

class Array
{
private:
    int *mpArr;           // 指向可扩容的数组内存
    int mCap;             // 数组容量
    int mCur;             // 数组有效元素个数
    void expand(int size) // 内部数组扩容接口 -- 如果扩容成两倍，那你就需要先开辟一块两倍容量的内存，然后把值拷贝进去，再把旧的数组内存释放掉
    {
        int *p = new int[size];
        memcpy(p, mpArr, sizeof(int) * mCur); // memcpy的用法：目标内存地址，原始地址，要拷贝的“字节数”
        delete[] mpArr;
        mpArr = p;
        mCap = size;
    }

public:
    Array(int size = 10) : mCur(0), mCap(size) // 这里用到的是初始化列表
    {
        mpArr = new int[mCap]();
    }
    ~Array()
    {
        delete[] mpArr;  // 释放堆上的那个数组
        mpArr = nullptr; // 释放指向堆上数组的指针 否则这个指针就变成了野指针
    };

    void push_back(int val) // 末尾添加元素
    {
        if (mCur == mCap) // 数组满了就进行扩容
        {
            expand(2 * mCap);
        }
        mpArr[mCur++] = val; // 然后添加数据
    }

    void pop_back() // 末尾删除元素
    {
        if (mCur == 0)
        { // 数组为空就什么都不做
            return;
        }
        mCur--;
    };
    void insert(int pos, int val) // 按位置增加元素
    {
        if (pos < 0 || pos > mCur) // 先要对参数合法性进行检查
        {
            return;
        }
        if (mCur == mCap)
        {
            expand(2 * mCap);
        }
        for (int i = mCur - 1; i >= pos; i--)
        {
            mpArr[i + 1] = mpArr[i];
        }
        mpArr[pos] = val;
        mCur += 1;
    };
    void erase(int pos) // 按位置删除
    {
        if (pos < 0 || pos > mCur)
        {
            return;
        }
        for (int i = pos; i < mCur - 1; i++)
        {
            mpArr[i] = mpArr[i + 1];
        }
        mCur--;
    };
    int find(int val) // 元素查询
    {
        for (int i = 0; i < mCur; i++)
        {
            if (mpArr[i] == val)
            {
                return i;
            }
        };
        return -1;
    }
    void show() const
    {
        for (int i = 0; i < mCur; i++)
        {
            cout << mpArr[i] << " ";
        }
        cout << endl;
    }
};

int main()
{
    Array arr;
    srand(time(0));
    for (int i = 0; i < 10; i++)
    {
        arr.push_back(rand() % 100);
    }
    arr.show();
    arr.pop_back();
    arr.show();
    arr.push_back(15);
    arr.insert()
}