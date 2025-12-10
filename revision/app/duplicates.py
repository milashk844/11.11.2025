def has_duplicates(your_list: list[int | float | str | bool]) -> bool:
    return len(your_list) != len(set(your_list))\

print(has_duplicates([1, 2, 3]))
print(has_duplicates([1, 2, 2, 3]))
# false якщо немає дублікатів