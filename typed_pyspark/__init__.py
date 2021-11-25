from typing import List, Generic, get_type_hints
import typing
from pyspark.sql import DataFrame as DataFrameOrig
import inspect
import attr

def _get_column_types(p):
    columns = set()
    dtypes = {}

    if isinstance(p, str):
        columns.add(p)
    elif isinstance(p, slice):
        columns.add(p.start)
        if not inspect.isclass(p.stop):
            raise TypeError("Column type hints must be classes, error with %s" % repr(p.stop))
        dtypes[p.start] = p.stop
    elif isinstance(p, (list, set)):
        for el in p:
            subcolumns, subdtypes = _get_column_types(el)
            columns |= subcolumns
            dtypes.update(subdtypes)
    elif isinstance(p, DatasetMeta):
        columns |= p.columns
        dtypes.update(p.dtypes)
    else:
        raise TypeError("Dataset[col1, col2, ...]: each col must be a string, list or set.")

    return columns, dtypes

class DatasetMeta(type):
    def __new__(metacls, name, bases, namespace, **kargs):
        return super().__new__(metacls, name, bases, namespace)

    def __getitem__(self, parameters):
        if hasattr(self, '__origin__') and (self.__origin__ is not None or self._gorg is not Dataset):
            return super().__getitem__(parameters)
        if parameters == ():
            return super().__getitem__(())
        if not isinstance(parameters, tuple):
            parameters = (parameters,)
        parameters = list(parameters)

        only_specified = True
        if parameters[-1] is ...:
            only_specified = False
            parameters.pop()

        columns, dtypes = _get_column_types(parameters)

        meta = DatasetMeta(self.__name__, self.__bases__, {})
        meta.only_specified = only_specified
        meta.columns = columns
        meta.dtypes = dtypes

        return meta



def class_annotation(cls):
    print("class annotation happening")
    return cls

class DataFrame(DataFrameOrig, extra=Generic, metaclass=DatasetMeta):

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            print(name, value)
            setattr(self, name, value)

    @classmethod
    def from_data(cls, data: List[dict]) -> List['DataFrame']:
        result = []
        for row in data:
            rowobj = cls(**row)
            result.append(rowobj)

        return result

    def __getattr__(self, name):
           return self[name]

    def __getitem__(self, items):
        return None

    def __repr__(self):
        return object.__repr__(self)