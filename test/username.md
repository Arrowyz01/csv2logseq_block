- username.csv
	- [[booker12]]
		- booker12
		source_file:: username.csv
		Identifier:: 9012
		First_name:: Rachel
		Last_name:: Booker
	- [[grey07]]
		- grey07
		source_file:: username.csv
		Identifier:: 2070
		First_name:: Laura
		Last_name:: Grey
	- [[johnson81]]
		- johnson81
		source_file:: username.csv
		Identifier:: 4081
		First_name:: Craig
		Last_name:: Johnson
	- [[jenkins46]]
		- jenkins46
		source_file:: username.csv
		Identifier:: 9346
		First_name:: Mary
		Last_name:: Jenkins
	- [[smith79]]
		- smith79
		source_file:: username.csv
		Identifier:: 5079
		First_name:: Jamie
		Last_name:: Smith
- query-table:: true
  #+BEGIN_QUERY
  {:title [:h2 "Name list"]
   :query [:find (pull ?b [*])
           :where
           [?b :block/properties ?p]
           [(get ?p :source-file) ?t]
           [(= "username.csv" ?t)]]}
  #+END_QUERY
