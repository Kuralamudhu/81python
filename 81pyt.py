hh1,jj1=map(int,input().split())
ss1=list(map(int,input().split()[:hh1]))
cat=0
for g in ss1:
   if(g==jj1):
      cat=cat+1
print(cat) 
