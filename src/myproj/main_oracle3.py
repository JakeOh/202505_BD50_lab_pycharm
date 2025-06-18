# from src.myproj.db_util import create_table
# from src.myproj.db_util import drop_table
# from src.myproj.db_util import create_table, drop_table
import src.myproj.db_util as db

def input_integer(msg):
    while True:
        try:
            dept_no = int(input(msg))
            return dept_no
        except ValueError:
            print('입력값은 정수여야 합니다.')


def show_main_menu():
    print('[0]종료 [1]테이블 생성 [2]테이블 삭제 [3]전체검색 [4]입력 [5]수정 [6]삭제 [7]부서번호검색 [8]부서이름검색')
    menu = input_integer('선택>>> ')
    return menu


def insert_data():
    dept_no = input_integer('생성할 부서 번호 입력>>> ')
    dept_name = input('부서 이름 입력>>> ')
    location = input('부서 위치 입력>>> ')
    db.insert_dept(dept_no, dept_name, location)


def update_data():
    dept_no = input_integer('수정할 부서번호 입력>>> ')
    dept_name = input('새로운 부서 이름 입력>>> ')
    location = input('새로운 부서 위치 입력>>> ')
    db.update_dept(dept_no, dept_name, location)


def delete_data():
    dept_no = input_integer('삭제할 부서번호 입력>>> ')
    db.delete_dept(dept_no)


def search_by_no():
    dept_no = input_integer('검색할 부서번호 입력>>> ')
    db.select_dept_by_deptno(dept_no)


def search_by_name():
    dept_name = input('검색할 부서이름 입력>>> ')
    db.select_dept_by_dname(dept_name)


def main():
    run = True
    while run:
        menu = show_main_menu()
        match menu:
            case 0:
                print('프로그램을 종료합니다.')
                run = False
            case 1:
                db.create_table()
            case 2:
                db.drop_table()
            case 3:
                db.select_dept()
            case 4:
                insert_data()
            case 5:
                update_data()
            case 6:
                delete_data()
            case 7:
                search_by_no()
            case 8:
                search_by_name()
            case _:
                print('메뉴 번호는 0 ~ 8 범위 정수만 가능합니다.')


if __name__ == '__main__':
    main()
