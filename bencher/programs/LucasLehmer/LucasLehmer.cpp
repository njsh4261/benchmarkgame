#include <iostream>
#include <vector>

using namespace std;

const int MIN_MERSENNE = 3;
const int MAX_MERSENNE = 64;

void usage(){
    cout << "usage: ./LucasLehmer [iteration_number]" << endl;
    cout << "iteration number should be between 3 and 64" << endl;
    exit(0);
}

void calculate()

int main(int argc, char** argv){
    if(argc != 2) {
        usage();
    }

    int iter_num = atoi(argv[1]);
    if(iter_num < MIN_MERSENNE || iter_num > MAX_MERSENNE) {
        usage();
    }

    unsigned long long s;

    for(int i=0; i<)
}