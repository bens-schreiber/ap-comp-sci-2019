from addsub import add, sub



def negLogic(x,y): #Creates logic needed for negatives in multiplication and division
    if (x < 0 or y < 0) and not (x < 0 and y < 0):
        neg = True
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        i = [x,y,neg]
        return i
    
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        neg = False 
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        i = [x,y,neg]
        return i



def multHelper(x): ##Turns the list of numbers the mult() function did and adds them all up.
    _ = []
    _.append(add(x[0],x[1]))
    i = len(x)-1
    while i != 1: ## turns a list of (5,5,5) into 5+5 = 10 and then 10 + 5 = 15
        _.append(x[i])
        i = sub(i,1)
        _ = add(_[0],_[1])
        _ = [_]
    x = _[0]
    return x
    

def mult(x,y):
     i = negLogic(x,y) #Returns values needed for dividing negatives
     x = i[0]
     y = i[1]
     neg = i[2]

     _ = 0
     numLibrary = []

     while _ < int(y):
         numLibrary.append(int(x)) ## makes a list of the same number. turns 5 x 3 into (5,5,5)
         _ = add(_,1) 
     if neg == True:
         x = multHelper(numLibrary)
         return -x
     elif neg == False:
         return multHelper(numLibrary)









def natDiv(x,y,neg): #Division of which has no remainder or decimal. Uses neg boolean value.
    i = 0
    while x != 0:
        x = sub(x,y)
        i = add(i,1)
    
    if neg == True: #You cannot naturally divide negative numbers using this function. This boolean value is only used for long divison, where a seperate function makes it dividable.
        i = -i
    return i


def mod(x,y):#mod operator
    i = 0
    while x > 0:
        if sub(x,y) == 0:
            return 0
        if sub(x,y) < 0:
            return x
        x = sub(x,y)
        i = add(i,1)
    return i

def approxDiv(x,y): #The same function as mod, but instead of finding the remainder it finds the closest value
    i = 0
    while x >= y:
        if sub(x,y) == 0:
            return 0
        if sub(x,y) < 0:
            return x
        x = sub(x,y)
        i = add(i,1)
    return i



def div(x,y):
    
    i = negLogic(x,y) #Returns values needed for dividing negatives
    x = i[0]
    y = i[1]
    neg = i[2]

    if mod(x,y) == 0: #If mod of the two numbers equals 0, then it can be divided "naturally" (no decimals)
        x = natDiv(x,y,neg)
        return x
    
    if mod(x,y) != 0: #Here is the long division process, for when the two numbers cannot be divided naturally.
        #X is our number and Y is our Dividend
        a = approxDiv(x,y) #a will be used to find the approx amount a number can go into another (EX: 37/6 = 6)
        b = mod(x,y) #The remainder from the division
        c = mult(b,10) #Take the remainder, and multiply it by 10. This is the step of divison where you create a decimal, and bring down a 0.
        if mod(c,y) == 0: #If the dividend can naturally divide into the remainder, then this method will be used
            
            numLibrary = []#This will keep track of all the numbers, so we can eventually create a single number out of them
            if neg == True:
                numLibrary.append('-')
            numLibrary.append(a)
            numLibrary.append('.')
            b = natDiv(c,y,0)
            numLibrary.append(b)
            x = (float("".join(str(n) for n in numLibrary))) #This will turn the numLibrary into a float.
            return x
        
        
        if mod(c,y) != 0: #If the division needs to go further, this method will be used (UP to 3 sig figs of decimals)
            numLibrary = [] #This will keep track of all the numbers, so we can eventually create a single number out of them
            if neg == True:
                numLibrary.append("-")
            numLibrary.append(a) #The approx number is appended to the list (ex: 37/6, approx num is 6, list is composed of [6]
            numLibrary.append(".") #Place the decimal point
            _ = 0
            while _ != 3:
                a = approxDiv(c,y) #Take the remainder that is multiplied by 10, and now approxDiv it by the dividend
                numLibrary.append(a)
                b = mod(c,y)
                c = mult(b,10)
                if mod(c,y) == 0: #If the number can now be divided naturally, do so
                    x = natDiv(c,y,0)
                    numLibrary.append(x)
                    x = (float("".join(str(n) for n in numLibrary))) #Turns it from list to decimal. Wanted it to be a function but it wouldn't let me
                    return x
                if mod(c,y) != 0: #If the number cannot be divided naturally, continue to the while loop
                    _ = add(_,1)
                    if _ == 3: #If the number has been divided 3 times (3 decimals), stop division, and end there.
                        x = (float("".join(str(n) for n in numLibrary)))
                        return x