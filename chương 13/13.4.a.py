f = open('bai_tho.txt','r',encoding="utf-8")
a = f.read(25)
print("nội dung 25 kí tự đầu tiên là \n",a)

b = f.read(35)
print('nội dung 35 kí tự tiếp theo là \n',b)

c = f.read()
print("nội dung còn lại là \n",c)
f = f.close()