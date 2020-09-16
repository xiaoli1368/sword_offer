# 8 kyu - Remove String Spaces


>## Detials
>
>Simple, remove the spaces from the string, then return the resultant string.
>



**原址：**[8 kyu - Remove String Spaces](<https://www.codewars.com/kata/57eae20f5500ad98e50002c5>)



**说明：**

> 从字符串中删除空格，然后返回结果字符串。



**代码：**

```python
def no_space(x):
    #your code here
    y = list(x)
    z = []
    for i in y:
        if i != ' ':
            z.append(i)
    return ''.join(z)

# 这是第一次的方式
# 可见还是转换为列表，再循环处理
# 应该使用python的高级用法
```



**参考答案：**

```python
def no_space(x):
    return x.replace(' ', '')

# 这是最简洁的答案
# 在第2次刷的时候想到
```



**其它答案：**

```python
def no_space(x):
    return ''.join(x.split(' '))

# 这是另外一种方式，先使用split以空格进行切割
# 然后再使用join组合起来
```



**关键技巧：**

1. 字符串函数：replace()

   > Help on method_descriptor:
   >
   > **replace(self, old, new, count=-1, /)**
   >     Return a copy with all occurrences of substring old replaced by new.
   >
   >       count
   >         Maximum number of occurrences to replace.
   >         -1 (the default value) means replace all occurrences.
   >    
   >     If the optional argument count is given, only the first count occurrences ar
   > e
   >     replaced.

2. 字符串函数：split()

   > Help on method_descriptor:
   >
   > **split(self, /, sep=None, maxsplit=-1)**
   >     Return a list of the words in the string, using sep as the delimiter string.
   >
   >     sep
   >       The delimiter according which to split the string.
   >       None (the default value) means split according to any whitespace,
   >       and discard empty strings from the result.
   >     maxsplit
   >       Maximum number of splits to do.
   >       -1 (the default value) means no limit.

3. 字符串函数：join()

   > Help on method_descriptor:
   >
   > **join(self, iterable, /)**
   >     Concatenate any number of strings.
   >
   >     The string whose method is called is inserted in between each given string.
   >     The result is returned as a new string.
   >    
   >     Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'