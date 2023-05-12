"""
Helpers for sharing tests between DataFrame/Series
"""

from pandas import DataFrame


def get_dtype(obj):
    return obj.dtypes.iat[0] if isinstance(obj, DataFrame) else obj.dtype


def get_obj(df: DataFrame, klass):
    """
    For sharing tests using frame_or_series, either return the DataFrame
    unchanged or return it's first column as a Series.
    """
    return df if klass is DataFrame else df._ixs(0, axis=1)
