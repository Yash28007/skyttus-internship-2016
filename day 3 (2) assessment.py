numbers = (10, 20, 30, 40, 50)
print(numbers)

print(numbers[2])

a, b, c, d, e = numbers
print(a, b, c, d, e)

fruits = {"apple", "banana", "mango", "orange", "grape"}
print(fruits)

fruits.add("pineapple")
print(fruits)

fruits.remove("banana")
print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))

print(set1.intersection(set2))

print(set1.issubset(set2))

duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(duplicate_list)
print(unique_set)

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Initial dictionary:", students)

students["David"] = 88
print("After adding new key-value:", students)

del students["Charlie"]
print("After deleting a key-value:", students)

extra_students = {"Eva": 92, "Frank": 80}
merged_dict = students | extra_students
print("Merged dictionary:", merged_dict)

key_to_check = "Alice"
print("Key exists:", key_to_check in merged_dict)

text = "apple banana apple orange banana apple"
words = text.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequency:", word_freq)

max_key = max(merged_dict, key=merged_dict.get)
print("Key with maximum value:", max_key)

reversed_dict = {v: k for k, v in merged_dict.items()}
print("Reversed dictionary:", reversed_dict)

merged_dict["Alice"] = 95
print("After updating value:", merged_dict)

tuple_list = [("Math", 90), ("Science", 85), ("English", 88)]
tuple_dict = dict(tuple_list)
print("Dictionary from tuples:", tuple_dict)
