def forLoops():
    print("---------\n")
    for x in range(3):
        print("this is a basic \"For in range(3)\" -> ",x)

    print("---------\n")
    for x in range(2,4):
        print("this is a \"For in range(2,4)\" starting on 2, going to 4 -> ", x)
    
    print("---------\n")
    for x in range(1,6,2):
        print("this is a \"For in range(1,6,2)\" starting on 1, going to 6, incrementing 2 -> ", x)
    
    print("---------\n")

def forEachLoops():
    fruits = ["apple", "lasagna", "pizza"]

    for fruit in fruits:
        print(fruit)


forLoops()
forEachLoops()