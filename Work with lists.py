lst = ['Apple' , 'Banana' , 'Orange' , 'Guava' , 'Grapes']
print("The length of this list is ", len(lst)) 
print("The first item on the list is", lst[0])
print("The last item on the list is ", lst[-1])
lst.append('Papaya')
print("updated list", lst)
lst.remove('Guava')
print("Updated list", lst)
lst.sort()
print ("Sorted list", lst)
lst.pop(1)
print("Updated list", lst)
lst.reverse()
print("Reversed list", lst)
print("Multiplied list", lst*2)
lst=lst[:4]
print("Sliced list", lst)
lst.clear()
print("Updated list", lst)
