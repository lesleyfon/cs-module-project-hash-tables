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
                self.update_node(node.key, node.value)

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

    def update_node(self, key, value):

        node = self.head

        while node:

            if node.key == key:
                # If the keys match then we want to update the value
                node.value = value

            node = node.next

    def delete_node(self, key):
        if self.head == None:
            return "No Node in the Linked List"

        linklist = self.head
        linklist_copy = self.head

        while linklist:

            if linklist.key == key:
                '''
                    If we find the node we want to delete:
                        1. Set the Linked List copy at that node to look at the next node in the original linked list
                '''
                linklist_copy = linklist.next
                self.head = linklist_copy
                return [1, "Node Deleted"]

            linklist_copy = linklist
            linklist = linklist.next

        return [0, 'No node to delete']


# def test_contains():
#     linklist.insert_node(HashTableEntry(1, "Hello"))
#     linklist.insert_node(HashTableEntry(2, "World"))
#     linklist.insert_node(HashTableEntry(5, "Welcome"))
#     linklist.insert_node(HashTableEntry(10, "Isnt this amazing"))

#     print("Find 5, Should Return True", linklist.find(5, "some"))
#     linklist.insert_node(HashTableEntry(5, "New Welcome Welcome"))
#     print("Find 5, Should Return True", linklist.find(5, "some"))

#     linklist.insert_node(HashTableEntry(20, "Added new Node"))
#     print("Find 20, Should Return True", linklist.find(20, "Some"))
#     print("Delete 10, Should Return 1", linklist.delete_node(10), 10)
#     print("Delete 10, Should Return False", linklist.find(10, "Some"))
#     print("Delete 20, Should Return 1", linklist.delete_node(20), 20)
#     print("Find 5, Should Return False", linklist.find(20, "Some"))


# test_contains()
