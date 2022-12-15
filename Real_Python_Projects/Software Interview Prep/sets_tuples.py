_set = set()
_set.add("hello")
_set.add("hi")
_set.add("yo")
_set.add("hey")
_set.add("whats good")
#print(_set)

if "hello" in _set:
    print("hello is in the set")
else:
    print("hello is not in the set")

tup = ("1", "2", 3)
print(tup)
tup = (1, 2, 3, 4)
print(tup)
print(type(tup))

if 1 in tup:
    print("1 in tup")
else:
    print("1 not in tup")

