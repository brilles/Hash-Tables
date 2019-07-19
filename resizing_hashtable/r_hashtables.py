class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)
    return hash % max


def hash_table_insert(hash_table, key, value):
    # store index
    index = hash(key, hash_table.capacity)

    # create LinkedPair with key/value
    item = LinkedPair(key, value)

    # store the pair at the index
    stored_pair = hash_table.storage[index]

    # if there is no collision
    if stored_pair is None:
        # insert
        hash_table.storage[index] = item
        return

    # if there is a collision
    else:
        # if the keys are the same => overwrite it
        if stored_pair.key == key:
            stored_pair.value = value
            return
        else:
            # traverse the LL
            while stored_pair.next is not None:

                # re-assign the stored_pair
                stored_pair = stored_pair.next

                # if the keys are the same => overwrite it
                if stored_pair.key == key:
                    stored_pair.value = value
                    return
            # if not, append
            stored_pair.next = item
            return


# '''

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # store index
    index = hash(key, hash_table.capacity)

    # store the pair at the index
    stored_pair = hash_table.storage[index]

    # if not found
    if stored_pair is None:
        print(f"Warning: no item at that index, nothing removed")
        return

    # only one node in LL (n -> None)
    if stored_pair.next is None and stored_pair.key == key:
        hash_table.storage[index] = None
        return None

    # store nth stored_pair
    nth_sp = hash_table.storage[index].next

    # traverse the LL
    while nth_sp is not None:

        if nth_sp.key is key:

            # reassign the LL node
            stored_pair.next = nth_sp.next
            return

        # keep traversing
        stored_pair = nth_sp
        nth_sp = nth_sp.next

# '''
# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    # store index
    index = hash(key, hash_table.capacity)

    # store the pair at the index
    stored_pair = hash_table.storage[index]

    # traverse the LL
    while stored_pair is not None:

        if stored_pair.key is key:

            return stored_pair.value
        # keep traversing
        stored_pair = stored_pair.next
    return None


def hash_table_resize(hash_table):
    # create new hash table with double the capacity
    resized_HT = HashTable(hash_table.capacity * 2)

    # iterate first HT and insert into second
    for i in hash_table.storage:
        stored_pair = i

        # traverse LL
        while stored_pair is not None:

            # insert
            hash_table_insert(resized_HT, stored_pair.key, stored_pair.value)

            stored_pair = stored_pair.next
    return resized_HT


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
