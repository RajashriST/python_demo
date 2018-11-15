#Fibonnaci series:-
#0,1,1,2,3,5,8..... 
a,b=0,1
num1=int(input("Enter a number :"))
print("You have entered %d"%num1)

def fibonnaci(n):
    global a,b
    while n>1:
        
        a,b=b,a+b
        print('',end=',')
        print(b,end='')
        n-=1

print(a,",",b,end='')
fibonnaci(num1)
