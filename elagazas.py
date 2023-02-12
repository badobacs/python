kor=input("Kerlek ird be a korod\n")
kor=int(kor)

vezet=input("Kerlek ird be hogy vezet-e\n")


# if kor<18:
#     print("Kiskoru")
# else:
#     print("Nagykoru")
    
if kor<6:
    print("Kisgyerek")
elif kor<18:
    print("Kiskoru")
elif kor<65:
    print("Nagykoru")
else: 
    print("nyugdijas")    

vezet=(vezet)


if kor<18:
    print("nem ihat")
else:
    if vezet==True:
        print("nem ihat")
    else:
            print("ihat")
    
    
if kor<18 or vezet==True:
    print("nem ihat")
else: print("ihat")
    
    
