s = '1h2j3Л4я5'
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 'abcdefghijklmnopqrstuvwxyz'
A_r = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
a_r = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(s)):
    if (s[i] in A) or (s[i] in a) or (s[i] in A_r) or (s[i] in a_r):
        s = s.replace(s[i], ' ')
s = s.split()
s = ''.join(map(str, s))

su = 0
for i in range(len(s)):
    su = su + int(s[i])
print(su)
