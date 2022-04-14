#https://open.kattis.com/problems/speedlimit 

miles = 0 
time = 0

while(True):
    x = input()
    if x == "-1":
        print(str(miles) + " miles")
        break
    
    split = x.split(" ")
    
    # Start of new block 
    if len(split) == 1:
        if (miles != 0):
            print(str(miles) + " miles") 
        miles = 0 
        time = 0
        continue
    

    newTime = int(split[1])
    miles += int(split[0]) * (newTime - time)
    time = newTime
