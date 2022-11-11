import pandas as pd

dataset_dir = "./data/"

chunk = pd.read_csv(dataset_dir + "amazon_reviews_multilingual_UK_v1_00.tsv.gz", compression='gzip', sep="\t",
                    encoding="utf-8", on_bad_lines='warn')
pd.read_csv(dataset_dir + "amazon_reviews_multilingual_FR_v1_00.tsv.gz", compression='gzip', sep="\t", encoding="utf-8",
            on_bad_lines='warn')
pd.read_csv(dataset_dir + "amazon_reviews_multilingual_JP_v1_00.tsv.gz", compression='gzip', sep="\t", encoding="utf-8",
            on_bad_lines='warn')
pd.read_csv(dataset_dir + "amazon_reviews_multilingual_DE_v1_00.tsv.gz", compression='gzip', sep="\t", encoding="utf-8",
            on_bad_lines='warn')
pd.read_csv(dataset_dir + "amazon_reviews_multilingual_US_v1_00.tsv.gz", compression='gzip', sep="\t", encoding="utf-8",
            on_bad_lines='warn')

nb_row = chunk.shape[0]
print(nb_row)

for i in {nb_row, 500000, 100000, 50000, 10000}:

    sample = chunk.sample(i)

    sample = sample.drop("customer_id", axis=1)
    sample = sample.drop("product_parent", axis=1)
    sample = sample.drop("vine", axis=1)
    sample = sample.drop("verified_purchase", axis=1)

    sample["product_title"].str.encode('ascii', 'ignore').str.decode('ascii')

    for collumn in sample:
        if sample[str(collumn)].dtypes == "object":
            sample[str(collumn)].str.encode('ascii', 'ignore').str.decode('ascii')

    sample["review_headline"].str.encode('ascii', 'ignore').str.decode('ascii')
    sample["review_body"].str.encode('ascii', 'ignore').str.decode('ascii')

    print(sample)

    sample.to_csv(str(i) + "_review_sample.csv", index=False, encoding="utf-8")
