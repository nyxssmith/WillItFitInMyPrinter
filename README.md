# Will It Fit In My Printer

This is a docker based test to see if a print file will fit in your printer.

Put these files at root of directory with `.stl` files in folders, in my case a nested folder structure of ~600 `stl` files that I want to print.

This will output `sorted_sizes.txt` which has the "size" and file path sorted with largest on the bottom.

## "Sizes"?

Sizes in this case are measured in the following way:

- For each file in `os.walk` the current directory

1. Using `os.walk` to get a list of all `.stl` files in the current directory and below
   - Change `stl` to `obj` or anything else `pymesh` can open and it should still work
1. For each `stl` file in the list:
   - Make a dict of `z height in mesh` mapped to `list of points at that height`
   - For each height in the dict:
     - Find the distance that is farthest between all points in the mesh
     - This is done inefficiently, but if I am already waiting ~10 min for a script to run, whats 5 more
   - Use the above process to get the "widest distance between 2 sides of a mesh" for each file. This is what "size" is in the output file.
1. Output a main log to `analysis.txt` and the results to `sorted_sizes.txt`

I have not confirmed but I think the sizes are in `mm`

My printer has print bed of 300mm diameter circle, but I can fit files that are greater than a size of 300 into it by moving the part around and angling it.
