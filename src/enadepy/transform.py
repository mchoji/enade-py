# The MIT License (MIT)
#
# Copyright (c) 2020 M. Choji
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""A set of functions that transform a dataset in any way."""

import pandas
from pandas.api.types import CategoricalDtype
from typing import List, TypeVar

from .index import get_index_dict
from .loaders import _dtypes

PandasSeries = TypeVar('PandasSeries', bound=pandas.core.frame.Series)
PandasDataFrame = TypeVar('PandasDataFrame', bound=pandas.core.frame.DataFrame)


def _label_co_turno_graduacao(row: PandasSeries) -> int:
    """Maps time period given from binary columns to category.

    This function maps the time period of a course indicated by the
    combination of three binary columns to a single value used as
    category.
    Currently, this is used to adjust the Enade microdata from 2016.
    Note: this function is not intended to be used externally.

    Args:
        row (PandasSeries): A row from Enade microdata.

    Returns:
        int: A value indicating the time period (category).
    """
    if row['IN_MATUT'] + row['IN_NOTURNO'] + row['IN_VESPER'] > 1:
        return 3
    elif row['IN_MATUT'] == 1:
        return 1
    elif row['IN_NOTURNO'] == 1:
        return 4
    else:
        return 2


def align_microdata_2016(filepath: str, output: str) -> None:
    """Changes Enade microdata from 2016 to match newer versions.

    Args:
        filepath (str): Path for the original data.
        output (str): Path for the output (converted) data.
    """
    df = pandas.read_csv(filepath, sep=';', dtype=_dtypes)
    df.rename(columns={'ANO_FIM_2G': 'ANO_FIM_EM'}, inplace=True)
    df = df.reindex(
        df.columns.tolist() + ['TP_INSCRICAO', 'TP_INSCRICAO_ADM'], axis=1
    )
    df['CO_TURNO_GRADUACAO'] = df.apply(
        lambda x: _label_co_turno_graduacao(x), axis=1
    )
    df.drop(
        columns=[
            'AMOSTRA', 'ID_STATUS', 'IN_GRAD', 'TP_SEMESTRE', 'IN_MATUT',
            'IN_NOTURNO', 'IN_VESPER'
        ],
        inplace=True
    )
    df.to_csv(output, sep=';', index=False, decimal=',')


def categorize(
    dataframe: PandasDataFrame,
    columns: List[str],
    only_current: bool = False
) -> PandasDataFrame:
    """Converts columns of a DataFrame to categorical type.

    Given a DataFrame, convert the given columns into categorical type
    according to predefined categories.

    Args:
        dataframe (PandasDataFrame): A pandas DataFrame containing Enade
        microdata.
        columns (List[str]): A list of columns to be converted to
        categorical type.
        only_current (bool, optional): If true, uses only currently
        present values as categories, not the predefined ones.
        Defaults to False.

    Returns:
        PandasDataFrame: A new DataFrame with the converted columns.
    """
    if not isinstance(dataframe, pandas.DataFrame):
        raise TypeError(
            'Argument "dataframe" should be of type pandas.DataFrame'
        )
    if not isinstance(columns, list):
        raise TypeError('Argument "columns" should be of type list')
    result = dataframe.copy()
    for col in columns:
        try:
            idx_col = get_index_dict(col)
        except NameError:
            result.loc[:, col] = result[col].astype('category')
        else:
            cats = list(idx_col.keys())
            cat_type = CategoricalDtype(cats)
            result.loc[:, col] = result[col].astype(cat_type)
            if only_current:
                result.loc[:, col].cat.remove_unused_categories()

    return result
