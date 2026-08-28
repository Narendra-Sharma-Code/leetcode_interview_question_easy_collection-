from threading import Thread
from time import sleep,time
from multiprocessing import process
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print(f"Hello {i+1}")
#             sleep(0.2)
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print(f"Hi {i+1}")
#             sleep(0.5)
# if __name__ == "__main__":
#     t1 = Hello()
#     t2 = Hi()
#     t1.start()
#     t2.start()
# def Helo():
#         for i in range(5):
#             print(f"Hallo {i+1}")
#             sleep(0.2)
# def hi():
#         for i in range(5):
#             print(f"Hii {i+1}")
#             sleep(0.5)
# obj1 = Thread(target= Helo)
# obj2 = Thread(target= hi)
# obj1.start()
# obj2.start()

def downloading(filename):
    print(f"Downloading {filename}...")
    sleep(0.5)
    print(f"{filename} downloaded!")

if __name__ == "__main__":
    files = ["video.mp4","img.png","data.csv"]
    for f in files:
        start = time()
        t1 = Thread(target=downloading, args=(f,))
        t2 = Thread(target=downloading, args=(f,))
        end = time()
        diff = end -start
        print(f"parellel {diff}")
        # t1.start()
        # t2.start()
        # t1.join()
        # t2.join()
        print("Bye")

# files = ["video.mp4","img.png","data.csv"]
# for f in files:
#     t3 = downloading(f)
