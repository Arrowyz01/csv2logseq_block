# csv2md_by_template (csv2mdt.py)
- this script helps you to convert csv file to md files via template

# Preparation
- python3
- pandas
- template.md
- filename.csv

# Caution
-  the variables in template.md should be like $title, $name or $title_name (no blank in variables, please replace blank with '_' by yourself)
- the variables in template.md should match the first row (colume name) in data.csv
- but you don't need to replace the blank in column name by yourself. script will do that. So you can keep column name in csv file as "title name"

# Quick start
- download csv2mdt.py and put it in the same folder as template.md and filename.csv
- use follow command
    > python csv2mdt.py filename.csv

- the output files will be automatically generated in the same folders

# Video


https://user-images.githubusercontent.com/85311840/153729075-4263ff1b-68c6-4309-bcfc-1075c82d330c.mp4

# Advanced
- you can edit the script somehow, such as the path to your template.md and the path to your csv file
- you can also put the script in $PATH, to make it easier to call
