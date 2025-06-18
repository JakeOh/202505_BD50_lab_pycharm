from .connect import get_connection

# Oracle 21c 버전에서는 create table if not exists table_name,
# drop table if exists table_name 구문을 제공하지 않음.
# Oracle 23ai 버전에서는 if not exists, if exists 문법이 가능.
sql_create_table = '''
create table dept_ex
as select * from dept
'''
