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
"""A set of helpers for all Enade microdata data mining stages."""

from typing import List


def list_cols_exam(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to the exam.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to the exam, excluding the
        ones passed as argument.
    """
    cols = ['NU_ANO']
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_institution(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to the institution.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to the institution,
        excluding the ones passed as argument.
    """
    cols = [
        'CO_IES',
        'CO_CATEGAD',
        'CO_ORGACAD',
        'CO_GRUPO',
        'CO_CURSO',
        'CO_MODALIDADE',
        'CO_MUNIC_CURSO',
        'CO_UF_CURSO',
        'CO_REGIAO_CURSO',
    ]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_student(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to the student.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to the student,
        excluding the ones passed as argument.
    """
    cols = [
        'NU_IDADE',
        'TP_SEXO',
        'ANO_FIM_EM',
        'ANO_IN_GRAD',
        'CO_TURNO_GRADUACAO',
        'TP_INSCRICAO_ADM',
        'TP_INSCRICAO',
    ]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_obj_info(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to the objective part of the exam.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to the objective part of
        the exam, excluding the ones passed as argument.
    """
    cols = [
        'NU_ITEM_OFG',
        'NU_ITEM_OFG_Z',
        'NU_ITEM_OFG_X',
        'NU_ITEM_OFG_N',
        'NU_ITEM_OCE',
        'NU_ITEM_OCE_Z',
        'NU_ITEM_OCE_X',
        'NU_ITEM_OCE_N',
    ]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_vectors(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to vectors.

    Vectors, in this context, refer to the structures which contain the
    answers for the questions from the exam.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to vectors,
        excluding the ones passed as argument.
    """
    cols = [
        'DS_VT_GAB_OFG_ORIG',
        'DS_VT_GAB_OFG_FIN',
        'DS_VT_GAB_OCE_ORIG',
        'DS_VT_GAB_OCE_FIN',
        'DS_VT_ESC_OFG',
        'DS_VT_ACE_OFG',
        'DS_VT_ESC_OCE',
        'DS_VT_ACE_OCE',
    ]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_presence(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to types of presence.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to types of presence,
        excluding the ones passed as argument.
    """
    cols = [
        'TP_PRES',
        'TP_PR_GER',
        'TP_PR_OB_FG',
        'TP_PR_DI_FG',
        'TP_PR_OB_CE',
        'TP_PR_DI_CE',
    ]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_disc_status(exclude: List[str] = None) -> List[str]:
    """Returns situation types from discursive questions.

    Returns variable names related to the situation types from questions
    in the discursive part of the exam.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names, excluding the ones passed as
        argument.
    """
    cols = [
        'TP_SFG_D1',
        'TP_SFG_D2',
        'TP_SCE_D1',
        'TP_SCE_D2',
        'TP_SCE_D3',
    ]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_grades(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to the grades.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to the grades,
        excluding the ones passed as argument.
    """
    cols = [
        'NT_GER',
        'NT_FG',
        'NT_OBJ_FG',
        'NT_DIS_FG',
        'NT_FG_D1',
        'NT_FG_D1_PT',
        'NT_FG_D1_CT',
        'NT_FG_D2',
        'NT_FG_D2_PT',
        'NT_FG_D2_CT',
        'NT_CE',
        'NT_OBJ_CE',
        'NT_DIS_CE',
        'NT_CE_D1',
        'NT_CE_D2',
        'NT_CE_D3',
    ]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_exam_eval(exclude: List[str] = None) -> List[str]:
    """Returns columns related to the perception about the exame.

    Returns variable names related to the perception of the student
    about the exam.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names, excluding the ones passed as
        argument.
    """
    cols = [f'CO_RS_I{i}' for i in range(1, 10)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_socioecon(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to socioeconomics aspects.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to socioeconomics aspects,
        excluding the ones passed as argument.
    """
    cols = [f'QE_I{i:02}' for i in range(1, 27)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_inst_eval(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to institution evaluation.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to institution evaluation,
        excluding the ones passed as argument.
    """
    cols = [f'QE_I{i}' for i in range(27, 69)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_licentiate(exclude: List[str] = None) -> List[str]:
    """Returns variable names related to licentiate courses.

    Args:
        exclude (List[str], optional): list of variables to exclude from
        the output. Defaults to None.

    Returns:
        List[str]: The variable names related to licentiate courses,
        excluding the ones passed as argument.
    """
    cols = [f'QE_I{i}' for i in range(69, 82)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]
