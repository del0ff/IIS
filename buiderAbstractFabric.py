from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_wheels(self) -> None:
        pass

    @abstractmethod
    def produce_engine(self) -> None:
        pass

    @abstractmethod
    def produce_body(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Model()

    @property
    def product(self) -> Model:
        product = self._product
        self.reset()
        return product

    def produce_wheels(self) -> None:
        self._product.add("Добавлены колеса")

    def produce_engine(self) -> None:
        self._product.add("Добавлен двигатель")

    def produce_body(self) -> None:
        self._product.add("Добавлен кузов")


class Model():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Сделано: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_full_model(self) -> None:
        self.builder.produce_body()
        self.builder.produce_engine()
        self.builder.produce_wheels()


class AbstractFactory(ABC):
    @abstractmethod
    def create_model(self) -> AbstractModel:
        pass


class SmallModel(AbstractFactory):
    def create_model(self) -> SmallModelProduct:
        SmallModelProduct.useful_function(self)


class RealModel(AbstractFactory):
    def create_model(self) -> RealModelProduct:
        RealModelProduct.useful_function(self)


class AbstractModel(ABC):
    @abstractmethod
    def useful_function(self) -> str:
        pass


class SmallModelProduct(AbstractModel):
    def useful_function(self) -> str:
        director = Director()
        builder = ConcreteBuilder1()
        director.builder = builder

        print("Сборка игрушечной модели машины.")
        director.build_full_model()
        builder.product.list_parts()

        builder.produce_wheels()
        builder.produce_engine()
        builder.produce_body()

        print("\n\tИгрушечная модель машины готова.")


class RealModelProduct(AbstractModel):
    def useful_function(self) -> str:
        director = Director()
        builder = ConcreteBuilder1()
        director.builder = builder

        print("Сборка реального автомобиля.")
        director.build_full_model()
        builder.product.list_parts()

        builder.produce_wheels()
        builder.produce_engine()
        builder.produce_body()

        print("\n\tРеальный автомобиль собран.")


def client_code(factory: AbstractFactory) -> None:
    product = factory.create_model()


if __name__ == "__main__":
    client_code(SmallModel())
    client_code(RealModel())
