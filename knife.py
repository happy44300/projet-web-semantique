import pandas as pd
import urllib.parse


def clear_url(origin_url):
    return urllib.parse.quote_plus(origin_url)


chunk = pd.read_csv("amazon_reviews_multilingual_FR_v1_00.tsv", sep="\t", encoding="utf-8")

sample = chunk.sample(5)

sample = sample.drop("customer_id",  axis=1)
sample = sample.drop("product_id", axis=1)
sample = sample.drop("product_parent",  axis=1)
sample = sample.drop("vine",  axis=1)
sample = sample.drop("verified_purchase",  axis=1)


sample["product_title"] = sample["product_title"].apply(clear_url)

sample["product_title"].str.encode('ascii', 'ignore').str.decode('ascii')

for collumn in sample:
    if sample[str(collumn)].dtypes == "object":
        print(collumn)
        sample[str(collumn)].str.encode('ascii', 'ignore').str.decode('ascii')


sample["review_headline"].str.encode('ascii', 'ignore').str.decode('ascii')
sample["review_body"].str.encode('ascii', 'ignore').str.decode('ascii')

print(sample.columns)

sample.to_csv("review_sample.csv", index=False, encoding="utf-8")
