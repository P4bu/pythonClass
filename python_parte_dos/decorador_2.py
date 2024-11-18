def check_access(func):
    def wrapper(employee):
        #Comprobar el rol 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('Acceso denegado')
    return wrapper

@check_access
def delete_employee(employee):
    print(f'Empleado {employee['name']} a sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)