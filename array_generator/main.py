import sys
import src.array_generate as ag

OUTPUT_LOCATION_DEFAULT = "./output/"

def main():
    if len(sys.argv) != 5:
        print("usage: python main.py [file_type] [file_name] [array_size] [num_of_array_to_generate]")
        sys.exit()
    
    file_type = sys.argv[1]
    file_name = sys.argv[2]
    size = int(sys.argv[3])
    generate_iter = int(sys.argv[4])

    if file_type == 'array':
        for i in range(1, generate_iter+1):
            ag.array_generate(
                file_name + "_" + str(i) + ".txt",
                size
            )
    elif file_type == 'graph':
        pass

if __name__ == "__main__":
    main()