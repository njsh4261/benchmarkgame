#!/bin/bash
gen_prog="./quicksort_input_generate.py"
bench_loc="./bencher/bin/bencher.py"

python "${gen_prog}"
python2.7 "${bench_loc}"