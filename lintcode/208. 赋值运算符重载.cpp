/*
 * 208. 赋值运算符重载
 * 
 * 思路：
 * 难点在于需要考虑好多种情况
 */

class Solution {
public:
    /*
    1、判断是否自己给自己赋值
    2、判断是否是NULL
    3、自己开辟字符串内存，注意字符串\0结尾，要多开辟一个
    */
    char *m_pData;
    Solution() {
        this->m_pData = NULL;
    }
    Solution(char *pData) {
        this->m_pData = pData;
    }

    // Implement an assignment operator
    Solution operator=(const Solution &object) {
        // write your code here
        // 如果给自己给自己赋值
        if (&object == this) {
            return *this;
        }
        // 删除自己的数据
        if (m_pData) {
            delete [] m_pData;
        }
        // 如果B内部没有数据
        if (object.m_pData == NULL) {
            return *this;
        }
        // 先统计B中数据长度
        int size = 0;
        char* ptr = object.m_pData;
        while (*ptr != '\0') {
            size += 1;
            ptr += 1;
        }
        // 申请内存并且拷贝
        m_pData = new char[size + 1];
        memcpy(m_pData, object.m_pData, size + 1);
        return *this;
    }
};