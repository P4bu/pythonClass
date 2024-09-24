# ejericicio sumatoria
# 1 + 2 + 3 + 4 + 5 

def sumatoria(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumatoria(n-1)

number = 3   
print(sumatoria(number))    
