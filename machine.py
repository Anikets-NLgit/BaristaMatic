# from ast import And


default_inventory={'Cocoa':10,
                'Coffee':10,
                'Cream':10, 
                'Decaf Coffee':10, 
                'Espresso':10, 
                'Foamed Milk':10, 
                'Steamed Milk':10, 
                'Sugar':10, 
                'Whipped Cream':10}
inventory={'Cocoa':10,
                'Coffee':10,
                'Cream':10, 
                'Decaf Coffee':10, 
                'Espresso':10, 
                'Foamed Milk':10, 
                'Steamed Milk':10, 
                'Sugar':10, 
                'Whipped Cream':10}

def default_inventor():
    # global inventory
    # inventory=default_inventory
    for key, value in inventory.items():
        print(key,",",value)
    # print(inventory)
    return

def availability(drink):
    if drink==1:
        if inventory['Espresso']-3>0:
            return True
        else:
            return False
    elif drink==2:
        if inventory['Espresso']-2>0 and inventory['Steamed Milk']-1>0:
            return True
        else:
            return False
    elif drink==3:
        if inventory['Espresso']-1>0 and inventory['Cocoa']-1>0 and inventory['Steamed Milk']-1>0 and inventory['Whipped Cream']-1>0:
            return True
        else:
            return False
    elif drink==4:
        if inventory['Espresso']-2>0 and inventory['Steamed Milk']-1>0 and inventory['Foamed Milk']-1>0:
            return True
        else:
            return False
    elif drink==5:
        if inventory['Coffee']-2>0 and inventory['Sugar']-1>0 and inventory['Cream']-1>0:
            return True
        else:
            return False
    elif drink==6:
        if inventory['Decaf Coffee']-3>0 and inventory['Sugar']-1>0 and inventory['Cream']-1>0:
            return True
        else:
            return False

def menu():
    print("Menu:")
    print('1','Caffe Americano,','$3.30',availability(1))
    print('2','Caffe Latte','$2.55,',availability(2))
    print('3','Caffe Mocha,','$3.55,',availability(3))
    print('4','Cappuccino,','$2.90,',availability(4))
    print('5','Coffee,','$2.75,',availability(5))
    print('6','Decaf,','$2.75,',availability(6))
    return
def InvtUpdate(Itemno):
    if Itemno==1:   
        if availability(1)==True:
            inventory['Espresso']=inventory['Espresso']-3
            print('Despensing: Caffe Americano')
        else:
            print("Out of stock. Please select other drink")

    elif Itemno==2:
        if availability(2)==True:
            inventory['Espresso']=inventory['Espresso']-2
            inventory['Steamed Milk']=inventory['Steamed Milk']-1
            print('Despensing: Caffe Latte')
        else:
            print("Out of stock. Please select other drink")    
    elif Itemno==3:
        if availability(3)==True:
            inventory['Espresso']=inventory['Espresso']-1
            inventory['Cocoa']=inventory['Cocoa']-1
            inventory['Steamed Milk']=inventory['Steamed Milk']-1
            inventory['Whipped Cream']=inventory['Whipped Cream']-1
            print('Despensing: Mocha')
        else:
            print("Out of stock. Please select other drink")
    elif Itemno==4:
        if availability(4)==True:
            inventory['Espresso']=inventory['Espresso']-2
            inventory['Steamed Milk']=inventory['Steamed Milk']-1
            inventory['Foamed Milk']=inventory['Foamed Milk']-1
            print('Despensing: Cappuccino')
        else:
            print("Out of stock. Please select other drink")
    elif Itemno==5:
        if availability(5)==True:
            inventory['Coffee']=inventory['Coffee']-2
            inventory['Sugar']=inventory['Sugar']-1 
            inventory['Cream']=inventory['Cream']-1
            print('Despensing: Coffe')
        else:
            print("Out of stock. Please select other drink")
    elif Itemno==6:
        if availability(6)==True:
            inventory['Decaf Coffee']=inventory['Decaf Coffee']-3
            inventory['Sugar']=inventory['Sugar']-1
            inventory['Cream']=inventory['Cream']-1
            print('Despensing: Decaf')
        else:
            print("Out of stock. Please select other drink")
    else:
        print('Invalid Selection')
    return

if __name__=="__main__":
    select='a'
    while select!='q' and select!='Q':
        default_inventor()
        menu()
        Itemno=int(input("Select your drink"))
        select=str(input("Press r/R for restock Or q/Q for quit or c/C for continue"))
        InvtUpdate(Itemno)
        if select=='r':
        #     default_inventor()
            # print(inventory)
            inventory=default_inventory
            # print('r in if')
        
        # print(default_inventory)
        # default_inventor()
    default_inventor()
    print('Come back again')
    
    


    # x=id(default_inventory())
    # a = ctypes.cast(x, ctypes.py_object).value
    # print(a)