# Use
- put csv2logseq_local.py in the same folder as csv file you want to convert. it will read the csv, and output a md file with logseq block/block properties structrue in the same folder
    > python csv2logseq_local.py filename.csv
- if you want to reverse the process, ie, read md file with logseq block/block properties structrue and output a csv, please use logseq_block2csv.py. just put it in the same folder as the md file you want to convert, the script will output the csv file in the same folder as well. but please note that: the script is very sensitve to the format in md file, you'd better make the md file as neat as possible
    > python logseq_block2csv.py filename.md
