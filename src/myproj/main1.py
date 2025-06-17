import sys
import myutil.plus as my_plus
import myutil.minus
import myutil2

print('main1.py __name__ =', __name__)

# __name__: 모든 파이썬 모듈(.py 파일)이 갖고 있는 특별한 변수.
#   (1) 현재 파일을 실행할 때는 __name__ 변수에 '__main__' 문자열이 할당.
#   (2) 다른 파일에서 import될 때는 __name__ 변수에는 파일 이름이 할당.
#   (목적) 단독으로 실행할 코드와 import될 때 실행할 코드를 구분하기 위해서.
if __name__ == '__main__':
    print(sys.version)
    result = my_plus.plus(1, 2)
    print('result =', result)

    result = myutil.minus.minus(1, 2)
    print('result =', result)

    result = myutil2.multiply(2, 3)
    print('result =', result)

    result = myutil2.divide(2, 3)
    print('result =', result)
