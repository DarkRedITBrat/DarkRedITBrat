# Slicing
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print("Get the characters from position 2 to position 5 (not included):")
print(b[2:5])
print()

# Slice From the Start
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print("Get the characters from the start to position 5 (not included):")
print(b[:5])
print()

#Slice To the End
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print("Get the characters from position 2, and all the way to the end:")
print(b[2:])
print()

# Negative Indexing
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print("""Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):""")
print(b[-5:-2])
print()