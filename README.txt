Read Me


Two text files were used in approximate string matching experiment are queries.1k.txt and tweets.3K.txt. The former one is queries string with US locations, the latter one is target file with numerous tweets. 

The other two text files in folder is the result of experiment. compare_of_bi_gram.txt contains the comparison results between queries and targets based on bi-gram algorithm. It is sorted by lines of queries.1k.txt. The numbers after the line are the tweet IDs that contains the similar content with queries. If there is no IDs after it, that means no similar results have been found. So is compare_of_soundex.txt, which is based on soundex algorithm.


Two programming language file are written by python, which need to be compiled with python version 2.7(the 'cmp' function is no longer contained in python version 3+ which may cause problem in compiling with python version 3+ environment.) The one called as Bi_gram.py is implemented by bi-gram algorithm. It can automatically read content from two text files and write the result into another one. It can also filter the queries tokens which are shorter than 2 characters or are equal to "and". It intersects the array related to first and second token of queries then gets the result which is related to them both. They are all illustrated in report with specific introduction. As well as Soundex.py file. 





