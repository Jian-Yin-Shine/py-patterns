'''
策略模式

它定义了算法家族，分别封装起来，让他们可以互相转换，此模式让算法的变化，不会影响使用算法的客户
- 策略模式是一种定义一系列算法的方法，从概念上来讲，所有算法完成的都是相同的工作，只是实现不同，
    他可以以相同的调用方式所有的算法，减少各类算法与算法类之间的耦合
- 策略模式的strategy类层次为context定义了一系列的可供重用的算法或者行为，继承有助于析取出这些算法的公用部分
- 解决的问题：不同行为堆砌在同一类中，很难避免使用条件语句，通过stratepy 消除
- 作用：封装算法、业务规则等

- 课程内容：
- 动机：某些对象使用的算法可能多种多样，经常改变，
        如果将这些算法都编码到对象中，将使得对象变得异常复杂，而且有时候支持不使用的算法也是一种负担

        在运行中根据需要透明地更改对象的算法，将算法和对象本身解耦

- strategy 模式提供了用于条件判断外的另一种解决方案
- strategy 及子类组件 提供了一系列可重用算法，从而可以使得类型
            在运行时，方便地根据需要在各个算法中切换
'''


from abc import abstractmethod, ABCMeta

class Strategy(object):
    """
    策略类， 定义所有支持算法的公有接口
    """

    __metaclass__ = ABCMeta
    @abstractmethod
    def calculate(self):
        pass

class StrategyA(Strategy):
    """
    具体的策略类，封装了具体的算法和行为
    """
    def calculate(self):
        print("calculate A")


class StrategyB(Strategy):
    """
    具体的策略类，封装了具体的算法和行为
    """

    def calculate(self):
        print("calculate B")

class Context(object):
    """
    上下文，维护一个对strategy对象的引用
    """

    def __init__(self, strategy):
        self.__strategy = strategy

    def do_calculate(self):
        self.__strategy.calculate()


if __name__ == '__main__':

    c1 = Context(StrategyA())
    c1.do_calculate()

    c2 = Context(StrategyB())
    c2.do_calculate()
