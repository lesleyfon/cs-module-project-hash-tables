
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

    def __str__(self):
        return 'STRING METHOD'

    def insert_node(self, node):

        if self.head == None:
            self.head = node
        else:
            node_exist = self.find(node.key)

            if node_exist[0] == False:

                node.next = self.head
                self.head = node

            else:
                self.update_node(node.key, node.value)

    def find(self, key):

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
                node.value = value

            node = node.next

    def delete_node(self, key):

        if self.head == None:
            return "No Node in the Linked List"

        linklist = self.head
        linklist_copy = self.head

        if linklist.key == key:
            self.head = linklist.next
            return linklist
        while linklist is not None:

            if linklist.key == key:
                linklist_copy.next = linklist.next
                self.head = linklist_copy
                return [1, "Node Deleted", key]

            linklist_copy = linklist
            linklist = linklist.next

        return [0, 'No node to delete']


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here

        self.capacity = capacity
        self.item_count = 0
        self.hash_table = [None] * capacity

        pass

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass
        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        hash_code = key.encode()
        for character in hash_code:
            hash = ((hash * 33) + character)
        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.item_count += 1

        # get the hash Index of where to save the Linked List
        index = self.hash_index(key)
        '''
            1. Hash abd get the index
            2. Check is its empty, then we create a node and add it to the head
            3. If its not empty"
                - Retrive the linked list and save it to a variable
                - create a new instance of the linked list
                - assing the node linked list variable to the head of the newly created linked list
                - call the insert method and pass in the key and value
        '''

        if self.hash_table[index] == None:

            self.hash_table[index] = HashTableEntry(key, value)
        else:

            hash_table_li = self.hash_table[index]

            li = LinkedList()
            li.head = hash_table_li
            li.insert_node(HashTableEntry(key, value))

            self.hash_table[index] = li.head

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        if(index == None):
            return None
        else:
            hash_table_li = self.hash_table[index]

            li = LinkedList()
            li.head = hash_table_li
            return li.find(key)[2]

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.item_count += 1

        index = self.hash_index(key)

        if(self.hash_table[index] == None):
            print("Key is not found")
        else:
            hash_table_li = self.hash_table[index]

            li = LinkedList()
            li.head = hash_table_li

            li.delete_node(key)
            self.hash_table[index] = li.head

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        all_key_value = []

        for i in range(len(self.hash_table)):

            head = self.hash_table[i]

            while head:
                all_key_value.append((head.key, head.value))
                head = head.next

        self.capacity = new_capacity
        self.hash_table = [None] * new_capacity

        for i in range(len(all_key_value)):
            index = self.hash_index(all_key_value[i][0])
            if index:
                self.put(all_key_value[i][0], all_key_value[i][1])

        del all_key_value


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
