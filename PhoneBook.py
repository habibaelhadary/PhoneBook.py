def printMainMenu():
    print("1- Search.\n2- Store.\n3- show all contacts.\n4- delete contact.\n5- Exit.\nPlease enter your choice:", end=' ')

choice = 0

phoneBook = {}

try:
    myfile = open('dcs.txt', 'r')
    for line in myfile:
        try:
            key, value = line.split(':')
            value = value.split('\n')
            value = value[0]
            phoneBook[key] = value
        except:
            continue
    myfile.close()
except Exception as e:
    print(e)
    myfile = open('dcs.txt', 'w')
    myfile.close()

while(True):
    printMainMenu()

    choice = input()

    if(choice == '1'):
        name = input("Enter the name: ")
        name = name.lower()
        try:
            num = phoneBook[name]

            print('Name: ', end='')
            print(name)
            print('Number: ', end='')
            print(num)
        except:
            print("name not found!")

    elif(choice == '2'):
        name    = input('Enter the name of your contact: ')
        num     = input('Enter the number of your contact: ')
        name = name.lower()
        phoneBook[name] = num
        myfile = open('dcs.txt', 'a')
        myfile.write(name + ':' + num + '\n')
        myfile.close()
        print('Contact stored successfully!')

    elif(choice == '3'):
        count = 1
        for name, num in phoneBook.items():
            print('N:' + str(count))
            print('Name: ' + name + '\nNumber: ' + num)
            count += 1
    elif(choice == '4'):
        name = input('Enter the name: ')
        if(name in phoneBook.keys()):
            del phoneBook[name]
            print('Name' + name + ' was deleted succesfully')
            myfile = open('dcs.txt', 'w')
            for key, value in phoneBook.items():
                myfile.write(key + ':' + value + '\n')
            myfile.close()
        else:
            print('Name ' + name + ' was not found')
    elif(choice == '5'):
        break
    else:
        print("another choice")
