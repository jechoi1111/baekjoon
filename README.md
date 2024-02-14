# 파이썬 문법

* **배열에 원하는 만큼 숫자 넣기**
    * value = [i + 1 for i in range(30)] : 1 ~ 30 까지의 숫자가 배열에 들어감
    * value = [0 for i in range(30)] : 0 이 30개 들어감

* **띄어쓰기를 기준으로 입력받은 값 모두 숫자로 변환**
    * n, m = map(int, input().split())
    * value = list(map(int, input().split())) : 입력 값을 모두 숫자 배열로 변환

* **사칙연산**
    * // : 몫만 남는 연산자

* **배열 -> 문자열 변환**
    * ' '.join(map(str, tmp)) : 배열을 각 값마다 띄어쓰기를 가진 문자열로 변환
        * join은 배열이 모두 문자여야 가능하다

* **Math 라이브러리**
    * math.floor : 내림

* **배열 Filter**
    * value = list(filter(lambda i: i != n, value))
        * lambda I 는 함수 이름
        * 조건
        * filter할 배열

* **배열의 길이 구하기**
    * len

* **배열에서 값이 있는지 찾기**
    * if x in a
    * a.find(x) : 찾는 값이 없는 경우 -1 반환 (문자열에서만 가능)
    * a.index(x) : 찾는 값이 없는 경우 에러 발생 (문자열, 리스트, 튜플 가능)

* **배열 중복 제거 방법**
    * set : 순서 유지 하지 않음
    * list(dict.fromkeys()) : 기존 리스트의 순서를 유지하고 중복 제거

* **배열 복사**
    * 얕은 복사 : 변형 객체인 리스트를 넣어두고 복사한 배열을 변경 시 기존 배열도 변경
        * list.copy
        * list[:]
    * 깊은 복사 : 어느 배열을 수정하여도 다른쪽에 영향 없음 (import copy)
        * deepcopy 

* **reduce 사용 방법**
    * reduce : functools import reduce
        * reduce(lambda acc, cur: acc + cur[‘age’], data, 0]
        * 함수, 계산식, 데이터, 초기값

* **아스키코드**
    * ord : 문자열 -> 아스키코드
    * chr : 아스키코드 -> 문자열

* **문자열 뒤집기**
    * reverse 
        * 순서
            * 문자열 -> 리스트 : list(str)
            * 리스트 역순 : list.reverse()
            * 리스트 -> 문자열 : ‘’.join(list)
    * [::-1]
        * num1, num2 = input().split()
        * num1 = int(num1[::-1]) -> 역순

* **문자열 출력**
  * sys.stdin.readline
    * EOFError를 발생시키지 않고 빈 문자열을 리턴
  * input
    * EOF 받는 경우 EORError 발생

* **문자열 자르기**
  * String[start:end:step]
    * start: 문자열의 시작 인덱스 (부분 문자열에 포함) - 기본값 0
    * end: 문자열의 끝 인덱스 (부분 문자열에 포함 X)
    * step: 현재 문자에서 step 간격으로 문자 추출 - 기본값 1

* **문자열 제거**
  * String.replace(old_str, new_str, count)
    * old_str: 교체하고 싶은 문자열
    * new_str: 새로 사용하고 싶은 문자열
    * count: 새로운 문자열로 변경 하고 싶은 횟수