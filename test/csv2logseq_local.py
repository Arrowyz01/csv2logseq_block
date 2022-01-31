# you may pip install pandas before.
import sys
import pandas as pd

# read file from argv
df = pd.read_csv (sys.argv[1])

# extract csv file name
import_file_name = sys.argv[1].split('.')[0]

# put the output file (same name with your input file but with _local.md)
output_file = open('./'+import_file_name+'_local.md', 'w')
sys.stdout = output_file

# pd.set_option('max_colwidth',None)

df.columns = df.columns.str.replace(' ', '_')

# create a first-level block in your logseq, the name is your input file
print("- "+str(sys.argv[1]))

# find first column name, you will use it as block title
first_column_name = df.columns[0]

# output from csv to block properties
for i in range(df.shape[0]):
    for index,data in df.iteritems():
        # block title is your first column name in csv
        if index == first_column_name:
            # create a second-level block under above first-level block, this block with two[[]], that can link to a new page, you can use it to write new notes
            print("  - [["+str(data[i])+"]]")
            # create a third-level block under above second-level block, without any [[]], that can be used to in query table
            print("    - "+str(data[i]))
            # incorporate a source-file property in every third-level block that can be query afterward
            print("    "+"source_file:: "+str(sys.argv[1]))
        else:
        # write properties of the third-level block
            print("    "+str(index)+":: "+str(data[i]))

# a basic query that will create a table that looks like the format in csv or a notion table database
# you can change the table name Publication list to any name you want!!!
print("- query-table:: true"+"\n"+
"  #+BEGIN_QUERY"+"\n"+
"  {:title [:h2 "+"\""+"Publication list"+"\"]"+"\n"+
"   :query [:find (pull ?b [*])"+"\n"+
"           :where"+"\n"+
"           [?b :block/properties ?p]"+"\n"+
"           [(get ?p :source-file) ?t]"+"\n"+
"           [(= \""+str(sys.argv[1])+"\" ?t)]]}"+"\n"+
"  #+END_QUERY")

output_file.close()
