"""
观察者模式：

定义类一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象，这个主题在发生变化时，
    会通知所有观察者，使得他们能够自动更新自己

- 他是基于事件的UI框架中常用的设计模式，也是MVC模式的重要部分
"""

from abc import ABCMeta, abstractmethod

class Subject(object):
    """
    把所有对观察者对象的引用保存在一个聚集里
    每个主题都可以有任意数量的观察者

    抽象主题提供了接口增加，删除观察者对象
    """
    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for o in self.__observers:
            o.update()


class ConcreteSubject(Subject):
    """
    具体主题，将有关状态存入具体观察者对象
    在具体主题的内部状态改变时， 给所有登记过的观察者发出通知
    """
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

class Observer(object):
    """
    抽象观察者，为所有具体观察者定义接口，在得到主题的通知时更新自己
    """
    __metaclass__ = ABCMeta
    @abstractmethod
    def update(self):
        pass

class ConcreteObserver(Observer):
    """
    具体观察者，实现抽象观察者所要求的更新接口
    以使本身的状态与主题的状态协调
    """

    def __init__(self, subject, name):
        self.subject = subject
        self.name = name
        self.objserver_staus = None

    def update(self):
        self.objserver_staus = self.subject.status
        print("the observer: %s status change to %s" %(self.name, self.objserver_staus) )


if __name__ == '__main__':
    s = ConcreteSubject()

    s.attach(ConcreteObserver(s, "X"))
    s.attach(ConcreteObserver(s, "Y"))
    s.attach(ConcreteObserver(s, "Z"))

    s.status = "A"
    s.notify()

    s.status = "B"
    s.notify()
