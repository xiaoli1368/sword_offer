# 7 kyu - Complementary DNA


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

