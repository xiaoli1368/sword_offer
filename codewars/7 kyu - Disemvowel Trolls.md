# 7 kyu - Disemvowel Trolls


>## Detials
>
>Trolls are attacking your comment section!
>
>A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
>
>Your task is to write a function that takes a string and return a new string with all vowels removed.
>
>For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
>
>Note: for this kata `y` isn't considered a vowel.



**原址：**[7 kyu - Disemvowel Trolls](<https://www.codewars.com/kata/52fba66badcd10859f00097e>)



**说明：**

> 编写一个函数，该函数接受一个字符串并返回一个删除了所有元音的新字符串。注意，在这里'y'不是元音。



**代码：**

```python
def disemvowel(string):
    string2 = list(string)
    string3 = []
    test   = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
    for i in string2:
        if i not in test:
          string3.append(i)
    return ''.join(string3)

# 这是第1次的方式
```

```python
def disemvowel(string):
    test = 'aoeiuAOEIU'
    for i in test:
        string = string.replace(i, '')
    return string

# 这是第2种思路
# 注意：replace只是返回了新的结果，但是并不影响原始的str
#	   因此必须进行 str = str.replace() 操作

# 更为简洁的方式是：
def disemvowel(string):
    for i in 'aoeiuAOEIU':
        string = string.replace(i, '')
    return string
```



**参考答案：**

```python
def disemvowel(string):
    return string.translate(None, "aeiouAEIOU")

# 这是python2的形式，以下是python3的形式
# 其中 translator 最终是一个字典：
# {97: None, 101: None, 105: None, 111: None, 117: None, 65: None, 69: None, 73: None, 79: None, 85: None}
def disemvowel(string):
    translator = str.maketrans({key: None for key in "aeiouAEIOU"})
    return string.translate(translator)

# 以下是另外一种可行的形式
def disemvowel(string):
    return string.translate(str.maketrans('','','aeiouAEIOU'))

# 以下二者等价
# str.maketrans({key: None for key in "aeiouAEIOU"})
# str.maketrans('','','aeiouAEIOU')
```

这种方式**关键在于translate()函数的使用**，其作用看起来是等价于循环调用replace：

> Help on method_descriptor:
>
> **translate(self, table, /)**
>     Replace each character in the string using the given translation table.
>
>       table
>         Translation table, which must be a mapping of Unicode ordinals to
>         Unicode ordinals, strings, or None.
>    
>     The table must implement lookup/indexing via __getitem__, for instance a
>     dictionary or list.  If this operation raises LookupError, the character is
>     left untouched.  Characters mapped to None are deleted.

还有**maketrans()函数**的使用：

> Help on built-in function maketrans:
>
> **maketrans(x, y=None, z=None, /)**
>     Return a translation table usable for str.translate().
>
>     If there is only one argument, it must be a dictionary mapping Unicode
>     ordinals (integers) or characters to Unicode ordinals, strings or None.
>     Character keys will be then converted to ordinals.
>     If there are two arguments, they must be strings of equal length, and
>     in the resulting dictionary, each character in x will be mapped to the
>     character at the same position in y. If there is a third argument, it
>     must be a string, whose characters will be mapped to None in the result.

以下是另外一种简洁有力的方法：

```python
def disemvowel(string):
    return ''.join(c for c in string if c.lower() not in 'aeiou')

# 这种方式有一个讨论是：是否使用lower()
def disemvowel(string):
    return ''.join(c for c in string if c not in 'aeiouAEIOU')
```

这种方式也不错，关键是更加容易理解。先利用列表生成式以及大小写转换，将string中不包括元音的字符提取到一个列表中，再使用join函数进行拼接。



**以下是对不同方法的耗时分析：**

```python
import time

def disemvowel1(string):
    start_time = time.time()
    translator = str.maketrans({key: None for key in "aeiouAEIOU"})
    string = string.translate(translator)
    print('方法1用时：')
    print(time.time() - start_time)

def disemvowel2(string):
    start_time = time.time()
    string = string.translate(str.maketrans('','','aeiouAEIOU'))
    print('方法2用时：')
    print(time.time() - start_time)

def disemvowel3(string):
    start_time = time.time()
    string = ''.join(c for c in string if c not in 'aeiouAEIOU')
    print('方法3用时：')
    print(time.time() - start_time)

def disemvowel4(string):
    start_time = time.time()
    string = ''.join(c for c in string if c.lower() not in 'aeiou')
    print('方法4用时：')
    print(time.time() - start_time)

def disemvowel5(string):
    start_time = time.time()
    for i in 'aoeiuAOEIU':
        string = string.replace(i, '')
    print('方法5用时：')
    print(time.time() - start_time)

def disemvowel6(string):
    start_time = time.time()
    string2 = list(string)
    string3 = []
    test   = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
    for i in string2:
        if i not in test:
          string3.append(i)
    string = ''.join(string3)
    print('方法6用时：')
    print(time.time() - start_time)

sentence = "a"*(10**7) + "b"*(10**7) + "e"*(10**7)

disemvowel1(sentence)
disemvowel2(sentence)
disemvowel3(sentence)
disemvowel4(sentence)
disemvowel5(sentence)
disemvowel6(sentence)
```

输出结果为：

```python
方法1用时：
0.04700016975402832
方法2用时：
0.04800009727478027
方法3用时：
1.5920000076293945
方法4用时：
3.301999807357788
方法5用时：
0.26600003242492676
方法6用时：
3.515000104904175
```

可以发现：

- 用时最短的是使用 translate() 函数的方式，两种不同的调用方法相差的不是很大。
- 其次用时短的是循环调用 replace() 函数的方式，可以看到使用 str 内置的函数效果很快。
- 而其它的方法之所以会慢，是因为实现过程中**“先将字符串转换为列表，处理之后又将列表合并为字符串”**，因此应该避免这种操作，直接选择字符串函数会更快。
- 最后可以发现，使用 lower() 函数会导致结果变慢。