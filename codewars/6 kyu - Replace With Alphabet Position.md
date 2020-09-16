# 6 kyu - Replace With Alphabet Position


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
>



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

