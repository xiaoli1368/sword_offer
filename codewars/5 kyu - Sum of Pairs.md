# 5 kyu - Sum of Pairs


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
>



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

