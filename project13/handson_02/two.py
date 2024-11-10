import one

print("TOP LEVEL TWO.py")
one.func()

if __name__ == "__main__":
    print("TWO.py being run directly")
else:
    print("TWO is being imported")