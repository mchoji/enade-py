"""A set of functions that transform a dataset in any way."""

import pandas as pd
from pandas.api.types import CategoricalDtype

from .index import get_index_dict
from .loaders import _dtypes


def _label_co_turno_graduacao(row):
    if row['IN_MATUT'] + row['IN_NOTURNO'] + row['IN_VESPER'] > 1:
        return 3
    elif row['IN_MATUT'] == 1:
        return 1
    elif row['IN_NOTURNO'] == 1:
        return 4
    else:
        return 2


def align_microdata_2016(filepath_or_buffer, output):
    """Changes microdata from 2016 to match newer versions."""
    df = pd.read_csv(filepath_or_buffer, sep=';', dtype=_dtypes)
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


def categorize(dataframe, columns, only_current=False):
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError(
            'Argument "dataframe" should be of type pandas.DataFrame'
        )
    if not isinstance(columns, list):
        raise TypeError(
            'Argument "columns" should be of type list'
        )
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
