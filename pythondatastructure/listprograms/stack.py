#how to push to stack
#top=0
#if(top>sizeof(stack))
 #   stack is full
#else
 #   stack[top]=element
  #  top=top+1

#push
lst=[]
size=3
top=0
item=int(input("enter the number"))
if(top<=size):
    lst.append(item)
    top+=1
print(lst)
#pop
top=3
size=3
lst=[10,20,30]
if(size>top):
    lst.pop()
    top-=1
