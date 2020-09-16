# Codewars题解笔记

作者：xiaoli1368
日期：2020/09/16
邮箱：xiaoli1644@qq.com

## 目录

[TOC]

## 8 kyu - Remove String Spaces


>## Detials
>
>Simple, remove the spaces from the string, then return the resultant string.

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
   >  Return a copy with all occurrences of substring old replaced by new.
   >
   >    count
   >      Maximum number of occurrences to replace.
   >      -1 (the default value) means replace all occurrences.
   >
   >  If the optional argument count is given, only the first count occurrences ar
   > e
   >  replaced.

2. 字符串函数：split()

   > Help on method_descriptor:
   >
   > **split(self, /, sep=None, maxsplit=-1)**
   >  Return a list of the words in the string, using sep as the delimiter string.
   >
   >  sep
   >    The delimiter according which to split the string.
   >    None (the default value) means split according to any whitespace,
   >    and discard empty strings from the result.
   >  maxsplit
   >    Maximum number of splits to do.
   >    -1 (the default value) means no limit.

3. 字符串函数：join()

   > Help on method_descriptor:
   >
   > **join(self, iterable, /)**
   >  Concatenate any number of strings.
   >
   >  The string whose method is called is inserted in between each given string.
   >  The result is returned as a new string.
   >
   >  Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

## 8 kyu - Multiply

**原址：**[8 kyu - Multiply](<https://www.codewars.com/kata/50654ddff44f800200000004>)

**说明：**

> 实现两数相乘

**代码：**

```python
def multiply(a, b):
	return a * b
```

**其它答案：**

```python
def multiply(x, y): return x * y
```

```python
multipy = lambda x, y: x * y
```

```python
def multiply(x, y):
    a *= b
    return a

'''这种方式并不好， 因为a的值会被修改
'''
```

## 7 kyu - Disemvowel Trolls


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
>  Replace each character in the string using the given translation table.
>
>    table
>      Translation table, which must be a mapping of Unicode ordinals to
>      Unicode ordinals, strings, or None.
>
>  The table must implement lookup/indexing via __getitem__, for instance a
>  dictionary or list.  If this operation raises LookupError, the character is
>  left untouched.  Characters mapped to None are deleted.

还有**maketrans()函数**的使用：

> Help on built-in function maketrans:
>
> **maketrans(x, y=None, z=None, /)**
>  Return a translation table usable for str.translate().
>
>  If there is only one argument, it must be a dictionary mapping Unicode
>  ordinals (integers) or characters to Unicode ordinals, strings or None.
>  Character keys will be then converted to ordinals.
>  If there are two arguments, they must be strings of equal length, and
>  in the resulting dictionary, each character in x will be mapped to the
>  character at the same position in y. If there is a third argument, it
>  must be a string, whose characters will be mapped to None in the result.

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

## 7 kyu - Descending Order


>## Detials
>
>Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
>
>### Examples:
>
>Input: `21445` Output: `54421`
>
>Input: `145263` Output: `654321`
>
>Input: `1254859723` Output: `9875543221`

**原址：**[7 kyu - Descending Order](<https://www.codewars.com/kata/5467e4d82edf8bbf40000155>)

**说明：**

> 你的任务是创建一个函数，该函数可以将任何非负整数作为参数，并以其降序返回数字。 基本上，重新排列数字以创建尽可能高的数字。

**代码：**

```python
def Descending_Order(num):
    #Bust a move right here  
    return int(''.join(sorted(list(str(num)), reverse=True)))
```

## 7 kyu - Deodorant Evaporator


>## Detials
>
>This program tests the life of an evaporator containing a gas.
>
>We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day) and the threshold (threshold) in percentage beyond which the evaporator is no longer useful. All numbers are strictly positive.
>
>The program reports the nth day (as an integer) on which the evaporator will be out of use.
>
>**Note** : Content is in fact not necessary in the body of the function "evaporator", you can use it or not use it, as you wish. Some people might prefer to reason with content, some other with percentages only. It's up to you but you must keep it as a parameter because the tests have it as an argument.

**原址：**[7 kyu - Deodorant Evaporator](<https://www.codewars.com/kata/5506b230a11c0aeab3000c1f>)

**说明：**

> 该程序测试含有气体的蒸发器的寿命。
>
> 我们知道蒸发器的含量（以ml计的含量），每天损失的泡沫或气体的百分比（evap_per_day）和阈值（阈值），以百分比超过蒸发器不再有用。 所有数字都是严格正数。
>
> 该程序报告蒸发器将不使用的第n天（整数）。

**代码：**

```python
def evaporator(content, evap_per_day, threshold):
    day_spend = 0
    remain = 100
    while remain > threshold:
        day_spend += 1
        remain *= (1 - evap_per_day / 100)
    return day_spend
```

## 7 kyu - Complementary DNA


>## Detials
>
>Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
>
>If you want to know more <http://en.wikipedia.org/wiki/DNA>
>
>In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
>
>More similar exercise are found here <http://rosalind.info/problems/list-view/> (source)
>
>```python
>DNA_strand ("ATTGC") # return "TAACG"
>
>DNA_strand ("GTAT") # return "CATA"
>```

**原址：**[7 kyu - Complementary DNA](<https://www.codewars.com/kata/5506b230a11c0aeab3000c1f>)

**说明：**

> 实现对于输入DNA的碱基配对

**代码：**

```python
def DNA_strand(dna):
    # code here
    result = []
    if(dna): # if not empty
        for i in range(len(dna)):
            if(dna[i] == 'A'):
                result.append('T')
            elif(dna[i] == 'T'):
                result.append('A')
            elif(dna[i] == 'G'):
                result.append('C')
            elif(dna[i] == 'C'):
                result.append('G')
        return ''.join(result)
    else:
        return result
```

## 7 kyu - Binary Addition


>## Detials
>
>Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
>
>The binary number returned should be a string.

**原址：**[7 kyu - Binary Addition](<https://www.codewars.com/kata/551f37452ff852b7bd000139>)

**说明：**

> 实现一个将两个数字相加并以二进制形式返回其总和的函数。 转换可以在添加之前或之后完成。返回的二进制数应为字符串。


**代码：**

```python
def add_binary(a,b):
    #your code here
    c      = a + b
    result = []
    shang  = 1
    yushu  = 1
    while(shang != 0):
        shang = c // 2
        yushu = c % 2
        result.append(str(yushu))
        c     = shang
    return ''.join(result[::-1])
```

## 6 kyu - Roman Numerals Encoder


>## Detials
>
>Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
>
>Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
>
>Example:
>
>```python
>solution(1000) # should return 'M'
>```

**原址：**[6 kyu - Roman Numerals Encoder](https://www.codewars.com/kata/51b62bf6a9c58071c600001b)

**说明：**

> 创建一个以正整数作为参数并返回包含该整数的罗马数字表示的字符串的函数。
>
> 现代罗马数字是通过从最左边的数字开始分别表示每个数字并跳过值为零的任何数字来编写的。 在罗马数字中，呈现1990：1000 = M，900 = CM，90 = XC; 导致MCMXC。 2008年写成2000 = MM，8 = VIII; 或MMVIII。 1666按降序使用每个罗马符号：MDCLXVI。

**代码：**

```python
def solution(n):
    # TODO convert int to roman string
    result = []
    string = list(str(n))
    length = len(string)
    ref = [['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
           ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
           ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
           ['M', 'MM', 'MMM', 'MM', 'M', 'MM', 'MMM', 'MMMM', 'MM']
        ]
    for i in range(length):
        if string[i] == '0':
            continue
        else:
            result.append(ref[length - 1 - i][int(string[i]) - 1])      
    return ''.join(result)
```

## 6 kyu - Replace With Alphabet Position


>## Detials
>
>Welcome.
>
>In this kata you are required to, given a string, replace every letter with its position in the alphabet.
>
>If anything in the text isn't a letter, ignore it and don't return it.
>
>`"a" = 1`, `"b" = 2`, etc.
>
>## Example
>
>```python
>alphabet_position("The sunset sets at twelve o' clock.")
>```
>
>Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` (as a string)

**原址：**[6 kyu - Replace With Alphabet Position](https://www.codewars.com/kata/546f922b54af40e1e90001da)

**说明：**

> 在这个kata中，你需要给一个字符串，用字母表中的位置替换每个字母。如果文本中的任何内容不是字母，请忽略它并且不返回它。

**代码：**

```python
def alphabet_position(text):
    result = []
    for i in range(len(text)):
        ascii = ord(text[i])
        if(ascii >= 65 and ascii <= 90):
            result.append(str(ascii - 64))           
        elif(ascii >= 97 and ascii <= 122):
            result.append(str(ascii - 96))
    if(result): # if not empty
        return ' '.join(result)
    else:
        return ''
    pass
```

## 6 kyu - Give me a Diamond


>## Detials
>
>Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.
>
>## Task
>
>You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (`*`) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (`\n`).
>
>Return `null/nil/None/...` if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
>
>## Examples
>
>A size 3 diamond:
>
>```
>*
>***
>*
>```
>
>...which would appear as a string of `" *\n***\n *\n"`
>
>A size 5 diamond:
>
>```
>*
>***
>*****
>***
>*
>```
>
>...that is: `" *\n ***\n*****\n ***\n *\n"`

**原址：**[6 kyu - Give me a Diamond](<https://www.codewars.com/kata/5503013e34137eeeaa001648>)

**说明：**

> 您需要使用星号（`*`）字符返回在屏幕上打印时看起来像钻石形状的字符串。 应删除尾随空格，并且每行必须以换行符（`\ n`）终止。

**代码：**

```python
def diamond(n):
    # Make some diamonds!
    result = []
    if (n < 0 or n % 2 == 0):
        return None
    else:
        for i in range(1, n + 1):
            y = (n + 1) // 2     # 中间的行
            x = (y - abs(y -i))  # i的等价的行
            result.append(' ' * (y - x) + '*' * (x * 2 -1) + '\n')
        return ''.join(result)
```

## 6 kyu - CamelCase Method


>## Detials
>
>Write simple .camelCase method (`camel_case` function in PHP, `CamelCase` in C# or `camelCase` in Java) for strings. All words must have their first letter capitalized without spaces.
>
>For instance:
>
>```python
>camelcase("hello case") => HelloCase
>camelcase("camel case word") => CamelCaseWord
>```
>
>Don't forget to rate this kata! Thanks :)

**原址：**[6 kyu - CamelCase Method](<https://www.codewars.com/kata/587731fda577b3d1b0001196>)

**说明：**

> 编写简单的.camelCase方法（PHP中的`camel_case`函数，C＃中的`CamelCase`或Java中的`camelCase`）。 所有单词的首字母必须没有空格。

**代码：**

```python
def camel_case(string):
    result = []
    sign = 1
    for i in string:
        if(i == ' '):
            sign = 1
        else:
            if(sign == 1):
                result.append(i.upper())
            else:
                result.append(i.lower())
            sign = 0
    return ''.join(result)
```

## 5 kyu - Sum of Pairs


>## Sum of Pairs
>
>Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
>
>```python
>sum_pairs([11, 3, 7, 5],         10)
>#              ^--^      3 + 7 = 10
>== [3, 7]
>
>sum_pairs([4, 3, 2, 3, 4],         6)
>#          ^-----^         4 + 2 = 6, indices: 0, 2 *
>#             ^-----^      3 + 3 = 6, indices: 1, 3
>#                ^-----^   2 + 4 = 6, indices: 2, 4
>#  * entire pair is earlier, and therefore is the correct answer
>== [4, 2]
>
>sum_pairs([0, 0, -2, 3], 2)
>#  there are no pairs of values that can be added to produce 2.
>== None/nil/undefined (Based on the language)
>
>sum_pairs([10, 5, 2, 3, 7, 5],         10)
>#              ^-----------^   5 + 5 = 10, indices: 1, 5
>#                    ^--^      3 + 7 = 10, indices: 3, 4 *
>#  * entire pair is earlier, and therefore is the correct answer
>== [3, 7]
>```
>
>Negative numbers and duplicate numbers can and will appear.
>
>**NOTE:** There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.

**原址：**[5 kyu - Sum of Pairs](<https://www.codewars.com/kata/54d81488b981293527000c8f>)

**说明：**

> 给定一个整数列表和一个和值，返回前两个值（请从左侧解析）按照外观的顺序返回以形成总和。可以并且将出现负数和重复数字。

**代码：**

```python
def sum_pairs(ints, s):
    my_dict = {}
    for i, m in enumerate(ints):
        if my_dict.get(s - m) is not None: 
            return [s - m, m]
        else: 
            my_dict[m] = i
```

## 5 kyu - Perimeter of squares in a rectangle


>The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : `4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80`
>
>Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:
>
>![alternative text](http://i.imgur.com/EYcuB1wm.jpg)
>
>\#Hint: See Fibonacci sequence
>
>\#Ref: <http://oeis.org/A000045>
>
>The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.
>
>```
>perimeter(5)  should return 80
>perimeter(7)  should return 216
>```

**原址：**[5 kyu - Perimeter of squares in a rectangle](<https://www.codewars.com/kata/559a28007caad2ac4e000083>)

**说明：**

> 该图显示了6个正方形，其边长为1,1,2,3,5,8。很容易看出这些正方形的周长之和为：4 *（1 + 1 + 2 + 3 + 5 + 8）= 4 * 20 = 80。当有n + 1个方格以与图中相同的方式处理时，你能编写函数给出矩形中所有方块的周长之和。函数周长具有参数n，其中n + 1是正方形（它们从0到n编号）并返回所有正方形的总周长。

**代码：**

```python
def perimeter(n):
    a = [1, 1]
    for i in range(2, n + 1):
        a.append(a[i - 2] + a[i - 1])
    return 4 * sum(a)
```

## 5 kyu - Number of trailing zeros of N!


>Write a program that will calculate the number of trailing zeros in a factorial of a given number.
>
>```
>N! = 1 * 2 * 3 * ... * N
>```
>
>Be careful `1000!` has 2568 digits...
>
>For more info, see: <http://mathworld.wolfram.com/Factorial.html>
>
>## Examples
>
>```py
>zeros(6) = 1
># 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
>
>zeros(12) = 2
># 12! = 479001600 --> 2 trailing zeros
>```
>
>*Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.*

**原址：**[5 kyu - Number of trailing zeros of N!](<https://www.codewars.com/kata/52f787eb172a8b4ae1000a34>)

**说明：**

> 编写一个程序，计算给定数字的阶乘中的尾随零的数量。

**代码：**

```python
def zeros(n):
    sumcac = 0
    i = 5
    while(i < n):
        sumcac += len(range(i, n + 1, i))
        i *= 5
    return sumcac
```

## 5 kyu - Human Readable Time


>## Detials
>
>Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (`HH:MM:SS`)
>
>- `HH` = hours, padded to 2 digits, range: 00 - 99
>- `MM` = minutes, padded to 2 digits, range: 00 - 59
>- `SS` = seconds, padded to 2 digits, range: 00 - 59
>
>The maximum time never exceeds 359999 (`99:59:59`)
>
>You can find some examples in the test fixtures.

**原址：**[5 kyu - Human Readable Time](<https://www.codewars.com/kata/52685f7382004e774f0001f7>)

**说明：**

> 编写一个函数，它以非负整数（秒）作为输入，并以人类可读的格式返回时间（`HH：MM：SS`）。

**代码：**

```python
def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds - hh * 3600) // 60
    ss = seconds - hh * 3600 - mm * 60
    time = [hh, mm, ss]
    for i in range(3):
        time[i] = '0' + str(time[i]) if time[i] < 10 else str(time[i])
    return ':'.join(time)
```

## 5 kyu - Did I Finish my Sudoku


>Write a function done_or_not/`DoneOrNot` passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'
>
>Sudoku rules:
>
>Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.
>
>Rows:
>
>![img](http://www.sudokuessentials.com/images/Row.gif)
>
>There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.
>
>In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.
>
>Columns:
>
>![img](http://www.sudokuessentials.com/images/Column.gif)
>
>
>
>There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.
>
>In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.
>
>Regions
>
>![img](http://www.sudokuessentials.com/images/Region.gif)
>
>A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.
>
>Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.
>
>In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.
>
>Valid board example:
>
>![img](http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/364px-Sudoku-by-L2G-20050714_solution.svg.png)
>
>For those who don't know the game, here are some information about rules and how to play Sudoku: <http://en.wikipedia.org/wiki/Sudoku> and <http://www.sudokuessentials.com/>

**原址：**[5 kyu - Did I Finish my Sudoku](<https://www.codewars.com/kata/53db96041f1a7d32dc0004d2>)

**说明：**

> 检测是否完成数独

**代码：**

```python
def done_or_not(board): #board[i][j]
    a = list(range(9))
    for i in range(9):
        my_dict1 = dict(zip(board[i], a))
        if(len(my_dict1) != 9):
            return('Try again!')
        my_dict2 = dict(zip([j[i] for j in board], a))
        if(len(my_dict2) != 9):
            return('Try again!')
        x = i % 3 * 3
        y = i // 3 * 3
        my_dict3 = dict(zip(board[y][x:x+3] + board[y+1][x:x+3] + board[y+2][x:x+3], a))
        if(len(my_dict3) != 9):
            return('Try again!') 
    return('Finished!')
```

## 4 kyu - Twice linear


>Consider a sequence `u` where u is defined as follows:
>
>1. The number `u(0) = 1` is the first one in `u`.
>2. For each `x` in `u`, then `y = 2 * x + 1` and `z = 3 * x + 1` must be in `u` too.
>3. There are no other numbers in `u`.
>
>Ex: `u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]`
>
>1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
>
>## Task:
>
>Given parameter `n` the function `dbl_linear` (or dblLinear...) returns the element `u(n)` of the ordered (with <) sequence `u` (so, there are no duplicates).
>
>## Example:
>
>```
>dbl_linear(10) should return 22
>```
>
>## Note:
>
>Focus attention on efficiency

**原址：**[4 kyu - Twice linear](<https://www.codewars.com/kata/5672682212c8ecf83e000050>)

**说明：**

> 给定参数`n`，函数`dbl_linear`（或dblLinear ...）返回有序（带有<）序列`u`的元素`u（n）`（因此，没有重复）。

**代码：**

```python
def dbl_linear(n):
	# your code
    i = 0
    a = [1]
    index2 = 0
    index3 = 0
    while(i < n):
        x = a[index2] * 2 + 1
        y = a[index3] * 3 + 1
        if(x < y):
            a.append(x)
            index2 += 1
            i += 1
        elif(x > y):
            a.append(y)
            index3 += 1
            i += 1
        elif(x == y):
            index3 += 1
    return(a[n])
```

## 4 kyu - Sudoku Solution Validator


>### Sudoku Background
>
>Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9. 
>(More info at: <http://en.wikipedia.org/wiki/Sudoku>)
>
>### Sudoku Solution Validator
>
>Write a function `validSolution`/`ValidateSolution`/`valid_solution()` that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
>
>The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
>
>### Examples
>
>```
>validSolution([
>[5, 3, 4, 6, 7, 8, 9, 1, 2],
>[6, 7, 2, 1, 9, 5, 3, 4, 8],
>[1, 9, 8, 3, 4, 2, 5, 6, 7],
>[8, 5, 9, 7, 6, 1, 4, 2, 3],
>[4, 2, 6, 8, 5, 3, 7, 9, 1],
>[7, 1, 3, 9, 2, 4, 8, 5, 6],
>[9, 6, 1, 5, 3, 7, 2, 8, 4],
>[2, 8, 7, 4, 1, 9, 6, 3, 5],
>[3, 4, 5, 2, 8, 6, 1, 7, 9]
>]); // => true
>
>validSolution([
>[5, 3, 4, 6, 7, 8, 9, 1, 2], 
>[6, 7, 2, 1, 9, 0, 3, 4, 8],
>[1, 0, 0, 3, 4, 2, 5, 6, 0],
>[8, 5, 9, 7, 6, 1, 0, 2, 0],
>[4, 2, 6, 8, 5, 3, 7, 9, 1],
>[7, 1, 3, 9, 2, 4, 8, 5, 6],
>[9, 0, 1, 5, 3, 7, 2, 1, 4],
>[2, 8, 7, 4, 1, 9, 6, 3, 5],
>[3, 0, 0, 4, 8, 1, 1, 7, 9]
>]); // => false
>```

**原址：**[4 kyu - Sudoku Solution Validator](<https://www.codewars.com/kata/529bf0e9bdf7657179000008>)

**说明：**

> 数独解决方案验证器

**代码：**

```python
def validSolution(board):
    a = list(range(9))
    for i in range(9):
        my_dict1 = dict(zip(board[i], a))
        if len(my_dict1) != 9:
            return False
        my_dict2 = dict(zip([j[i] for j in board], a))
        if len(my_dict2) != 9:
            return False
        x = i % 3 * 3
        y = i // 3 * 3
        my_dict3 = dict(zip(board[y][x:x+3] + board[y+1][x:x+3] + board[y+2][x:x+3], a))
        if len(my_dict3) != 9:
            return False
    return True
```

## 4 kyu - Next bigger number with the same digits


>You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
>
>```js
>12 ==> 21
>513 ==> 531
>2017 ==> 2071
>```
>
>If no bigger number can be composed using those digits, return `-1`:
>
>```js
>9 ==> -1
>111 ==> -1
>531 ==> -1
>```

**原址：**[4 kyu - Next bigger number with the same digits](<https://www.codewars.com/kata/55983863da40caa2c900004e>)

**说明：**

> 您必须创建一个带有正整数的函数，并返回由相同数字组成的下一个更大的数字。如果使用这些数字不能组成更大的数字，则返回-1。

**代码：**

```python
def next_bigger(n):
    result = []    
    list_n = list(str(n))
    min_n = sorted(list_n, reverse=True)
    length = len(list_n)
    if(n == int(''.join(min_n))):
        return(-1)
    else:
        for i in range(length - 2, -1, -1):
            for j in range(length - 1, i, -1):
                if(list_n[i] < list_n[j]):
                    list_n[i], list_n[j] = list_n[j], list_n[i]
                    return(int(''.join(list_n[:i + 1]) + ''.join(sorted(list_n[i + 1:]))))
```
