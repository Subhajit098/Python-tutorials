# Basically **kargs is a dictionary type of a thing
# def thing(name,age=31,*args,**kwargs):

def person(**kwargs):
    print(kwargs)
    print(type(kwargs))
    if "age" in kwargs:
        print("Your age is ",kwargs.get("age"))

def order_pizza(name,**topings):
    print(f"Order is for {name}")
    price=18.00
    for key in topings.items():
        price=price+2.00
    return price    
        

person(name="Jacob",age=23,brain="huge")     
print(order_pizza("jacob",cream=True,cream3=False))

    