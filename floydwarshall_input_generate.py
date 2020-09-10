import random
import math
import os.path
import sys

def random_graph(filename, node_num, density):
    new_file = open(os.path.join(os.getcwd(), "bencher/tmp/floydwarshall", filename), 'w')
    new_file.write("%d\n" % node_num)

    edge_count = int(node_num*density)
    for i in range(node_num):
        random_edge_count = int(random.gauss(node_num/2, math.sqrt(node_num)))
        if random_edge_count > node_num:
            random_edge_count = node_num
        elif random_edge_count < 1:
            random_edge_count = 1
        select_vertex = sorted(random.sample(range(node_num), random_edge_count))
        str_list = []
        for j in range(node_num):
            if j in select_vertex and i != j:
                str_list.append("%d " % random.randint(1, node_num))
            elif i == j:
                str_list.append("%d " % 0)
            else:
                str_list.append("%d " % (sys.maxsize/2))
        edge_list = ''.join(str_list).strip()+"\n"
        new_file.write(edge_list)

def main():
    if len(sys.argv) != 2:
        print("usage: python floydwarshall_input_generate.py [number_of_vertices]")
    else:
        node_num = int(sys.argv[1])
        density = 0.6
        random_graph("floydwarshall-input%d.txt" % (node_num), node_num, density)

if __name__ == "__main__":
    main()