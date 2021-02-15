import random


def bubbleSort(list):
    sorted = False
    while(sorted is False):
        sorted = True
        for j in range(len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                sorted = False
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]


size = 20
num_list = []
for i in range(size):
    num_list.append(random.randint(0, 100))


print(num_list)


bubbleSort(num_list)
print(num_list)
