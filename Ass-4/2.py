n=eval(input())
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print(len(a))
p=len(a)
i=0
while i<p:
    if a[i]%2==0:
        print(a[i])
        a.remove(a[i])
        
        p=p-1
        i=i-1
    i=i+1
        
    
    

print(a)
