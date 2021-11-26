import unittest
from pyspark.sql.session import SparkSession
import pyspark.sql.functions as F
from typed_pyspark import DataFrame, class_annotation

def avg_age(df):
    return df.groupBy("name").agg(F.sum("age").alias("sum"))

@class_annotation
class User(DataFrame):
    name: str
    age: str


users_data = [
    {"name": "user1", "age": 29},
    {"name": "user2", "age": 30},
    {"name": "user1", "age": 15},
]


class AnnotationTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.users = User.from_data(users_data)
        super().__init__(*args, **kwargs)

    def test_first(self):
        spark = SparkSession.builder.getOrCreate()

        df = spark.createDataFrame(self.users)

        result = avg_age(df)
        assert len(result.collect()) == 2

    def test_create_objects(self):
        user = User(**users_data[0])

        assert user.name == users_data[0]["name"]
        assert isinstance(user, DataFrame)

        assert self.users[0].name == users_data[0]["name"]
        assert self.users[0].age == users_data[0]["age"]
        assert self.users[1].age == users_data[1]["age"]


if __name__ == '__main__':
    unittest.main()
