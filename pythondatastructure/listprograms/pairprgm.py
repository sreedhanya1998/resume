lst=[2,1,3,4,6,7]
lst.sort()
#[1,2,3,4,6,7]
 # l.........u
  #lst[1]+lst[u]=total   1+7=8
  #  move upp backward if searching element<total
#if searching element>total
 #   move low forward

low=0
upp=len(lst)-1
element=int(input("enter the number"))
while(low<=upp):
     total=lst[low]+lst[upp]
     if(element<total):
         upp=upp-1
     elif(element>total):
         low=low+1
     elif(element==total):
         print("pairs are",(lst[low],lst[upp]))
         break



