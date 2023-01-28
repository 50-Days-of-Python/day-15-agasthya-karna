#Write your code here.
def num(l):
    l1=[]
    for j in range(len(l)):
        c=0
        s=''
        y=len(str(l[j]))
        x=str(l[j])[::-1]
        for i in range(y):
            if(y%2==0):
                if(c%3==0 and i!=y-1 and i!=0):
                    s=s+","
                s=s+x[i]
                c=c+1
            else:
                if(c%3==0 and i!=y and i!=0):
                    s=s+","
                s=s+x[i]
                c=c+1
        l1.append(s[::-1])
    return l1

l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))

print(num(l))
