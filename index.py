#task 2   

fwr=[{'product':'shoe', 'id':1, 'size':5, 'price':2000, 'brand':'nike', 'stock':3}]
while True:
    print('''
1.product details
2.view product details
3.update product details
4.search product details
5.delete product details
6.exit             
          ''')
    choice=int(input('enter the choice :'))

    if choice==1:
          product=str(input("enter product :"))
          id=int(input("enter id :"))
          size=int(input("enter size :"))
          brand=str(input("enter brand :"))
          price=str(input("enter price :"))
          stock=int(input("enter stock :"))
          fwr.append({'product':product, 'id':id, 'size':size,  'brand':brand, 'price':price, 'stock':stock})

        
    elif choice==2:
        for i in fwr:
            print(i)


    elif choice==3:
        id=int(input("enter id :"))
        f=0
        for i in fwr:
         if id == i['id']:                                                                            
             while True:
                  print('''
                     1.product
                     2.size
                     3.brand
                     4.price
                     5.stock
                     6.exit''')
                  choice=int(input('enter the choice :'))
                  if choice == 1:
                         product=str(input('enter product :'))
                         i['product']=product
                  elif choice==2:
                         size=int(input('enter size :'))
                         i['size']=size                                                                      
                  elif choice==3:
                         brand=str(input('enter brand :'))
                         i['brand']=brand
                  elif choice==4:
                         price=int(input('enter price :'))
                         i['price']=price
                  elif choice==5:
                         stock=str(input('enter stock :'))
                         i['stock']=stock
                  else:
                         break
                         f=1
         if f==0:
                 print('invalid name')


    elif choice==4:
        id=int(input("enter id :"))
        f=0
        for i in fwr:
            if id == i['id']:
              print(i)
              f=1
        if f==0:
                print('invalid name')


    elif choice==5:
         id=int(input("enter id :"))
         f=0
         for i in fwr:
            if id == i['id']:
              fwr.remove(i)
              f=1
              if f==0:
                print('invalid name')


    elif choice==6:
        break

    else:
        ('invalid option')







