x=float(input())
g=[1,999]
c=[1000,5000]
v=[5001,10000]
if x>=g[0] and x<=g[1]:
    print(x)
elif x>=c[0] and x<=c[1]:
    x=x-((x/100)*5)
    print(x)
elif x>=v[0] and x<=v[1]:
    x=x-((x/100)*10)
    print(x)
elif x >=10001:
    x=x-((x/100)*15)
    print(x)