# type: ignore[return-value,type-arg]
from __future__ import annotations

from typing import Any, NewType

from typed_pyspark import DataFrame, class_annotation


def test_columns_present():
    annotation = DataFrame["name":str, "age":int]
    assert annotation.columns == {"name", "age"}
