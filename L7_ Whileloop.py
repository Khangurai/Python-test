#while 
'''''
a=20
b=20
while a<b:
    print('{} hello ray'.format(a))
    a+=1
print('Nothing do!')
'''
#break
'''''
for va in "Raysomething":
    if va=='i':
        break
    print(va)
print('______________ending')
'''
#continue
'''''
for va in "Raysomething":
    if va=='i':
        continue
    print(va)
print('______________ending')
'''
ls  = [60,71,3,32,1]#list
#index 0  1  2 3  4
data = 99
found =False #flag
index =0

while index < len(ls):#true
    if ls[index]==data:
        found=True
        break
    index+=1
if not found:
    ls.append(data)
print(ls)


#different between break and continue