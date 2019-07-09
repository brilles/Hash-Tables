class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.count = 0
        self.storage = [None] * capacity


def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)
    return hash % max


def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    stored_pair = hash_table.storage[index]

    if hash_table.storage[index] is not None:
        if pair.key != stored_pair.key:
            print(f"Warning, index at {str(index)} is not empty")

    hash_table.storage[index] = pair


def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    if (hash_table.storage[index] is None or
            hash_table.storage[index].key != key):
        print(f"Unable to remove item with key {key}")
    else:
        hash_table.storage[index] = None


def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value

    print(f"Unable to find value with key {key}")
    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")
    # breakpoint() ht -> dir(ht) -> ht.storage
    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
