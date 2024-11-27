class Item:
    def __init__(self,Nazwa,Waga,Wartość):
        self.Nazwa = Nazwa
        self.Waga = Waga
        self.Wartość = Wartość


Crist = []

Crist.append(Item('Hammer',20,60))
Crist.append(Item('GoldBar',400,10000))
Crist.append(Item('Watch',5,500))
Crist.append(Item('Phone',10,1000))
Crist.append(Item('Necklace',5,50))
Crist.append(Item('Computer',300,1000))
Crist.append(Item('Shovel',100,100))
Crist.append(Item('Table',500,550))
Crist.append(Item('Coat',15,200))
Crist.append(Item('Shoes',40,400))

for i in range(0,len(Crist)-1):
    if Crist[i].Wartość/Crist[i].Waga < Crist[i+1].Wartość/Crist[i+1].Waga:
        help1 = Crist[i].Wartość
        help2 = Crist[i].Waga
        help3 = Crist[i].Nazwa
        Crist[i].Wartość = Crist[i+1].Wartość
        Crist[i].Waga = Crist[i+1].Waga
        Crist[i].Nazwa = Crist[i+1].Nazwa
        Crist[i+1].Wartość = help1
        Crist[i+1].Waga = help2
        Crist[i+1].Nazwa = help3


for i in Crist:
    print("Obiekt:",i.Nazwa,i.Waga,i.Wartość,"\n")


MaxWeight = 800
start=0
Knapsack =[]
def Knapsacking(a,Max,Knap):
    if a >= len(Crist):
        return 0
    else:
        for i in range(a,len(Crist)-1):
            if  Crist[i].Waga <= Max:
                Knap.append(Item(Crist[i].Nazwa,Crist[i].Waga,Crist[i].Wartość))
                MaxNew = Max - Crist[i].Waga
                b = a + 1
                if MaxNew < 5 :
                    break
                return Knapsacking(b,MaxNew,Knap)
            else:
                b = a + 1

Knapsacking(start,MaxWeight,Knapsack)
for i in Knapsack:
    print("W Plecaku jest:",i.Nazwa,"\n")


