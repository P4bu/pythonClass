x = 100

def local_function():
    x = 10 #Variable local
    print(f'El valor de la variable es: {x}')

local_function()
# print(f'{x} es local, no se mostrara')    

def show_global():
    print(f'El valor de la variable global es {x}')

print(f' la variable global: {x}')