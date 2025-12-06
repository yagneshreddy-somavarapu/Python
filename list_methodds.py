li = []
num = int(input("Enter number of elements in list: "))
for i in range(num):
    value = int(input("Enter value: "))
    li.append(value)
print(li)
while True:
    print("1.Insert element into list\n2.Delete element from list\n3.Sort the list\n4.Reverse the list\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = int(input("Enter value to insert: "))
        li.append(val)
        print("Updated list:", li)
    elif choice == 2:
        val = int(input("Enter value to delete: "))
        if val in li:
            li.remove(val)
            print("Updated list:", li)
        else:
            print("Value not found in list.")
    elif choice == 3:
        li.sort()
        print("Sorted list:", li)
    elif choice == 4:
        li.reverse()
        print("Reversed list:", li)
    elif choice == 5:
        print("Exiting the program.")
        break