x=int(input("What's X?:"))
y=int(input("What's y?:"))

if x < y:
    print("x is less than y")
elif x > y: #only if the preceding statement is wrong, the last question is asked.
    print("x is grater than y")
else: #only if both preceding statements wrong, the following case is triggered.
    print ("x is equal to y")