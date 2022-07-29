number = [4, 3, 7, 4, 2, 9]
#number.append(3) append is used for add number in last
#number.remove(9) remove is used for remove a digit that we give him
#number.pop()  pop is used to remove last item of list
#number.clear() clear is used to remove all items of list
#number.insert(1, 8) is used to insert a item first index then add number
#print(number.index(70)) index is used for check index of number
#print(4 in number) to find a digit in list
#print(number.count(4)) to count digit in list
#number.sort() to sort item in list
#number.reverse() to add decending order in list
#number2 = number.copy() copy last item of list and add in new
#number.append(5) list then
#print(number2) print other variable
unique = []
for duplication in number:
    if duplication not in unique:
        unique.append(duplication)
print(unique)