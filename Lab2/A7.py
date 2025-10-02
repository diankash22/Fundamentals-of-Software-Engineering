row1=int(input("Строка 1="))
column1=int(input("Колонка 1="))
row2=int(input("Строка 2="))
column2=int(input("Колонка 2=")) #если посмотреть на шахматную доску то сумма четных координат состветвувет белому цвету,а нечетное черному

sum1=row1+column1
sum2=row2+column2

if sum1%2==0 and sum2%2==0 or sum1%2==1 and sum2%2==1:
    print("YES")
    if sum1%2==0 and sum2%2==0:
        print("White")
    else :
        print("Black")
else :
    print("NO")