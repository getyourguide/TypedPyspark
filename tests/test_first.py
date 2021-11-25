from pyspark.sql.session import SparkSession
from typed_pyspark import DataFrame

spark = SparkSession.builder.getOrCreate()

def test_columns_present():
    annotation = DataFrame['name': str, 'age': int]
    assert annotation.columns == {'name', 'age'}

