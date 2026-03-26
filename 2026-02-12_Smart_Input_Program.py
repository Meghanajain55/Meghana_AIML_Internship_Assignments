# Smart Input Program

# Taking inputs from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age
if age < 13:
    category = "a Child"
elif age < 20:
    category = "a Teenager"
elif age < 60:
    category = "an Adult"
else:
    category = "a Senior"

# Printing personalized message
print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are {category}.")
print(f"It's awesome that you enjoy {hobby}!")