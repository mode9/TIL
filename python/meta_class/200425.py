# Hello = type('hello', (), {})
# print(Hello)
#
#
# def replace(self, old, new):
#     while old in self:
#         self[self.index(old)] = new
#
#
# AdvancedList = type('AdvancedList', (list,), {'desc': '향상된 리스트', 'replace': replace})
#
# x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
# x.replace(1, 100)
# print(x)
# print(x.desc)
#
#
# class MakeCalc(type):
#     def __new__(mcs, name, bases, namespace):
#         namespace['desc'] = '계산 클래스'
#         namespace['add'] = lambda self, a, b: a + b
#         return type.__new__(mcs, name, bases, namespace)
#
#
# Calc = MakeCalc('Calc', (), {})
# c = Calc()
# print(c.desc)
# print(c.add(1, 2))
#
#
class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class Hello(metaclass=Singleton):
    pass


a = Hello()
b = Hello()
print(a is b)
print(id(a))
print(id(b))


# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#     """대문자로 변환된 속성의 리스트와 함께 클래스 객체를 반환합니다."""
#     uppercase_attr = {}
#     for name, val in future_class_attr.items():
#         if not name.startswith('__'):
#             uppercase_attr[name.upper()] = val
#         else:
#             uppercase_attr[name] = val
#     return type(future_class_name, future_class_parents, uppercase_attr)
#
#
# __metaclass__ = upper_attr
#
#
# class Foo():
#     bar = 'bip'
#
#
# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))
#
# f = Foo()
# print(f.BAR)


class UpperAttrMetaclass(type):

    def __new__(mcs, cls_name, bases, dct):
        upper_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                upper_attr[name.upper()] = val
            else:
                upper_attr[name] = val
        return super(UpperAttrMetaclass, mcs).__new__(mcs, cls_name, bases, upper_attr)


class Foo(metaclass=UpperAttrMetaclass):
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)
