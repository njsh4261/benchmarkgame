#!/bin/bash
tmp_loc="./bencher/tmp/"
benchmarks=("fibonacci" "floydwarshall" "quicksort")

for dir in "${benchmarks[@]}"; do
	rm -r "${tmp_loc}${dir}"
    mkdir "${tmp_loc}${dir}"
done

./run.sh