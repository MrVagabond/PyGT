import aop


def multiply(context):
    print(context.args)
    print(context.kwargs)
    yield
    context.result *= 100



if __name__ == "__main__":
    aop.register(
        handler=multiply,
        modules=aop.match(equals='math'),
        targets=aop.match(regexp='(sin|cos)')
    )



