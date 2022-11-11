mkdir data
curl https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_US_v1_00.tsv.gz --output ./data/amazon_reviews_multilingual_US_v1_00.tsv.gz
curl https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_UK_v1_00.tsv.gz --output ./data/amazon_reviews_multilingual_UK_v1_00.tsv.gz
curl https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_JP_v1_00.tsv.gz --output ./data/amazon_reviews_multilingual_JP_v1_00.tsv.gz
curl https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_FR_v1_00.tsv.gz --output ./data/amazon_reviews_multilingual_FR_v1_00.tsv.gz
curl https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_DE_v1_00.tsv.gz --output ./data/amazon_reviews_multilingual_DE_v1_00.tsv.gz