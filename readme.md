# LINK ALL THE DATA
### Semantic Web Project

[Link to the diapo](https://docs.google.com/presentation/d/17ujsVmwEoxKzDSSzz7CoVLtgLVd3hdcQStUgbiQ9YqY/edit#slide=id.p)

Objectives:
 - [x] Find an interesting dataset that can be linked with others
 - [x] Transform it into an RDF format (an RDF graph)
 - [x] Executes some sparql requests on it, preferably interesting ones
 - [ ] Make some sparql requests that link another RDF graph, preferably interesting ones
 - [ ] Make a sparql requests that link to the maximum number of RDF graphs possible

## Dataset presentation

![](./img/graph.png)

[**Original dataset index**](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt): Amazon product reviews in uk, france, japan, germany, us

We have a little more than 10M triples in total.

You can use the download.bat file in ./dataset to download all the dataset (total size about 2gb).

We removed some columns from the original dataset: product_parent, customer_id, vine, verified_purchase, review_body.


## Generating the graph

In order to handle a smaller (more manageable) dataset, a python script [knife.py](https://github.com/happy44300/projet-web-semantique/blob/main/knife.py) 
was created in the dataset folder.

To use it, simply execute the python file in the same folder as the original dataset (not renamed). Since it open all 
the dataset it might need more than 8gb of ram to execute (18gb in fact).
It requires the python pandas library.

The samples created are called n_review_sample_light_csv where n is the number of review in the sample. We call them light
because we removed the review_body column making the file drastically smaller.

## Transformation to RDF format (turtle)

To transform this dataset into an RDF format, the tool tarql was used. The script [tarqlerun.sparql](https://github.com/happy44300/projet-web-semantique/blob/main/tarqlerun.sparql) is used with tarql and transforms the data of [review_sample.csv](https://github.com/happy44300/projet-web-semantique/blob/main/review_sample.csv) into an RDF format (turtle by default).

Command to run our tarql script and save the results into a file (ntriples format) from ./dataset folder:
```bash
..\tarql-1.2\bin\tarql --ntriples --encoding "utf-8" ..\tarqlerun.sparql ./25000_review_sample_light.csv > ./25000_review_sample_light.nt
```

This results in the file [n_review_sample.ttl](https://github.com/happy44300/projet-web-semantique/blob/main/25000_review_sample_light.nt)
containing the data of the sample, but in an RDF format (turtle). 
This file is used as the RDF graph for the upcoming sparql requests.


## Group members

Houda Bouferis - Adrien Lesénéchal - Malo Le Reste - Bilal Molli
