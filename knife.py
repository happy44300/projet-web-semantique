import pandas as pd
import numpy as np

chunk = pd.read_csv("amazon_reviews_multilingual_FR_v1_00.tsv", sep="\t")

sample = chunk.sample(10000)

print(sample.columns)

sample = sample.drop("customer_id",  axis=1)
sample = sample.drop("product_id", axis=1)
sample = sample.drop("product_parent",  axis=1)
sample = sample.drop("vine",  axis=1)
sample = sample.drop("verified_purchase",  axis=1)


sample.to_csv("out.csv", index=False)
