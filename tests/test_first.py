from pyspark.sql.session import SparkSession
from typed_pyspark import DataFrame, class_annotation
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()

@class_annotation
class User(DataFrame):
    name: str
    age: str

Foo = class_annotation(DataFrame['abc'])

users_data = [
    {'name': 'user1', 'age': 29},
    {'name': 'user2', 'age': 30},
    {'name': 'user1', 'age': 15},
]

users = User.from_data(users_data)
SumResult = DataFrame['name': type(str), 'age']

def avg_age(df: User) -> SumResult:
    return df.groupBy('name').agg(F.sum('age').alias('sum'))

def test_columns_present():
    annotation = DataFrame['name': str, 'age': int]
    assert annotation.columns == {'name', 'age'}

def test_create_objects():
    user = User(**users_data[0])

    assert user.name == users_data[0]['name']
    assert isinstance(user, DataFrame)

    assert users[0].name == users_data[0]['name']
    assert users[0].age == users_data[0]['age']
    assert users[1].age == users_data[1]['age']

def test_function_defition():
    df = spark.createDataFrame(users)

    result = avg_age(df)
