import time
import codecs


def codecs_rewrite():
    start_time = time.time()

    with codecs.open("./codecs_rewrite.txt", "w", "utf-8") as cod:
        for i in range(1000000):
            cod.write(str(i))

    end_time = time.time()
    run_time = end_time - start_time
    return run_time


def open_rewrite():
    start_time = time.time()

    with open("./open_rewrite.txt", mode="w", encoding="utf-8") as ope:
        for i in range(1000000):
            ope.write(str(i))

    end_time = time.time()
    run_time = end_time - start_time
    return run_time


print("---------------------------------")
print("codecs:            || open:")
for _ in range(5):
    print(codecs_rewrite(), end=" || ")
    print(open_rewrite())
print("---------------------------------")

