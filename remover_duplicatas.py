some_list = ['a', 'b','c','b','d','m','n','n']

duplicates = []
for _string in some_list:
  if some_list.count(_string) > 1:
    duplicates.append(_string)
    some_list.remove(_string)
print(sorted(some_list), "\n", sorted(duplicates))