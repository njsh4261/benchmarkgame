import random
import os.path
import sys

def array_generate(filename, size):
    new_file = open(os.path.join(os.getcwd(), "bencher/tmp/quicksort", filename), 'w')

    first_line = "%d\n" % size
    new_file.write(first_line)
    for _ in range(1, size):
        new_file.write(str(random.randint(0, size)) + " ")
    new_file.write(str(random.randint(0, size)))

    new_file.close()

def main():
    if len(sys.argv) != 2:
        print("usage: python quicksort_input_generate.py [array_size]")
    else:
        size = int(sys.argv[1])
        array_generate("quicksort-input%d.txt" % size, size)

if __name__ == "__main__":
    main()
