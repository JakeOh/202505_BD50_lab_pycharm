from oracledb import DatabaseError

from src.myproj.db_util import get_connection

# dept_ex 테이블의 모든 레코드 검색
sql_select = 'select * from dept_ex order by deptno'

# sql_select를 실행하고 그 결과를 출력하는 함수
def select_dept():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql_select)
                for row in cursor:
                    print(row)
            except DatabaseError as e:
                print(e)


if __name__ == '__main__':
    select_dept()
