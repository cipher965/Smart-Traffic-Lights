import random
from Algos import GetMaxCarIndex
from TrafficControlVar import NormalTrafficVar,CongestedTrafficVar
from OutputDemo3 import Base,Back,Pole,HeadText
from Basic_Processing import main

NormVal=10

List=main()
for i in range(0,4):
    List[i]=List[i]*random.randrange(1,4)

MaxIndex=int(GetMaxCarIndex(List))

for i in range(0,4):
    print ("\tIntersection ",i+1," - ",List[i]," Cars")

Base()
Pole()
Back()
HeadText()

if List[MaxIndex]<=NormVal :
    print ("Normal Flow of traffic ")
    NormalTrafficVar(List)
else :
    print ("Congested flow of traffic ")
    CongestedTrafficVar(List)