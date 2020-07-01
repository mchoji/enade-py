"""A set of functions that transform a dataset in any way."""

import pandas as pd

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
