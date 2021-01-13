from __future__ import annotations
from abc import ABC


class Target:
    def text(self) -> str:
        return "Принимаю без _ в начале в первом случае и без точки в конце во втором случае. Все остальное можно."


class Adaptee:
    def specific_text(self) -> str:
        return "_.adasd."


class Adapter_space(Target, Adaptee):
    def text(self) -> str:
        return f"Adapter: {self.specific_text().strip('_')}"


class Adapter_dot(Target, Adaptee):
    def text(self) -> str:
        return f"Adapter: {self.specific_text().strip('.')}"


def client_code(target: "Target") -> None:
    print(target.text(), end="")


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == 'space':
            print("Mediator reacts space:")
            self._component1.do_space()
        elif event == 'dot':
            print("Mediator reacts dot:")
            self._component2.do_dot()


class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_space(self) -> None:
        print("1 компонент убирает _")
        target = Target()
        client_code(target)
        print("\n")

        adaptee = Adaptee()
        print("Не понял:")
        print(f"Было: {adaptee.specific_text()}", end="\n\n")

        print("Но могу понять, если убрать _:")
        adapter = Adapter_space()
        client_code(adapter)


class Component2(BaseComponent):
    def do_dot(self) -> None:
        print("2 компонент убирает . в конце")
        target = Target()
        client_code(target)
        print("\n")

        adaptee = Adaptee()
        print("Не понял")
        print(f"Было: {adaptee.specific_text()}", end="\n\n")

        print("Но могу понять, если убрать . в конце:")
        adapter = Adapter_dot()
        client_code(adapter)


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Убрать _")
    c1.do_space()

    print("\n", end="")

    print("Убрать . в конце")
    c2.do_dot()
