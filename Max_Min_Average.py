N=int(input("tedad danesh amozan ra vared konid"))
min=int(input("nomre danesh amozan ra vared konid"))
max=min
sum=min
for i in range(N-1):
    a=int(input("nomre danesh amozan ra vared konid"))
    sum=sum+a
    if max<=a:
        max=a
    else:
        min=a
Average=sum/N
print("Average" ,Average)
print("highest score" ,max)
print("lowest score" ,min)