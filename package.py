
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("student name" ,['mohamed eldushi' ,'abdullah samer', 'oualid dejaber'])
table.add_column("department" ,['software testing' ,'full-stack' ,'database management'])

table.align = "l"
print(table)
