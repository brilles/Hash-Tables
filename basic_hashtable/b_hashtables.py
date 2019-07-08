

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity

# '''
# Fill this in.
# Research and implement the djb2 hash function
# [keys] -> | hash function | -> [hashes]
# [John Smith] -> HF -> [02]
# '''


def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + max
    hash = max % hash - 1
    return hash

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''


def hash_table_insert(hash_table, key, value):
    hash_key = hash(key, len(hash_table.array))
    if hash_table.array[hash_key] is not None:
        print("WARNING: overwriting a value with a different key")
    hash_table.array[hash_key] = value

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    key = hash(key, len(hash_table.array))
    if hash_table.array[key] is None:
        print("WARNING: attempting to remove a value that isn't there")
    hash_table.array[key] = None
# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    if hash_table.array[hash(key, len(hash_table.array))] is None:
        return None
    else:
        return hash_table[key]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
