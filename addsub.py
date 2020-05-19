def negNumToList(x):
    x = abs(x)
    list = [] # create a list with 0 values
    while len(list) != x: #If the length of the list does not equal x, then append a "1" to the list, until equal. 
        list.append(-1)
    return list

def numToList(x):
    list = [] # create a list with 0 values
    while len(list) != x: #If the length of the list does not equal x, then append a "1" to the list, until equal. 
        list.append(1)
    return list

def isNumNeg(x):
    return x < 0


def negOrPosList(x):
    negNum = isNumNeg(x)
    if negNum:
        x = negNumToList(x)
    else:
        x = numToList(x)
    return x

def detectIfList(x):
    if type(x) is list:
        x = x
    if type(x) is not list:
        x = numToList(x)
    return(x)
    


def addHelper(x,y):

    #check if solution is 0
    if -1 in x or -1 in y:
        if -1 not in x and y:
            if abs(len(x)) == abs(len(y)):
                x = 0
                return x


    if -1 not in x: #Is this a negative solution, or positive (EX: x + y or -x + y)
        if -1 not in y:
            x.extend(y)
            x = len(x)
            return x
            
    
    if -1 in x: #if x is negative
        if -1 in y: #if y is also negative
            x.extend(y) #
            x = len(x)
            x = -x #Do basic addition! But then make sure the output is negative.
            return x
        
        elif -1 not in y: # y must be positive
            if len(x) > len(y): #Will output be positive or negative?
                x = natSub(x,y)
                x = -x
                return x
            if len(x) < len(y):
                x = natSub(y,x)
                return x
            if len(x) == len(y):
                x = add(len(x),len(y))
                x = -x
                return x

    if -1 not in x: # x must be positive.
        if len(y) > len(x): #Will outcome be negative?
            x = natSub(y,x)
            x = -x
            return x
        
        if len(y) < len(x): #Outcome must be positive.
            x = natSub(x,y)
            return x
    
        


def add(x,y): #Addition function
    x = negOrPosList(x) # User may be adding a negative number. Detect if it is negative, and put it in the negative list ([-1, -1]) = -2
    y = negOrPosList(y)
    x = addHelper(x,y) #Basic math logic that dictates if the number will be positive or negative upon outcome of addition
    return x
    
def natSub(x,y): #This is basic Subtraction that only works with natural numbers. Used in the negative number logic. 
    x = detectIfList(x)
    y = detectIfList(y)#in the process of negative addition, the natSub function might be used. The values are already in a list, so we need to detect if it is a list or not, before converting a number to it.
    
    for _ in range(len(y)):
        if 1 in x:
            x.remove(1)
        if 1 not in x:
            x.remove(-1) #function could be a negative, in which we need to remove a -1. Same thing, really
    x = len(x)
    return x


def subHelper(x,y): #subHelper deals with subtraction logic. It turns subtraction problems into addition with negatives EX: x-y = x+(-y)
    if -1 not in x:
        if -1 in y: #x is positive while y is negative
                x = len(x)
                y = len(y)
                x = add(x,y)
                return x    
        if -1 not in y:
            y = len(y)
            y = -y
            x = len(x)
            x = add(x,y)
            return x
    else: # X or Y or both must be negative
        if -1 in x:
            if -1 in y: #both X and Y are negative
                x = len(x)
                x = -x
                y = len(y)
                x = add(x,y)
                return x
            else: 
                if -1 in x: #only X is negative
                    x = len(x)
                    x = -x
                    y = len(y)
                    y = -y
                    x = add(x,y)
                    return x            
        
    
def sub(x,y): #Subtraction that substitutes in negative nuabers and adds. Unlike natSub, it works for cases that will turn out negative, and accepts negative inputs.
    x = negOrPosList(x) 
    y = negOrPosList(y)
    x = subHelper(x,y)
    return x