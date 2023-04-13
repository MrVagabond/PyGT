import ast
import sys
import inspect
import mypy


def get_decorators(cls):
    """
    :param cls: 输入一个类对象
    :return: 返回一个字典，键是类中的属性名，值是该属性方法的装饰器列表
    """
    target = cls
    decorators = {}

    def visit_FunctionDef(node):
        decorators[node.name] = []
        for n in node.decorator_list:
            name = ''
            if isinstance(n, ast.Call):
                name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
            else:
                name = n.attr if isinstance(n, ast.Attribute) else n.id

            decorators[node.name].append(name)

    node_iter = ast.NodeVisitor()
    node_iter.visit_FunctionDef = visit_FunctionDef
    node_iter.visit(ast.parse(inspect.getsource(target)))
    return decorators



# Python装饰器只能装饰函数？貌似不能装饰类
# 那如果我想装饰类的方法，**执行流程**是怎样的？
def test(func):
    return func

def weave_in(func):

    def inner(*args, **kwargs):
        print("织入开始")
        r = func(*args, **kwargs)
        print("织入结束")
        return r

    return inner

class Person(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    @test
    def addMoney(self, n:int) -> bool:
        self.money += n
        print(self.name + "增加" + str(n) + "块钱")
        return True



# Python的名字解析规则是什么？
# 主模块的名字空间添加规则是什么？好像




if __name__ == "__main__":

    print(dir())


    # 获取需要代理的类对象
    clazz:type = getattr(sys.modules["__main__"], "Person")
    # print(dir(clazz))


    # 创建一个同名类，照搬原类的属性方法，对加了test的属性方法做代理
    clazzProxy = type(clazz.__name__, clazz.__bases__, dict())
    # print(dir(clazzProxy))

    # print(get_decorators(clazz))
    for k, v in get_decorators(clazz).items():
        if "test" in v:
            print(k + " need be checked")
            setattr(clazzProxy, k, weave_in(getattr(clazz, k)))
        else:
            setattr(clazzProxy, k, getattr(clazz, k))

    # print(dir(clazzProxy)) # 打印创建的代理类


    # 一些简单验证
    # clazz("mrzj1", 24, 1000).addMoney(10)
    # clazzProxy("mrzj2", 24, 1000).addMoney(10)
    # Person("mrzj3", 24, 1000).addMoney(10)

    # 修改名字绑定
    setattr(sys.modules["__main__"], "Person", clazzProxy)
    Person("mrzj4", 24, 1000).addMoney(10)      # 偷换成功！！！！！
    print(Person == clazzProxy) # True

