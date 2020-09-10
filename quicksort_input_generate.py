import random
import os.path

def array_generate(filename, size):
    new_file = open(os.path.join(os.getcwd(), "bencher/tmp/quicksort", filename), 'w')

    first_line = "%d\n" % size
    new_file.write(first_line)
    for _ in range(1, size):
        new_file.write(str(random.randint(0, size)) + " ")
    new_file.write(str(random.randint(0, size)))

    new_file.close()

SIZE = 20000000
FILENAME = "quicksort-input%d.txt" % SIZE
array_generate(FILENAME, SIZE)
