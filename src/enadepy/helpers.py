"""A set of helpers for all Enade microdata data mining stages."""


def list_cols_exam(exclude=None):
    cols = ['NU_ANO']
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_institution(exclude=None):
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


def list_cols_student(exclude=None):
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


def list_cols_obj_info(exclude=None):
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


def list_cols_vectors(exclude=None):
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


def list_cols_presence(exclude=None):
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


def list_cols_disc_status(exclude=None):
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


def list_cols_grades(exclude=None):
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


def list_cols_exam_eval(exclude=None):
    cols = [f'CO_RS_I{i}' for i in range(1, 10)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_socioecon(exclude=None):
    cols = [f'QE_I{i:02}' for i in range(1, 27)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_inst_eval(exclude=None):
    cols = [f'QE_I{i}' for i in range(27, 69)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]


def list_cols_licentiate(exclude=None):
    cols = [f'QE_I{i}' for i in range(69, 82)]
    if exclude is None:
        return cols
    else:
        return [x for x in set(cols) - set(exclude)]
