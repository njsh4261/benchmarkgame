import random as rnd

def array_generate(filename, size):
    new_file = open(filename, 'w')

    first_line = "%d\n" % size
    new_file.write(first_line)
    for _ in range(1, size):
        new_file.write(str(rnd.randint(0, size)) + " ")
    new_file.write(str(rnd.randint(0, size)))

    new_file.close()