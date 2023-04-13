
# 容器泛型接口
class SingletonContainer:

    def __init__(self):
        raise NotImplemented

    def put(self, element):
        raise NotImplemented

    def get(self):
        raise NotImplemented


class PyGTContainer(SingletonContainer):

    # 定义容器中元素的类型
    class Entry:
        """
        每个entry应该是名字和对象（模块对象、类对象、函数对象）
        这个名字应该是该对象的唯一标识符
        """
        pass

    def __init__(self):
        pass

    def put(self, entry:Entry):
        pass

    def get(self)->Entry:
        pass

