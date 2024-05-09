#defing a function for plyer 1
def player_1(n):
    #if there are no chocolater in the bowl then player 1 loses
    if n!=0:
        x=int(input("how many chocolates you want to remove player_1:"))
        if x==1 or x==2:
            n=n-x
            #after picking chocolate player 1 will player 2
            return player_2(n)
    else:
        print("player 2 wins")      
#defing a function for player 2
def player_2(n):    
    #if there are no chocolater in the bowl then player 2 loses
    if n!=0: 
        #if number of chocolates remaining in bowl are even then player 2 will pick 2 chocolates and call player 1   
        if n%2==0:
            n=n-2
            print("player 2 took 2 chocolates")
            return player_1(n)
        #if number of chocolates remaining in bowl are odd then player 2 will pick 1 chocolate and call player 1 
        else:
            n=n-1
            print("player 2 took 1 chocolates")
            return player_1(n) 
    else:
        print("player 1 wins")

player_1(10)
