import inspect
from objprint import op

glo_var = 1

def bar():
    bar_frame = inspect.currentframe()
    # op(bar_frame)
    print(bar_frame.f_back.f_lineno)


def foo():
    foo_frame = inspect.currentframe()
    op(foo_frame)
    bar()


if __name__ == "__main__":
    foo()