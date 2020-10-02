#python program to generate fibonacci seriese
a,b = 0,1
n=int(input("Enter number of terms: "))
while(n>0):
    print(a)
    a,b = b,a+b
    n=n-1

    
