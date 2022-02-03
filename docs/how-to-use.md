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
