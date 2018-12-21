#一个登陆读写本地文件的小demo

name=['chen','wang','li']
password='111'
count=0
with open(r'C:\Users\Administrator\Desktop\sss.txt','r') as namelist:
    list=namelist.readlines()
    list1=[]
    for i in list:
        list1.append(i.rstrip('\n'))
    print(list1)
    while count<3 :
        _name=input("name:")
        _password=input("password:")
        if _name in list1 :
            print("ni yi bei suoding")
            break
        elif _name in name and _password==password:
            print("ni hao:",_name)
            break
        else:
            count+=1
    else:
        print("ni yi bei suoding")
        with open(r'C:\Users\Administrator\Desktop\sss.txt', 'w') as namelist:
            list.append(_name)
            for i in list:
                namelist.write(i+"\n")




