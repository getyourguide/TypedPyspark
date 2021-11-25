from pyspark.sql.session import SparkSession
from typed_pyspark import DataFrame

spark = SparkSession.builder.getOrCreate()

def test_spark():
    data  = [{'name': "abc", "age": 21}, {'name': "cde", "age": 23}]

    annotation = DataFrame['name': str, 'age': int]
    assert annotation.columns == {'name', 'age'}

