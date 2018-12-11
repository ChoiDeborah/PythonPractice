#example_01

a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']

print(a[4] +' '+ a[2])

#example_02

result = " ".join(a)
print(result)


#example_03

a = [1, 2, 3]

#print(a.__len__())
print(len(a))


#example_04

num = [1, 2, 3]
num.append([4,5])
print(num)

num = [1, 2, 3]
num.extend([4,5])
print(num)

#example_05

arr = [1, 3, 5, 4, 2]

arr.sort(reverse = True)
#arr.reverse()

print(arr)

#example_06

arr = [1, 2, 3, 4, 5]
arr.remove(2)
arr.remove(4)

print(arr)

