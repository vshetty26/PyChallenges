tpl = tuple(input("Enter elements of the tuple separated by spaces: ").split())
lst = list(tpl)
lst.append("new_element")
tpl = tuple(lst)
print(tpl)
