#frag die userin nach ihrem namen
name = input("what's your Name?: ").strip().title()

#teile den namen der userin in vor- & nachnamen
first, last=name.split()

#sag hallo zur userin
print(f"Hello, {first}!")