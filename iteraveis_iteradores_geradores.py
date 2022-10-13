list_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_test = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
dictionary = {"key": "1",
              "key2": "2",
              "key3": "3",
              "key4": "4",
              "key5": "5",
              "key6": "6",
              "key7": "7",
              "key8": "8",
              "key9": "9",
              "key10": "10"}

print("para ser um iterável basicamente o objeto tem de ter o método '__iter__'  e o método '__getitem__'")
print("uma lista é iterável?", hasattr(list, '__iter__'))
print("um tupla é iterável?", hasattr(tuple, '__iter__'))
print("um dicionário é iterável?", hasattr(dictionary, '__iter__'))
