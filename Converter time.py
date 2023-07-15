s=int(input("zaman ra vared konid (be saniye)"))
m=0
h=0
for i in range (9999999999999999999999999999999999999999999999999999999999999999999999):
    if s<60:
        break
    else:
        s=s-60
        m=m+1
for j in range (9999999999999999999999999999999999999999999999999999999999999999999999):
    if m<60:
        break
    else:
        m=m-60
        h=h+1
print(h ,":" ,m ,":" ,s)