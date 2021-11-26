from pyspark.sql import SparkSession

from typed_pyspark import DataFrame


class User(DataFrame):
    id: int
    name: str


def test_simple_object():
    def test(f: User) -> User:
        return f

    test(User(id=123, name="abc"))


def test_spark():
    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"phone": "1233125"}])

    def f_spark(f: User) -> User:
        return f

    user: User = f_spark(df)
