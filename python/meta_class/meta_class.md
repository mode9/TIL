# Meta Class

클래스를 생성하는 클래스.



파이썬은 모두 객체로 이루어져있다.

클래스는 자신의 객체를 생성할 수 있지만, 여전히 클래스 자체는 객체이다.  따라서,

객체를 만족하는 조건은 3가지 정도가 있다.

1. 변수에 할당할 수 있다.
2. 복사할 수 있다.
3. 함수 인자로 전달할 수 있다.
4. 식별가능한 고유 ID(메모리주소 등)가 있다.
5. Attribute가 존재하고 추가할 수 있다.
6. type이 있다.

````python
class A:
  pass

def echo(o):
  print(o)
  
echo(A) # <class '__main__.A'>
id(A) # 140678733512880
dir(A) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__'...]
type(A) # <class 'type'>
````

type은 하나의 인자만 받을 때는 해당 인자의 type을 반환해주지만,

3가지의 인자를 받아 클래스 객체를 반환하기도 하는데,

````python
type(name, bases, attr)
````

Where:

- **`name`**: 클래스의 명칭
- **`bases`**: 튜플형태의 부모클래스 (상속하기 위해서, 비워도 상관X)
- **`attrs`**: key / value 형태의 클래스 속성 Dictionary

````python
>>> MyShinyClass = type('MyShinyClass', (), {}) # 클래스 객체 반환
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # 클래스 인스턴스 생성
<__main__.MyShinyClass object at 0x8997cec>
````

이처럼 클래스 객체를 생성하는 클래스가 메타클래스라고 볼 수 있으며, 파이썬의 Default 메타클래스는 type이다.

#### 메타클래스 활용

그렇다면 메타클래스를 사용하는 이유는 무엇일까?

메타클래스는 일반적으로 클래스가 생성될 때 무언가를 제어하거나 변경하고 싶을 때 사용된다(API 등)

3가지로 정리해보면,

1. 클래스 생성 가로챔
2. 클래스 수정
3. 수정된 클래스 반환

##### 예시 1), 클래스의 모든 속성명을 대문자로 사용하고 싶다면,

```python
class UpperAttrMetaclass(type):
  def __new__(cls, cls_name, parents, attrs):
    uppercase_attrs = {}
    for attr, val in attrs.items():
      if attr.startswith('__'):
        uppercase_attrs[attr] = val
      else:
        uppercase_attrs[attr.upper()] = val
    return super(UpperAttrMetaclass, cls).__new__(cls, cls_name, parents, attrs)
```

클래스 객체가 생성될 때 __new__ 함수가 호출된다. 호출 될 때 인자로 받은 클래스 속성정보가 담긴 attrs를 체크하여

private 속성이 아닌 모든 속성명을 대문자로 변환하는 메타클래스인 UpperAttrMetaclass를 작성하였다.

실제로 해당 메타클래스를 받는 클래스를 작성하여 테스트를 해보면,

```python
class Foo(metaclass=UpperAttrMetaclass):
  bar = 'bp'
>>> hasattr(Foo, 'bar') # return False
>>> hasattr(Foo, 'BAR') # return True
>>> Foo.BAR # 'bp'
```

와 같이 실행되는 것을 볼 수 있다.

##### 예시 2) 싱글톤

```python
class Singleton(type):
  __instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls.__instances:
      cls.__instances[cls] = super().__call__(*args, **kwargs)
    
    return cls.__instances[cls]
```

오직 하나의 인스턴스만 허용하도록 클래스 생성을 제한하는 싱글톤 패턴의 메타클래스를 작성하였다.

클래스가 호출될 때, 만약 해당 클래스의 인스턴스가 존재하지 않으면 생성하여 반환, 존재한다면 이미 생성된 인스턴스를 반환하는 형태이다.

```python
class Bar(metaclass=Singleton):
  pass

a = Bar()
b = Bar()
>>> a is b # True
>>> id(a) #4448322960
>>> id(b) #4448322960
```

##### 예시 3) 다중상속 제한

continue..