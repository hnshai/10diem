f = open("bai_tho.txt","r+")
a = f.read(12)
print("12 kí tự đầu tiên ",a)
b =f.tell(12)
print('vị trí hiện thời',b)
f.seek(0)
c = f.read(12)
print(c)