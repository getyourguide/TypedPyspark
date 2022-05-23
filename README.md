# TypedPyspark

Contains a set of abstractions to type dataframes in pyspark.

Allows one to:

- Define dataframe schemas and use them as annotations in variables, functions, classes
- Create mock data for tests easily based on these schemas

#  Rationale

In Projects using spark that follow software engineering best practices is common to see
functions defined with type annotations like this:

```py
from pyspark.sql import DataFrame

def get_name_from_id(dt: DataFrame) -> DataFrame:
    ...
```

But this type annotation only guarantees that a DataFrame instance is called.
It says nothing about how the dataframe looks like.

1. If the columns needed are there
2. If they have the correct types
3. If there are much more data than needed

This library tries to address exactly these problems.
By running it you get type errors when the annotations dont match reality.
You also get self-documenting code in form of expressive annotations.


# How to use it

```py

from typed_pyspark import Dataframe

reviewTable = Dataframe(
    default_values={
        "original_review_id": 0,
        "is_original_language": True,
        "review_text_id": 1,
        "rating": 2.4,
    },
    schema={
        "date_of_review": "Timestamp",
        "review_id": "Integer",
        "tour_id": "Integer",
        "rating": "Double",
        "original_review_id": "Integer",
        "is_original_language": "Boolean",
        "review_text_id": "Integer",
    },
)

ReviewTableType = ReviewTable.type_annotation()

Daily_Reviews = Dataframe( schema={
        "date": "Date",
        "tour_id": "Integer",
        "num_reviews": "Integer",
        "avg_star_rating": "Double",
    },
    default_values={},
)

Daily_ReviewsType = Daily_Reviews.type_annotation()


# defining type annotations
def calculate_daily_review_data(
    date_begin: date, date_end: date, reviews: ReviewTableType
) -> Daily_ReviewsType:
    ...

# writing tests
def test_dates_are_filtered():
    reviews_df = ReviewTable.create_df(
        [
            {
                "review_id": 1,
                "tour_id": 2,
            },
            {
                "review_id": 2,
                "tour_id": 2,
            },
        ],
    )

    result_df: RawReviewsType = get_raw_reviews(datetime.date(2021, 12, 15), reviews_df)
    expected_df = RawReviews.create_df(
        [
            {
                "review_id": 1,
                "tour_id": 2,
            },
        ],
    )


```

# Install

```sh
pip install 'typed-pyspark~=0.0.4'
```

## Acknowledgements

Inspired by [dataenforce](https://github.com/CedricFR/dataenforce) which provides similar functionality for pandas.
