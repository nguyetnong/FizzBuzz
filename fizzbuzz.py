number=(input("nhap 2 so bat ki:"))
num_split=number.split()
a=int(num_split[0])
b=int(num_split[1])

if a>b:
    print("so ket tthuc can lon hon so bat dau:a<b")
else:
    for i in range(a,b+1):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else :
            print("khong thuoc truong hop tren in ra i:",i)
            
    
