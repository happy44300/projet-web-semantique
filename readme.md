# LINK ALL THE DATA
### Semantic Web Project

[Link to the diapo](https://docs.google.com/presentation/d/17ujsVmwEoxKzDSSzz7CoVLtgLVd3hdcQStUgbiQ9YqY/edit#slide=id.p)

Objectives:
 - [x] Find an interesting dataset that can be linked with others
 - [x] Transform it into an RDF format (an RDF graph)
 - [ ] Executes some sparql requests on it, preferably interesting ones
 - [ ] Make some sparql requests that link another RDF graph, preferably interesting ones
 - [ ] Make a sparql requests that link to the maximum number of RDF graphs possible

## Dataset presentation

**Original dataset**: Amazon product reviews in France
 - [Link to the index](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt)
 - [Link to the file (170mb)](https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_FR_v1_00.tsv.gz)

In order to handle a smaller (more manageable) dataset, a python script [knife.py](https://github.com/happy44300/projet-web-semantique/blob/main/knife.py) was created and used to take a sample of the original dataset and to remove some columns. To use it, simply execute the python file in the same folder as the original dataset (not renamed). It requires the pandas library.

The sample created is called [review_sample.csv](https://github.com/happy44300/projet-web-semantique/blob/main/review_sample.csv), it has 10,000 lines and 11 columns.


## Transformation to RDF format (turtle)

To transform this dataset into an RDF format, the tool tarql was used. The script [tarqlerun.sparql](https://github.com/happy44300/projet-web-semantique/blob/main/tarqlerun.sparql) is used with tarql and transforms the data of [review_sample.csv](https://github.com/happy44300/projet-web-semantique/blob/main/review_sample.csv) into an RDF format (turtle by default).

Command to run our tarql script and save the results into a file (turtle format):
```bash
tarql tarqlerun.sparql > review_sample.ttl
```

This results in the file [review_sample.ttl](https://github.com/happy44300/projet-web-semantique/blob/main/review_sample.ttl) containing the data of the sample, but in an RDF format (turtle). This file will be used as the RDF graph for the upcoming sparql requests.


## Group members

Houda Bouferis - Adrien Lesénéchal - Malo Le Reste - Bilal Molli
