class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, node):
        self.next = node

    def is_tail(self):
        return self.next is None

    def is_equal_to(self, value):
        return self.value == value

    def to_string(self):
        string = str(self.value)
        if self.is_tail():
            return string

        return string + '->' + self.next.to_string()


class DoublyLinkedList(LinkedList):

    def __init__(self, value):
        super().__init__(
            value=value
        )
        self.prev = None

    def set_prev(self, node):
        self.prev = node

    def is_head(self):
        return self.prev is None

    def to_string_next(self):
        return self.to_string()

    def to_string_prev(self):
        string = str(self.value)
        if self.is_head():
            return string

        return string + '->' + self.prev.to_string_prev()

    def add_right(self, value):
        new_node = DoublyLinkedList(value)
        if self.is_tail():
            new_node.set_prev(self)
            self.set_next(new_node)
        else:
            new_node.set_prev(self)
            new_node.set_next(self.next)

            self.next.set_prev(new_node)
            self.set_next(new_node)

    def add_left(self, value):
        new_node = DoublyLinkedList(value)
        if self.is_head():
            new_node.set_next(self)
            self.set_prev(new_node)
        else:
            new_node.set_next(self)
            new_node.set_prev(self.prev)

            self.prev.set_next(new_node)
            self.set_prev(new_node)


def list_to_dllist(a_list):
    head = DoublyLinkedList(a_list[0])
    tail = head
    for element in a_list[1:]:
        new_node = DoublyLinkedList(element)
        tail.set_next(new_node)
        new_node.set_prev(tail)
        tail = tail.next
    return head, tail


def list_to_llist(a_list):
    head = DoublyLinkedList(a_list[0])
    tail = head
    for element in a_list[1:]:
        new_node = DoublyLinkedList(element)
        tail.set_next(new_node)
        tail = tail.next
    return head, tail


def test_llists():
    r = ['please', 'sit', 'spot', '.', 'sit', 'spot', ',', 'sit', '.', 'spot', 'here', 'now', 'here', '.']
    h, t = list_to_dllist(r)

    print('forward  :', h.to_string_next())
    print('backward :', t.to_string_prev())

    h.add_right('COUCOU')
    t.add_right('THISISTHETAIL')
    t = t.next

    print('forward  :', h.to_string_next())
    print('backward :', t.to_string_prev())

    h.add_left('THISISNEWHEAD')
    t.add_left('XXXX')
    h = h.prev

    print('forward  :', h.to_string_next())
    print('backward :', t.to_string_prev())


if __name__ == '__main__':
    test_llists()
