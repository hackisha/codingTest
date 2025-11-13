# codingTest
코딩테스트 벼락치기,,, <br>
https://blog.encrypted.gg/941 <br>

https://freedeveloper.tistory.com/373 <br>

인덱스 신경쓰기, 자료형 헷갈리면 그냥 print(type(x)) 찍어보기


### 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다..(;;)<br>
``` python
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)
```
### 람다 표현식
함수를 간단하게 작성할 때 사용
``` python3
#add함수를 간단하게 구현하면

print((lambda a, b: a + b)(3, 7)
#출력: 10
```

#### 람다 표현식 예: 내장 함수에서 자주 사용되는 람다 함수
```python3
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
  return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))


```
#### 람다 표현식 예: 여러 개의 리스트에 적용
``` python3
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a+ b, list1, list2)

print(list(result))


result = map(lambda a,b : a+b, list1, list2)
#결과: [7,9,11,13,15]
```
