def bubble_sort(lst):
    for i in range (len(lst)):
        for j in range(len(lst)-1):
            if lst[j]>list[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
            
    return list
list=[20,1,23,45,6,2,34,100]
print(f"unsorted list:{list}")
print(f"sorted list {bubble_sort(list)}")