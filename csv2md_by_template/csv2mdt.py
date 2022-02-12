import sys
import pandas as pd
from string import Template as tmp
# use string.Template function to replace $keyword in template.md and generate new md files, whose names are from csv first column.

# input csv file and transfer to pandas.Dataframe
csv_file=sys.argv[1]
df = pd.read_csv(csv_file)
# replace blank in the column name of csv file as '_', so replace "title name" as "title_name"
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(' ', '_')

# transfer Dataframe to python dict, the format is like [{A:1,B:2},{C:3,D:4}], so it's a list contains dicts
dict_list=df.to_dict('records')

# open template file, you can change it to your template file name and path
# the variables in template.md should be like $title, $name or $title_name
# the variables in template.md should be corresponding to the file line (colume name) in data.csv
# but you don't need to replace the blank in column name by yourself. script will do that. So you can keep column name in csv file as "title name"
with open('./template.md', 'r') as template_file:
    src = tmp(template_file.read())
    for group in dict_list:
        output_file = open('./'+group[list(group)[0]]+'.md', 'w')
        result = src.substitute(group)
        print(result, file=output_file)
        output_file.close()

