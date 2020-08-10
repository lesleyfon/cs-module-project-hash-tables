class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, node):
        '''
            Steps:
                If head is empty, 
                    - add node to the head
                else:
                    - Check if the node exist using
                    - If it exist call the update method to update that  node
                    - else:
                        insert node at head

        '''

        if self.head == None:
            self.head = node
        else:
            # Checks to see if a node exist in the linked list. If so then we want to update that node
            node_exist = self.find(node.key, node.value)

            if node_exist[0] == False:
                # if the node doesnt exist we want to add the node to the head node
                node.next = self.head
                self.head = node
            else:
                # If the node exist we want to update the node at that spot using the new node value
                self.update(node.key, node.value)

    def find(self, key, value):
        '''
            If head is none then we want to return a list with False, None, None as valuses of the node
            else:
                search through the node looking for the key that matches in the linkedlist
        '''
        if self.head == None:
            return [False, None, None]

        node = self.head
        while node != None:

            if node.key == key:
                return[True, node.key, node.value]
            else:
                node = node.next

        return [False, None, None]

    def update(self, key, value):

        node = self.head

        while node:

            if node.key == key:
                # If the keys match then we want to update the value
                node.value = value

            node = node.next

    def delete(self):
        pass

    def contains(self, key):
        if self.head == None:
            return False
        node = self.head

        while node:
            if node.key == key:
                return True
            node = node.next
        return False


linklist = LinkedList()


def test_contains():
    linklist.insert_node(HashTableEntry(1, "Hello"))
    linklist.insert_node(HashTableEntry(2, "World"))
    linklist.insert_node(HashTableEntry(5, "Welcome"))
    linklist.insert_node(HashTableEntry(10, "Isnt this amazing"))

    print(linklist.find(5, "some"))
    linklist.insert_node(HashTableEntry(5, "New Welcome Welcome"))
    print(linklist.find(5, "some"))


test_contains()


# def test_delete_node():
#     linklist.insert_node(10)
#     linklist.insert_node(20)
#     assertEqual(linklist.delete_node(), 10)
#     assertFalse(linklist.contains(10))
#     assertEqual(linklist.delete_node(), 20)
#     assertFalse(linklist.contains(20))

#     linklist.insert_node(10)
#     assertEqual(linklist.delete_node(), 10)
#     assertIsNone(linklist.head)
#     assertIsNone(linklist.tail)
#     assertIsNone(linklist.delete_node())

# def test_get_max():
#     .assertIsNone(.list.get_max())
#     .list.insert_node(100)
#     .assertEqual(.list.get_max(), 100)
#     .list.insert_node(55)
#     .assertEqual(.list.get_max(), 100)
#     .list.insert_node(101)

#     .assertEqual(.list.get_max(), 101)
