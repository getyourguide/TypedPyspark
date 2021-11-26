from pyspark.sql import SparkSession

from typed_pyspark import DataFrame

phone = str
url = str


def test_with_spark():
    df_names = DataFrame["phone", "url", ...]
    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"phone": "1233125"}])

    def test(df: df_names) -> DataFrame["phone", "url"]:
        return df

    test(df)


def test_first():
    df_names = DataFrame["phone", "url", ...]

    def test(df: df_names) -> DataFrame["phone", "url"]:
        return DataFrame()

    test(DataFrame())
