list = [1,2,3,4,5,6,7,8,9,10]
a = len(list)
if a % 2 == 0:
    newlistf = list[:int(a/2)]
    newlists = list[int(a/2):]
    newlists.extend(newlistf)
    print(newlists)
else:
    newlistf = list[:int((a-1)/2)]
    newlists = list[int((a+1)/2):]
    newlists.append(list[int((a+1)/2 - 1)])
    newlists.extend(newlistf)
    print(newlists)

n = int(input("\n"+"Enter a digit : "))
if len(str(n)) == 1:
    sayac = 0
    while sayac< n-1 :
        sayac = sayac+ 2
        print(sayac)
else:
    print("Please enter a single digit number")
