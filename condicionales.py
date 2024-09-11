x = 5
if(x > 5): 
    print("X es mayor que 5")
elif(x == 5):
    print("X es igual que 5")    
else:
    print("X es menor que 5")
print("Afuera del IF")

a = 15
b = 20

if(a>10 and b>25):
    print("a es mayor que 10 y b es mayor que 15")
if(a>10 or b>25):
    print("a es mayor que 10 o b es mayor que 25")

if( not a > 25):
    print("a no es mayor que 10")

is_member = True
age = 12

if(is_member):
    if(age >= 15):
        print("Tienes acceso ya que eres miembro y mayor o igual 15 años")
    else:
        print("no tienes acceso ya que eres miembro pero menor a 15 años")
else:
    print("No eres miembro y no tienes acceso")            
