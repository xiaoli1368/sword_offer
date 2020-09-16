# 该文件主要用来进行 Codewars 代码的测试

# ---------------------------------------------------------------
'''
def disemvowel(string):
    test = 'aoeiuAOEIU'
    for i in test:
        string = string.replace(i, '')
    return string

test = "This website is for losers LOL!"
print(disemvowel(test))

translator = str.maketrans({key: None for key in "aeiouAEIOU"})
print(type(translator))

cac = str.maketrans('','','aeiouAEIOU')
print(cac)

print(test.translate(str.maketrans('','','aeiouAEIOU')))
'''

# # ---------------------------------------------------------------
'''
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
'''

# # ---------------------------------------------------------------
# '''

