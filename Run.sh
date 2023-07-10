#!/bin/bash
set -ex
# build and run docker image
image_name="stl_sizer"

docker build -t $image_name .

docker run --rm -it -v $(pwd):/local $image_name

cat analysis.txt | cut -d: -f2 | sort -n >sorted_sizes.txt
