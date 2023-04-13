# 实现一个import_hook，使得Python解释器在运行时会调用该import_hook，
# 完成对主模块的依赖模块、类、函数的递归代理
# 参考实现：
# https://www.github.com/pfalcon/python-imphook



# 递归处理
# 对当前模块，如果它自己包含需要代理的函数对象或类对象，那么先实现这些代理
# 然后再看它依赖的模块对象、函数对象和类对象是否需要代理
# 返回True表示该模块确实发生了代理
# 返回False表示该模块不需要代理

def import_hook():
    pass



# 织入代理逻辑
# 可以按代理逻辑对象的类型确定织入的方式（比如环绕织入、前置织入、后置织入、异常织入）
def weave_in(obj, logic):
    pass