CREATE TABLE yelp.review (
    review_id text PRIMARY KEY,
    business_id text,
    cool int,
    date timestamp,
    funny int,
    minilm_description_embedding vector<float, 384>,
    stars int,
    text text,
    useful int,
    user_id text
);
