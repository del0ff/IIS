from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List
from queue import Queue


class GraphIterator(Iterator):
    _position: int = None

    def __init__(self, collection: TopCollection) -> None:
        self._collection = collection
        self._position = 0
        self.visited = []
        self.queue = []
        self.node = 'A'
        self.target_node = 'F'

    def __next__(self):
        
        global queue
        self.visited.append(self.node)
        self.queue.append(self.node)
        while self.queue:
            try:
                value = self._collection[self._position]
                self._position += 1
            except IndexError:
                raise StopIteration()

            try:
                s = self.queue.pop(0)
            except:
                pass
            else:
                print (s, end=' ')
                if s == self.target_node:
                    print('Найденная вершина')
                    raise StopIteration()

                for neighbour in value.split(' '):
                    if neighbour not in self.visited:
                        self.visited.append(neighbour)
                        self.queue.append(neighbour)


class GraphIterator2(Iterator):
    _position: int = None

    def __init__(self, collection: TopCollection) -> None:
        self._collection = collection
        self._position = 0
        self.queue=Queue()
        self.visited_nodes={}
        self.beg_node = 'A'
        self.target_node = 'F'

    def __next__(self):
        
        self.queue.put(self.beg_node)
        self.visited_nodes={self.beg_node}
        while True:
            try:
                value = self._collection[self._position]
                self._position += 1
            except IndexError:
                raise StopIteration()
            u = self.queue.get()
            if len(value) > 0:
                print("Обходим узел", value)
                for node in value.split(' '):
                    print(" -- Смотрим ребро", node)
                    if not(node in self.visited_nodes):
                        print("   ---- Узел", node,"добавили в очередь")
                        self.visited_nodes.add(node)
                        self.queue.put(node)
                    if node == self.target_node:
                        print("Поиск успешно завершен")
                        raise StopIteration()
                

class TopCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> GraphIterator:
        return GraphIterator(self._collection)

    def add_item(self, item: set):
        self._collection.append(item)


class TopCollection2(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> GraphIterator2:
        return GraphIterator2(self._collection)

    def add_item(self, item: set):
        self._collection.append(item)


if __name__ == "__main__":
    collection = TopCollection()

    collection.add_item('B C')
    collection.add_item('D E')
    collection.add_item('F')
    collection.add_item('')
    collection.add_item('F')
    collection.add_item('')

    print('A->[B,C]\nB->[D,E]\nC->[F]\nD->[]\nE->[F]')
    print('Обход графа в ширину')
    print('\n'.join(collection))

    collection2 = TopCollection2()

    collection2.add_item('B C')
    collection2.add_item('D E')
    collection2.add_item('F')
    collection2.add_item('')
    collection2.add_item('F')
    collection2.add_item('')

    print('Обход графа в глубину')
    print('\n'.join(collection2))
            