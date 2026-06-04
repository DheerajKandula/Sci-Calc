e = 2.71828
π = 3.14159

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Floor Division\n7.Exponentiation\n8.Root\n9.e Power\n10.10 Power\n11.Factorial\n12.Percentage\n13.Logarithm\n14.Sine\n15.Cosine\n16.Tangent")
c = int(input("Enter the S.No of the Operation you want to use: "))
a = float(input("Enter first number: "))
if(c<=8 | c==12 | c==13):
    b = float(input("Enter second number: "))

def Factorial(a):
    if a==0 or a==1:
        return 1
    return a*Factorial(a-1)

def Percentage(a,b):
    return (a/100)*b

def Logarithm(a,b):
    d = 1
    e = 1
    f = b
    while(f<a):
        e=e*b
        f=f*b
        d=d+1
    return d

def Sine(a):
    i=0
    x=0
    a=a*π/180
    while(i<15):
        x=x+((-1)**i)*(a**(2*i+1))/Factorial(2*i+1)
        i=i+1
    return x

def Cosine(a):
    i=0
    x=0
    a=a*π/180
    while(i<15):
        x=x+((-1)**i)*(a**(2*i))/Factorial(2*i)
        i=i+1
    return x

def Tangent(a):
    return Sine(a)/Cosine(a)

match c:
    case 1: print(a+b)
    case 2: print(a-b)
    case 3: print(a*b)
    case 4: print(a/b)
    case 5: print(a%b)
    case 6: print(a//b)
    case 7: print(a**b)
    case 8: print(a**1/b)
    case 9: print(e**a)
    case 10: print(10**a)
    case 11: print(Factorial(a))
    case 12: print(f"{Percentage(a,b)}%")
    case 13: print(Logarithm(a,b))
    case 14: print(Sine(a))
    case 15: print(Cosine(a))
    case 16: print(Tangent(a))
    case _: print("Nothing was selected")