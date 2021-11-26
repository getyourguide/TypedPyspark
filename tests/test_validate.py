from typing import Any

import pytest
from pyspark.sql import SparkSession

from typed_pyspark import DataFrame, InvalidSchemaException, validate_dataframes


def test_return():
    id = Any
    name = Any

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"id": "123"}])

    @validate_dataframes
    def get_name(dt: DataFrame["id"]) -> DataFrame["id", "name"]:
        return dt

    with pytest.raises(InvalidSchemaException):
        get_name(df)
