data1=input("data1: ")
data2=input("data2: ")
data3=input("data3: ")
data4=input("data4: ")
datas1=dict(zip(data1.split(","),data2.split(",")))
datas2=dict(zip(data3.split(","),data4.split(",")))
a=input("key: ")
if  a in datas1 and a in datas2:
    print("present in first and second dictionary")
elif a in datas1:
    print("present in the first dictionary")
elif a in datas2:
    print("present in the second dictionary")
else:
    print("key is not present")