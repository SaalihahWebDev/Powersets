print("Welcome to power set maker")
input_string = input("Enter 3 numbers separated by commas (like 1,2,3): ")
items = input_string.split(",")
# Strip any whitespace
items = [item.strip() for item in items]
power_set = [[]]
print("\nLet's build the power set step by step")
for item in items:
    print(f"\nAdding item: {item}")
    new_subsets = []
    for subset in power_set:
        new_subset = subset + [item]
        print(f"Adding {item} to {subset} -> {new_subset}")
        new_subsets.append(new_subset)  
power_set.extend(new_subsets)
print("\nFinal power set:")
for subset in power_set:
    print(subset)
print("\nYay! We made the powers of 2")