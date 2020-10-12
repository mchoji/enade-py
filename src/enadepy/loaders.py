# The MIT License (MIT)

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
"""Provides functions for loading and saving Enade data in general."""

import pandas
from typing import Any, TypeVar

PandasDataFrame = TypeVar('PandasDataFrame', bound=pandas.core.frame.DataFrame)

_dtypes = {
    'NU_ANO': 'int64',
    'CO_IES': 'int64',
    'CO_CATEGAD': 'int64',
    'CO_ORGACAD': 'int64',
    'CO_GRUPO': 'int64',
    'CO_CURSO': 'int64',
    'CO_MODALIDADE': 'int64',
    'CO_MUNIC_CURSO': 'int64',
    'CO_UF_CURSO': 'int64',
    'CO_REGIAO_CURSO': 'int64',
    'NU_IDADE': 'Int64',
    'TP_SEXO': 'string',
    'ANO_FIM_EM': 'Int64',
    'ANO_IN_GRAD': 'Int64',
    'CO_TURNO_GRADUACAO': 'Int64',
    'TP_INSCRICAO_ADM': 'Int64',
    'TP_INSCRICAO': 'Int64',
    'NU_ITEM_OFG': 'int64',
    'NU_ITEM_OFG_Z': 'int64',
    'NU_ITEM_OFG_X': 'int64',
    'NU_ITEM_OFG_N': 'int64',
    'NU_ITEM_OCE': 'int64',
    'NU_ITEM_OCE_Z': 'int64',
    'NU_ITEM_OCE_X': 'int64',
    'NU_ITEM_OCE_N': 'int64',
    'DS_VT_GAB_OFG_ORIG': 'string',
    'DS_VT_GAB_OFG_FIN': 'string',
    'DS_VT_GAB_OCE_ORIG': 'string',
    'DS_VT_GAB_OCE_FIN': 'string',
    'DS_VT_ESC_OFG': 'string',
    'DS_VT_ACE_OFG': 'str',
    'DS_VT_ESC_OCE': 'string',
    'DS_VT_ACE_OCE': 'str',
    'TP_PRES': 'Int64',
    'TP_PR_GER': 'Int64',
    'TP_PR_OB_FG': 'Int64',
    'TP_PR_DI_FG': 'Int64',
    'TP_PR_OB_CE': 'Int64',
    'TP_PR_DI_CE': 'Int64',
    'TP_SFG_D1': 'Int64',
    'TP_SFG_D2': 'Int64',
    'TP_SCE_D1': 'Int64',
    'TP_SCE_D2': 'Int64',
    'TP_SCE_D3': 'Int64',
    'NT_GER': 'float64',
    'NT_FG': 'float64',
    'NT_OBJ_FG': 'float64',
    'NT_DIS_FG': 'float64',
    'NT_FG_D1': 'float64',
    'NT_FG_D1_PT': 'float64',
    'NT_FG_D1_CT': 'float64',
    'NT_FG_D2': 'float64',
    'NT_FG_D2_PT': 'float64',
    'NT_FG_D2_CT': 'float64',
    'NT_CE': 'float64',
    'NT_OBJ_CE': 'float64',
    'NT_DIS_CE': 'float64',
    'NT_CE_D1': 'float64',
    'NT_CE_D2': 'float64',
    'NT_CE_D3': 'float64',
    'CO_RS_I1': 'string',
    'CO_RS_I2': 'string',
    'CO_RS_I3': 'string',
    'CO_RS_I4': 'string',
    'CO_RS_I5': 'string',
    'CO_RS_I6': 'string',
    'CO_RS_I7': 'string',
    'CO_RS_I8': 'string',
    'CO_RS_I9': 'string',
    'QE_I01': 'string',
    'QE_I02': 'string',
    'QE_I03': 'string',
    'QE_I04': 'string',
    'QE_I05': 'string',
    'QE_I06': 'string',
    'QE_I07': 'string',
    'QE_I08': 'string',
    'QE_I09': 'string',
    'QE_I10': 'string',
    'QE_I11': 'string',
    'QE_I12': 'string',
    'QE_I13': 'string',
    'QE_I14': 'string',
    'QE_I15': 'string',
    'QE_I16': 'Int64',
    'QE_I17': 'string',
    'QE_I18': 'string',
    'QE_I19': 'string',
    'QE_I20': 'string',
    'QE_I21': 'string',
    'QE_I22': 'string',
    'QE_I23': 'string',
    'QE_I24': 'string',
    'QE_I25': 'string',
    'QE_I26': 'string',
    'QE_I27': 'Int64',
    'QE_I28': 'Int64',
    'QE_I29': 'Int64',
    'QE_I30': 'Int64',
    'QE_I31': 'Int64',
    'QE_I32': 'Int64',
    'QE_I33': 'Int64',
    'QE_I34': 'Int64',
    'QE_I35': 'Int64',
    'QE_I36': 'Int64',
    'QE_I37': 'Int64',
    'QE_I38': 'Int64',
    'QE_I39': 'Int64',
    'QE_I40': 'Int64',
    'QE_I41': 'Int64',
    'QE_I42': 'Int64',
    'QE_I43': 'Int64',
    'QE_I44': 'Int64',
    'QE_I45': 'Int64',
    'QE_I46': 'Int64',
    'QE_I47': 'Int64',
    'QE_I48': 'Int64',
    'QE_I49': 'Int64',
    'QE_I50': 'Int64',
    'QE_I51': 'Int64',
    'QE_I52': 'Int64',
    'QE_I53': 'Int64',
    'QE_I54': 'Int64',
    'QE_I55': 'Int64',
    'QE_I56': 'Int64',
    'QE_I57': 'Int64',
    'QE_I58': 'Int64',
    'QE_I59': 'Int64',
    'QE_I60': 'Int64',
    'QE_I61': 'Int64',
    'QE_I62': 'Int64',
    'QE_I63': 'Int64',
    'QE_I64': 'Int64',
    'QE_I65': 'Int64',
    'QE_I66': 'Int64',
    'QE_I67': 'Int64',
    'QE_I68': 'Int64',
    'QE_I69': 'string',
    'QE_I70': 'string',
    'QE_I71': 'string',
    'QE_I72': 'string',
    'QE_I73': 'string',
    'QE_I74': 'string',
    'QE_I75': 'string',
    'QE_I76': 'string',
    'QE_I77': 'string',
    'QE_I78': 'string',
    'QE_I79': 'string',
    'QE_I80': 'string',
    'QE_I81': 'string'
}


def read_raw(filepath: str, **kwargs: Any) -> PandasDataFrame:
    """Loads raw data with expected dtypes and more.

    Args:
        filepath (str): A path for the raw data containing the microdata
        as provided by the official source.
        **kwargs (Any): Any arguments that should be passed to
        `pandas.read_csv`.

    Returns:
        PandasDataFrame: A pandas DataFrame.

    See Also:
        read_interm: reads Enade microdata that have already been loaded
        with `read_raw` once.
        write_interm: write a DataFrame containing Enade microdata to
        disk.
        pandas.read_csv
    """
    df = pandas.read_csv(
        filepath,
        sep=';',
        header=0,
        decimal=',',
        dtype=_dtypes,
        na_values={
            'ANO_FIM_EM': [''],
            'ANO_IN_GRAD': [''],
        },
        **kwargs
    )

    for column in ['DS_VT_ACE_OFG', 'DS_VT_ACE_OCE']:
        df[column] = df[column].astype('string')

    df['DS_VT_ACE_OFG'] = df['DS_VT_ACE_OFG'].str.zfill(8)
    df['DS_VT_ACE_OCE'] = df['DS_VT_ACE_OCE'].str.zfill(27)

    return df


def read_interm(filepath: str, **kwargs: Any) -> PandasDataFrame:
    """Loads intermediate data with expected dtypes.

    Loads data from disk representing Enade microdata that was
    initially loaded using function `read_raw`.

    Args:
        filepath (str): A path for data that was previously loaded using
        function `read_raw` and written to disk using `write_interm`.
        **kwargs (Any): Any arguments that should be passed to
        `pandas.read_csv`.

    Returns:
        PandasDataFrame: A pandas DataFrame with the loaded data.

    See Also:
        read_raw: reads raw Enade microdata.
        write_interm: writes a DataFrame containing Enade microdata to
        disk.
        pandas.read_csv
    """
    df = pandas.read_csv(filepath, dtype=_dtypes, **kwargs)
    return df


def write_interm(pd: PandasDataFrame, filepath: str, **kwargs: Any) -> None:
    """Writes a DataFrame to disk.

    Write a DataFrame previously loaded with functions `read_raw` or
    `read_interm` to disk.

    Args:
        pd (PandasDataFrame): A pandas DataFrame to write to disk.
        filepath (str): The file name where the data will be written to.
        **kwargs (Any): Any arguments that should be passed to
        `pandas.DataFrame.to_csv`.

    See Also:
        read_raw: reads raw Enade microdata.
        read_interm: reads formatted Enade microdata.
        pandas.DataFrame.to_csv
    """
    pd.to_csv(filepath, index=False, **kwargs)


def read_dtb_municipio(filepath: str) -> PandasDataFrame:
    """Reads DTB dataset from a file.

    Args:
        filepath (str): Path for DTB dataset in disk.

    Returns:
        PandasDataFrame: A pandas DataFrame with the loaded data.

    Note:
        The DTB dataset contains information about Brazilian Territorial
    Division and can be downloaded at
    https://www.ibge.gov.br/explica/codigos-dos-municipios.php.
    """
    df = pandas.read_csv(filepath, dtype='string')
    return df
