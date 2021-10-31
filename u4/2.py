prov = str(input())
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 'abcdefghijklmnopqrstuvwxyz'
A_r = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
a_r = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

nov = ''
for i in range(len(prov)):
    if (prov[i] == ' '):
        nov = nov + ' '
    if (prov[i] in A):
        l = A.find(prov[i])
        nov = nov + a[l]
    if (prov[i] in a):
        t = a.find(prov[i])
        nov = nov + A[t]
    if (prov[i] in A_r):
        l = A_r.find(prov[i])
        nov = nov + a_r[l]
    if (prov[i] in a_r):
        t = a_r.find(prov[i])
        nov = nov + A_r[t]
print(nov)
