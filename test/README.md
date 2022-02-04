# What you need to prepare
- python3
    > which python
    > python -V
- make sure you have pandas installed, use follow command to check
    > pip list
- or install pandas
    > pip install pandas
- find your logseq vault

# quick start
- convert '.csv' to '.md' with logseq block structures and a query table with "Table name".

    - download and put 'csv2logseq.py' in the same folder as '.csv' file you want to convert, use shell and 'cd' to that folder.
    - type the command, you need to change to your '.csv' filename and your "Table name". Please note that: the "" is necessary for the table name of query table.
        > python csv2logseq.py filename.csv "Table name"
    - it will read the '.csv', and output a '.md' file with logseq block/block properties structrue in the same folder. 
    - then you can copy the output '.md' file to your logseq vault (ie. in "pages" folder). 

- convert '.md' with logseq block structures to '.csv'.

    - if you want to reverse the process, ie, read '.md' file with logseq block/block properties structrue and output a '.csv' file, please use 'logseq_block2csv.py'. 
    - just download and put it in the same folder as the '.md' file you want to convert, use shell and 'cd' to that folder.
    - type the command, you need to change to your '.md' filename.
        > python logseq_block2csv.py filename.md
    - the script will output the '.csv' file in the same folder as well. 
    - but please note that: the script is very sensitve to the format in '.md' file, you'd better make the '.md' file as neat as possible.
