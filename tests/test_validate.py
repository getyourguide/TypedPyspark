from typing import Any

from pyspark.sql import SparkSession

from typed_pyspark import DataFrame, validate


def test_first():
    id = Any
    name = Any

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"id": "123"}])

    @validate
    def get_name(dt: DataFrame["id"]) -> DataFrame["id", "name"]:
        return dt

    result = get_name(df)
