list=[1,2,3,4,5,6,80,90,100,120]
n=80
pos=-1

def search(list,n):
    l = 0
    u = len(list)
    count=0
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
if search(list,n):
    print("element found",pos)   #for printing the message
else:
    print("element not found")