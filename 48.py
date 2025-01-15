d = {"a": 1, "b": 2, "c": 3}
if len(d.values()) == len(set(d.values())):
    inverted = {v: k for k, v in d.items()}
    print(inverted)
else:
    print("Values are not unique, inversion not possible")
