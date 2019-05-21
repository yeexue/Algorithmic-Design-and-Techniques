# Uses python3
## copy from https://www.jianshu.com/p/5c41fce5512e 

len1 = input()
n = input()
a = [int(x) for x in n.strip().split()]
le = int(len1)

# check the largest number's index 

index1 = 0

for i1 in range(1,le):
    if a[i1] > a[index1] :
        index1 = i1

# check the second largest number's index 

if index1 == 0 : index2 = 1
else: index2 = 0

for i2 in range(1,le):
    if a[i2] > a[index2] and i2 != index1 :
        index2 = i2

result = a[index2] * a[index1]
print(result)
