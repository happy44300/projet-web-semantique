import sys

import pandas as pd
import re

countries = {
    "FR": "France",
    "UK": "United_Kingdom_of_Great_Britain_and_Northern_Ireland",
    "JP": "Japan",
    "DE": "Germany",
    "US": "United_States"
}


def replace(strToMatch, replaceWith, input):
    if strToMatch == input:
        return replaceWith
    else:
        return input


dataset_dir = "./data/"

df_uk = pd.read_csv(dataset_dir + "amazon_reviews_multilingual_UK_v1_00.tsv.gz", compression='gzip', sep="\t",
                    encoding="utf-8",
                    on_bad_lines='warn')

df_jp = pd.read_csv(dataset_dir + "amazon_reviews_multilingual_JP_v1_00.tsv.gz", compression='gzip', sep="\t",
                    encoding="utf-8",
                    on_bad_lines='warn')
df_de = pd.read_csv(dataset_dir + "amazon_reviews_multilingual_DE_v1_00.tsv.gz", compression='gzip', sep="\t",
                    encoding="utf-8",
                    on_bad_lines='warn')

df_us = pd.read_csv(dataset_dir + "amazon_reviews_multilingual_US_v1_00.tsv.gz", compression='gzip', sep="\t",
                    encoding="utf-8",
                    on_bad_lines='warn')

df_fr = pd.read_csv(dataset_dir + "amazon_reviews_multilingual_FR_v1_00.tsv.gz", compression='gzip', sep="\t",
                    encoding="utf-8",
                    on_bad_lines='warn')

dataframe = [df_uk, df_jp, df_us, df_de, df_fr]

nb_row = 0

for i in range(len(dataframe)):

    dataframe[i] = dataframe[i].drop("customer_id", axis=1)
    dataframe[i] = dataframe[i].drop("product_parent", axis=1)
    dataframe[i] = dataframe[i].drop("vine", axis=1)
    dataframe[i] = dataframe[i].drop("verified_purchase", axis=1)
    dataframe[i] = dataframe[i].drop("review_body", axis=1)

    nb_row += dataframe[i].shape[0]

    for countryCode in countries.keys():
        dataframe[i]["marketplace"] = dataframe[i]["marketplace"].apply(lambda x: replace(countryCode, countries.get(countryCode), x))

print("total triples:" + str(nb_row))

for i in {sys.maxsize}:
    totalTriples = i * len(dataframe)

    sample = None

    for _df in dataframe:
        if i < _df.shape[0]:
            sample = pd.concat([sample, _df.sample(i)])
        else:
            sample = pd.concat([sample, _df])

    file_name = str(totalTriples) + "_review_sample_light.csv"
    print("saving: " + file_name)
    sample.to_csv(file_name, index=False, encoding="utf-8")
