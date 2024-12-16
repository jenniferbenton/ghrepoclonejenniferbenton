ep1 = {'EmployeeID',221092,'EmployeeName','Fedrick Zocco','Number of Experience',2,'Current Position','Research Scientist'}

for emp_data in ep1:
    print(f'Employee Data Key: {emp_data}')
    print(f'Employee Data Values:{ep1[emp_data]}')
    ep1[emp_data] = 'Jenny B'
    ep1[emp_data] = 50045336
    if emp_data == 'EmployeeName':
        ep1[emp_data] = 'Jenny B'
    elif emp_data == 'EmployeeID':
        ep1[emp_data] = '50045336'
    elif emp_data == 'Current Position':
        ep1[emp_data] = 'Apprentice'
    else:
        ep1[emp_data] = 1
print(f'Employee data after the change')


