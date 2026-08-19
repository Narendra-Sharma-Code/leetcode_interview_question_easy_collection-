# Recursion: Function calling itself is called recursion
import sys
print(sys.setrecursionlimit(30))
from time import sleep

count = 1
def greet():
    global count
    print(f"Hello {count}")
    sleep(0.1)
    count += 1
    greet()

# greet()
