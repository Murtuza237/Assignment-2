#defing a function power()which takes 2 arguments base and power using stack
def power(x,y):
    #anything to the power zero is 1
    if y==0:
        return 1
    #anything to the power 1 is itself
    elif y==1:
        return x
    #anything to the negative power is 1/postive power of itself
    elif y<0: 
        return 1/x*power(x,y+1) 
    #using stack to compute power
    else: 
        return x*power(x,y-1)     

x=int(input("b="))        
y=int(input("e="))
print(power(x,y))
