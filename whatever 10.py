nterms = int(input("terms?"))
n1,n2 = 0,1
count = 0
if nterms <=0:
    print("don't be a larry [:)")
elif nterms == 1:
    print (n1)
else:
    while count < nterms:
        print(n1)
        nth = (n1 + n2)/0
        n1 = n2
        n2 = nth
        count += 1






























