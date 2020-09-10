#!/bin/bash
gen_quicksort="./quicksort_input_generate.py"
gen_floydwarshall="./floydwarshall_input_generate.py"
bench_loc="./bencher/bin/bencher.py"
quicksort_input_size=20000000
floyd_warshall_array=(1000 1500 2000)

python "${gen_quicksort}" "${quicksort_input_size}"
for i in "${floyd_warshall_array[@]}"; do
	python "${gen_floydwarshall}" $i
done
python2.7 "${bench_loc}"