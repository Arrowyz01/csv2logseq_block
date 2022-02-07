# csv2logseq_block
Hello everone, I like notion database that can create from csv, I also like logseq. But I don't like that notion put my data online. So I try to do something with my basic python knowledge to make a "notion-like table database" in logseq. Feel free to try.

This is a Python script that can read csv file and output a markdown file containing logseq block and block properties (from csv data), and a basic query script to generate a table query (like the format in csv file). The goal is to simulate notion table database in logseq. 

Also come with a script to reverse!

I try to fix some problem, also make the usage a little bit easier... maybe not?

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
    

# Image
- expand the major block

<img width="1552" alt="expand" src="https://user-images.githubusercontent.com/85311840/152789156-02c3f1b4-4dda-4d81-a95b-6eb3a2e943ae.png">


- collapse the major block

<img width="1552" alt="fold" src="https://user-images.githubusercontent.com/85311840/152789177-b8b396ff-75c3-4df9-b148-21a9213dee1c.png">


- click one block from query table, you can create new page from \[\[block title]].

<img width="1552" alt="block" src="https://user-images.githubusercontent.com/85311840/152789190-41c0cf25-5cc6-41b6-a849-43abf20f4231.png">

# Video

- csv2md

https://user-images.githubusercontent.com/85311840/152789292-9fb429ba-5155-46cc-9e82-a740b383f294.mov

- md2csv

https://user-images.githubusercontent.com/85311840/152789344-85ef1761-cf9b-4586-b83b-6d915a884098.mov

# Advanced use 
- go to the 'advanced' folder and download a little bit different 'csv2logseq.py'
- add this script into your $PATH (or put it in a folder that already in your $PATH)
- change a little bit in the script
  - 1st line: path to your python
  - 22th line: path to your logseq vault folder
- now you can use the follow command in any folder that contains csv files and the output file will directly appear in your logseq vault folder
    > csv2logseq.py filename.csv "Table name"

