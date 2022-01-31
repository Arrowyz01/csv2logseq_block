# csv2logseq_block
Hello everone, I like notion database that can create from csv, I also like logseq. But I don't like that notion put my data online. So I try to do something with my basic python knowledge to make a "notion-like table database" in logseq. Feel free to try.

This is a Python script that can read csv file and output a markdown file containing logseq block and block properties (from csv data), and a basic query script to generate a table query (like the format in csv file). The goal is to simulate notion table database in logseq. 

# What you need to prepare
- python3 and its path
- make sure you have pandas installed
- find your logseq path

# What you need to change in csv2logseq.py
- 1st line: path to your python
- 15th line: path to your logseq
- 47th line: query table name

# How to use this script
- download csv2logseq.py
- change what you need to change in csv2logseq.py
- cd to you csv folder

- If you add this script into your $PATH (or put it in a folder that already in your $PATH), you can direct use follow code, the filename.md will appear in your logseq/pages

  > csv2logseq.py filename.csv

- If you don't want to add it to you $PATH, you can follow code, the filename.md will appear in your logseq/pages

  > python /path/to/csv2logseq.py filename.csv

- another option: use test/csv2logseq_local.py that will generate filename_local.md in current folder

  > python /path/to/csv2logseq_local.py filename.csv
