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

<img width="1440" alt="截屏2022-01-31 21 55 16" src="https://user-images.githubusercontent.com/85311840/151871789-4449e4da-8f4d-424f-859e-0db62de4ae95.png">

- collapse the major block

<img width="1440" alt="截屏2022-01-31 21 55 05" src="https://user-images.githubusercontent.com/85311840/151872053-3db78d77-0038-4e1d-8d79-37ca16bab658.png">

- click one block from query table, you can create new page from \[\[block title]].
<img width="1440" alt="截屏2022-01-31 21 58 55" src="https://user-images.githubusercontent.com/85311840/151872192-809fcd29-dadb-4fbf-968d-4900e38d0b08.png">

# Advanced use 
- go to the 'advanced' folder and download a little bit different 'csv2logseq.py'
- add this script into your $PATH (or put it in a folder that already in your $PATH)
- change a little bit in the script
  - 1st line: path to your python
  - 22th line: path to your logseq vault folder
- now you can use the follow command in any folder that contains csv files and the output file will directly appear in your logseq vault folder
    > csv2logseq.py filename.csv "Table name"

