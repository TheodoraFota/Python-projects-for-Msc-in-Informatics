def main():
    print('FIBONACCI NUMBERS!')
    print('-------------------')
    choice=int(input('Give me a term of  Fibonacci sequence: '))
    f=fibonacci(choice)
    if is_prime(f):
        print("The value of Fibonaccis' term",choice,'is',f,"and it's prime!")
    else:
        print("The value of Fibonaccis' term",choice,'is',f,"and it's not prime!")

def fibonacci(x):
    #RETURNS THE VALUE OF FIBONACCI FOR X 
    a=1
    b=1
    for i in range(x-2):
        tmp=b
        b=a+b
        a=tmp
    return b

def is_prime(number):
    #RETURNS IF A NUMBER IS PRIME OR NOT
    flag=True 
    for i in range(1,number):
        if not(((pow(i,number)-i)%number==0)):
            flag=False
    return flag
main()
