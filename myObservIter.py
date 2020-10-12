from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator


class Subject(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state = None
    _observer = None

    def attach(self, observer) -> None:
        print('Подписан')
        self._observer = observer

    def notify(self, collection) -> None:
        self._observer.update(collection)

    def some_business_logic(self) -> None:
        collection = Book()
        collection.add_item("book1")
        collection.add_item("Harry Potter")
        collection.add_item("book3")

        self.notify(collection)


class Observer(ABC):
    @abstractmethod
    def update(self, collection) -> None:
        pass


class PoterObserver(Observer):
    def update(self, collection) -> None:
        for elem in collection:
            print(elem)
            if elem == 'Harry Potter':
                print('Итератор на Harry Potter')


class BookIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class Book(Iterable):
    def __init__(self, collection = []) -> None:
        self._collection = collection

    def __iter__(self) -> BookIterator:
        return BookIterator(self._collection)

    def get_reverse_iterator(self) -> BookIterator:
        return BookIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


if __name__ == "__main__":

    subject = ConcreteSubject()

    observer_poter = PoterObserver()
    subject.attach(observer_poter)
    subject.some_business_logic()
