EmployeeData = {
    'A':{
        'EmployeeID':123232,
        'EmployeeName': 'Robert Williams',
        'Number of Experience': 16,
        'Current Position': 'IT Manager',
        'Salary': 75000,
         },
    'B': {
        'EmployeeID':219836,
        'EmployeeName': 'Ramon Kapur',
        'Number of Experience': 27,
        'Current Position': 'Plant Manager',
        'Salary': 95212
        },
    'C': {
        'EmployeeID': 100212,
        'EmployeeName': 'Philie Torres',
        'Number of Experience': 32,
        'Current Position': 'CEO',
        'Salary': 923123
        },
    'D': {
        'EmployeeID': 311231,
        'EmployeeName': 'Gail Munes',
        'Number of Experience': 0,
        'Current Position': 'Machine Learning Intern',
        'Salary': 45419
         },
    'E': {
        'EmployeeID': 221092,
        'EmployeeName': 'Fedrick Zocco',
        'Number of Experience': 2,
        'Current Position': 'Research Scientist',
        'Salary': 118910
        }
}
for emp_data in EmployeeData:
    ann_sal = EmployeeData[emp_data]['Salary']
    mont_sal = ann_sal/12
    print(ann_sal)
    print(mont_sal)
    


