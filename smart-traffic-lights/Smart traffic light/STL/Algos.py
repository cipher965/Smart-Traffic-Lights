def GetMaxCarIndex(List):
    IndexVal=0
    Max=List[0]
    for i in range(1,4) :
        if(Max<List[i]):
            IndexVal=i
            Max=List[i]
    return IndexVal

def GetSMaxCarIndex(List):
    if(List[0]>List[1]):
        max=0
        secondmax=1
    else:
        max = 1
        secondmax = 0
    for i in range(2,4):
        if List[i] > List[max]:
            secondmax = max
            max = i
        else:
            if List[i] > List[secondmax]:
                secondmax = i
    return secondmax

def GetTMaxCarIndex(List):
    if (List[0] < List[1]):
        min = 0
        secondmin = 1
    else:
        min = 1
        secondmin = 0

    for i in range(2, 4):
        if List[i] < List[min]:
            secondmin = min
            min = i
        else:
            if List[i] <List[secondmin]:
                secondmin = i

    return secondmin

def Ones(List):
    count=0
    for i in range(0,4):
        if(List[i]==1):
            count=count+1
    return count

def Zeroes(List):
    count=0
    for i in range(0,4):
        if(List[i]==0):
            count=count+1
    return count

def NthZero(List):
    for i in range(0,4):
        if(List[i]==0):
            return i
    return 0

def NonZero(List):
    for i in range(0,4):
        if(List[i]!=0):
            return i
    return 0