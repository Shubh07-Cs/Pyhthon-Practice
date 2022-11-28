import calendar
D=int(input())
Y=D//365
YR=D%365
M=YR//30
Ds=YR%30
if D>=365:
    print(Y,"Y",M,"M",Ds,"D")
elif D<=365:
    print(M,"M",Ds,"D")    
else:
    print("False")    