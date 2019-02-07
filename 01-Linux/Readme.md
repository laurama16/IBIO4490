



## Your turn

1. What is the ``grep``command?

The grep command is used to search files line by line. This command means global expression print which refers to process each text line to search an specific text or a given file containing a match. According to that, the grep command used on the script is to find the word gray within the sipi_images ignoring the uppercases or the lowercases [1].

2. What is the meaning of ``#!/bin/python`` at the start of scripts?

The meaning of the ``#!/bin/python`` command refers if the script is executable and then the script calls the language mentioned in the command to run the code. So, in this example, calls out the python language coding [2].  

3. Download using ``wget`` the [*bsds500*](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html#bsds500) image segmentation database, and decompress it using ``tar`` (keep it in you hard drive, we will come back over this data in a few weeks).

 First i wrote the command wget and then i put the link mentioned. Then, the download started and lasted for 7 minutes. After that, i decompressed the archive using tar command. For that, i used the specifications '-x' for extract the file, 'z' for extracting the file with gzip, 'v' for displaying progress in the terminal and 'f' to specify the name of the resulting file [3]. 

4. What is the disk size of the uncompressed dataset, How many images are in the directory 'BSR/BSDS500/data/images'?
 
The disk size used for the dataset named as BSR is 73 MB. That information was found using the command 'du' that stands for disk usage. I used the parameters '-sh' where the first one gave me the summary within all files in the directory and the second one gave me the size in units as KB, MB and so on.  

There are 201 train images, 201 test images and 101 validation images. In order to get to this information, i went to each directory and put the command 'ls -l | wc -l'; where the first part of the command refers to list all the files in the current directory. The '-l' parameter tells me the status of the file in the directory. Then, the '| wc-l' command was used to count the lines printed by the ls command, that is because wc means word count and the parameter '-l' provides the line count. Considering that the ls command gives one line of extra information (total), the real number of images is the number given by the previous command minus 1.  

5. What are all the different resolutions? What is their format? Tip: use ``awk``, ``sort``, ``uniq`` 

The resolutions of the images are 481x321 and 321x481. In order to get that information, i looked out for the format and characteristics of the image files using the command 'identify' but first i used the command 'find' to find all the archives. Identify gives a line of information of the archive, so that is why i then used 'awk {print $3}' to print only the third column of information given by 'identify'. After that, i used sort to organize the column with previous results and finally i asked for the repeated lines in a file using 'uniq'. 
The line code used is presented below, 
```find . -name "*.*" -exec identify {} \; | awk '{print $3}' | sort | uniq```
The format of the images is .jpg and the command used to find that information was the latter with the modification of the column printed by 'awk' because the interest here is for the format and not for the size of the image. So, the column 2 was used. 

6. How many of them are in *landscape* orientation (opposed to *portrait*)? Tip: use ``awk`` and ``cut``
 
There are 152 images with landscape orientation (321x481). The code used started with a script. Inside this script, all the images in the directory were found and assigned to a variable. A counter was initialized and a iteration was made over the imager with a for. Using 'identify','awk' and 'cut' it was possible to save two new variables corresponding to the width and height of each image. The first two programs were used, as explained before, to seek within the images the resolution of each one. Then, 'cut' was used to separate the width and heigth in order to save them in two different variables. After that, inside the for a logical question was made to see if the width was greater than the heigth, if this condition was fulfilled the counter was actualized. The code used in this part is presented below.
```
#!/bin/bash

# remove the folder created by a previous run from the script
rm -rf P4

# create output directory
mkdir P4

# find all files whose name end in .tif
images=$(find -name *.jpg)

#iterate over them
count = 0
for im in ${images[*]}
do
   r=$(identify $im | awk '{print $3}' | cut -d "x" -f 1)
   c=$(identify $im | awk '{print $3}' | cut -d "x" -f 2)
   if [ $c -ge $r ]
   then
      echo $im is landscape
      count=$((count+1))
   else
      echo $im is portrait
     fi
 done
 echo $count
```
7. Crop all images to make them square (256x256) and save them in a different folder. Tip: do not forget about  [imagemagick](http://www.imagemagick.org/script/index.php).

First, a new directory was created with 'mkdir' and copy all the files in it (using 'cp'). Then, the modrify program was used. The parameters were '-resize' to give an specific size of the output image and "256x256^!" were the exclamation mark ensures that 256x256 is the only output size. It was necessary to create and copy the files first because 'mogrify' rewrite the output into the input file. The line codes used in this part are presented below.
```mogrify -resize "256x256^!"  *.jpg
find . -name "*.*" -exec identify {} \; | awk '{print $3}' | sort | uniq
```
References
[1] Linux grep command usage with examples. Interserver.net.2018. Available: https://www.interserver.net/tips/kb/linux-grep-command-usage-examples/
[2] Mu\F1oz, A. \BFCu\E1l es la diferencia entre  #!/usr/bin/python y #!/usr/bin/env python?. Stack overflow. Available: https://es.stackoverflow.com/questions/4034/cu%C3%A1l-es-la-diferencia-entre-usr-bin-python-y-usr-bin-env-python
[3] How to compress and extract files using the tar command on Linux. How to geek. 2018. Available:  https://www.howtogeek.com/248780/how-to-compress-and-extract-files-using-the-tar-command-on-linux/


