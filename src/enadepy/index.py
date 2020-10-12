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
"""A set of indexes that map identifiers to descriptions.

Each index in this module relates to a question or student/institution
information (variable) in Enade microdata. Indexes are represented by
dictionaries and should not be accessed directly.
"""

from typing import Dict

from .helpers import list_cols_inst_eval

_index_co_categad = {
    1:
    'Pública Federal',
    2:
    'Pública Estadual',
    3:
    'Pública Municipal',
    4:
    'Privada com fins lucrativos',
    5:
    'Privada sem fins lucrativos',
    7:
    'Especial',
    93:
    'Pessoa Jurídica de Direito Público - Federal',
    115:
    'Pessoa Jurídica de Direito Público - Estadual',
    116:
    'Pessoa Jurídica de Direito Público - Municipal',
    118: (
        'Pessoa Jurídica de Direito Privado - '
        'Com fins lucrativos - Sociedade Civil'
    ),
    120: (
        'Pessoa Jurídica de Direito Privado - '
        'Sem fins lucrativos - Associação de Utilidade Pública'
    ),
    121:
    ('Pessoa Jurídica de Direito Privado - '
     'Sem fins lucrativos - Fundação'),
    10001:
    'Pessoa Jurídica de Direito Público - Estadual',
    10002:
    'Pessoa Jurídica de Direito Público - Federal',
    10003:
    'Pessoa Jurídica de Direito Público - Municipal',
    10004: (
        'Pessoa Jurídica de Direito Privado - '
        'Com fins lucrativos - Associação de Utilidade Pública'
    ),
    10005:
    'Privada com fins lucrativos',
    10006: (
        'Pessoa Jurídica de Direito Privado - '
        'Com fins lucrativos - Sociedade Mercantil ou Comercial'
    ),
    10007: (
        'Pessoa Jurídica de Direito Privado - '
        'Sem fins lucrativos - Associação de Utilidade Pública'
    ),
    10008:
    'Privada sem fins lucrativos',
    10009: (
        'Pessoa Jurídica de Direito Privado - '
        'Sem fins lucrativos - Sociedade'
    ),
    17634:
    'Fundação Pública de Direito Privado Municípal',
}

_index_co_orgacad = {
    10019: 'Centro Federal de Educação Tecnológica',
    10020: 'Centro Universitário',
    10022: 'Faculdade',
    10026: 'Instituto Federal de Educação, Ciência e Tecnologia',
    10028: 'Universidade',
}

_index_co_grupo = {
    # Enade 2016
    5: 'Medicina Veterinária',
    6: 'Odontologia',
    12: 'Medicina',
    17: 'Agronomia',
    19: 'Farmácia',
    23: 'Enfermagem',
    27: 'Fonoaudiologia',
    28: 'Nutrição',
    36: 'Fisioterapia',
    38: 'Serviço Social',
    51: 'Zootecnia',
    55: 'Biomedicina',
    69: 'Tecnologia em Radiologia',
    90: 'Tecnologia em Agronegócios',
    91: 'Tecnologia em Gestão Hospitalar',
    92: 'Tecnologia em Gestão Ambiental',
    95: 'Tecnologia em Estética E Cosmética',
    3501: 'Educação Física (Bacharelado)',
    # Enade 2017
    21: 'Arquitetura e Urbanismo',
    72: 'Tecnologia em Análise e Desenvolvimento de Sistemas',
    76: 'Tecnologia em Gestão da Produção Industrial',
    79: 'Tecnologia em Redes de Computadores',
    701: 'Matemática (Bacharelado)',
    702: 'Matemática (Licenciatura)',
    903: 'Letras - Português (Bacharelado)',
    904: 'Letras - Português (Licenciatura)',
    905: 'Letras - Português e Inglês (Licenciatura)',
    906: 'Letras - Português e Espanhol (Licenciatura)',
    1401: 'Física (Bacharelado)',
    1402: 'Física (Licenciatura)',
    1501: 'Química (Bacharelado)',
    1502: 'Química (Licenciatura)',
    1601: 'Ciências Biológicas (Bacharelado)',
    1602: 'Ciências Biológicas (Licenciatura)',
    2001: 'Pedagogia (Licenciatura)',
    2401: 'História (Bacharelado)',
    2402: 'História (Licenciatura)',
    2501: 'Artes Visuais (Licenciatura)',
    3001: 'Geografia (Bacharelado)',
    3002: 'Geografia (Licenciatura)',
    3201: 'Filosofia (Bacharelado)',
    3202: 'Filosofia (Licenciatura)',
    3502: 'Educação Física (Licenciatura)',
    #
    4003: 'Engenharia da Computação',
    4004: 'Ciência da Computação (Bacharelado)',
    4005: 'Ciência da Computação (Licenciatura)',
    4006: 'Sistemas de Informação',
    4301: 'Música (Licenciatura)',
    5401: 'Ciências Sociais (Bacharelado)',
    5402: 'Ciências Sociais (Licenciatura)',
    5710: 'Engenharia Civil',
    5806: 'Engenharia Elétrica',
    5814: 'Engenharia de Controle e Automação',
    5902: 'Engenharia Mecânica',
    6002: 'Engenharia de Alimentos',
    6008: 'Engenharia Química',
    6208: 'Engenharia de Produção',
    6306: 'Engenharia',
    6307: 'Engenharia Ambiental',
    6405: 'Engenharia Florestal',
    6407: 'Letras - Inglês',
    6409: 'Tecnologia em Gestão da Tecnologia da Informação',
    # Enade 2018
    1: 'Administração',
    2: 'Direito',
    13: 'Ciências Econômicas',
    18: 'Psicologia',
    22: 'Ciências Contábeis',
    26: 'Design',
    29: 'Turismo',
    38: 'Serviço Social',
    67: 'Secretariado Executivo',
    81: 'Relações Internacionais',
    83: 'Tecnologia em Design de Moda',
    84: 'Tecnologia em Marketing',
    85: 'Tecnologia em Processos Gerenciais',
    86: 'Tecnologia em Gestão de Recursos Humanos',
    87: 'Tecnologia em Gestão Financeira',
    88: 'Tecnologia em Gastronomia',
    93: 'Tecnologia em Gestão Comercial',
    94: 'Tecnologia em Logística',
    100: 'Administração Pública',
    101: 'Teologia',
    102: 'Tecnologia em Comércio Exterior',
    103: 'Tecnologia em Design de Interiores',
    104: 'Tecnologia em Design Gráfico',
    105: 'Tecnologia em Gestão da Qualidade',
    106: 'Tecnologia em Gestão Pública',
    803: 'Comunicação Social - Jornalismo',
    804: 'Comunicação Social - Publicidade e Propaganda',
}

_index_co_modalidade = {
    0: 'EaD',
    1: 'Presencial',
}

_index_co_uf_curso = {
    11: 'Rondônia (RO)',
    12: 'Acre (AC)',
    13: 'Amazonas (AM)',
    14: 'Roraima (RR)',
    15: 'Pará (PA)',
    16: 'Amapa (AP)',
    17: 'Tocantins (TO)',
    21: 'Maranhão (MA)',
    22: 'Piauí (PI)',
    23: 'Ceará (CE)',
    24: 'Rio Grande do Norte (RN)',
    25: 'Paraíba (PB)',
    26: 'Pernambuco (PE)',
    27: 'Alagoas (AL)',
    28: 'Sergipe (SE)',
    29: 'Bahia (BA)',
    31: 'Minas gerais (MG)',
    32: 'Espírito santo (ES)',
    33: 'Rio de janeiro (RJ)',
    35: 'São paulo (SP)',
    41: 'Paraná (PR)',
    42: 'Santa catarina (SC)',
    43: 'Rio grande do sul (RS)',
    50: 'Mato grosso do sul (MS)',
    51: 'Mato grosso (MT)',
    52: 'Goiás (GO)',
    53: 'Distrito federal (DF)',
}

_index_co_regiao_curso = {
    1: 'Norte',
    2: 'Nordeste',
    3: 'Sudeste',
    4: 'Sul',
    5: 'Centro-Oeste',
}

_index_tp_sexo = {
    'M': 'Masculino',
    'F': 'Feminino',
}

_index_co_turno_graduacao = {
    1: 'Matutino',
    2: 'Vespertino',
    3: 'Integral',
    4: 'Noturno',
}

_index_tp_inscricao_adm = {
    0: 'Tradicional',
    1: 'Judicial',
}

_index_tp_inscricao = {
    1: 'Concluinte',
}

_index_tp_pres = {
    222: 'Ausente',
    333: 'Resultado desconsiderado por inscrição indevida',
    334: 'Eliminado por participação indevida',
    444: 'Ausente devido a dupla graduação',
    555: 'Presente com resultado válido',
    556: 'Presente com resultado desconsiderado pela Aplicadora',
    888: 'Presente com resultado desconsiderado pelo Inep',
    999: 'Presente por Ação judicial',
}

_index_tp_pr_ger = {
    222: 'Ausente',
    333: 'Participação com prova em branco',
    555: 'Participação com respostas válidas na prova',
    556: 'Participação com resultado desconsiderado pela Aplicadora',
    888: 'Participação com resultado desconsiderado pelo Inep',
}

_index_tp_pr_ob_fg = _index_tp_pr_ger

_index_tp_pr_di_fg = _index_tp_pr_ger

_index_tp_pr_ob_ce = _index_tp_pr_ger

_index_tp_pr_di_ce = _index_tp_pr_ger

_index_tp_sfg_d1 = _index_tp_sfg_d2 = _index_tp_sce_d1 = _index_tp_sce_d2 = \
    _index_tp_sce_d3 = {
        222: 'Não se aplica (estudante ausente)',
        333: 'Questão em branco (estudante presente)',
        335: 'Questão zerada por motivo de resposta nula',
        336: 'Questão zerada por motivo de resposta divergente com a temática',
        555: 'Questão com resultado válido',
        556: ('Questão com resultado desconsiderado devido a '
              'problemas administrativos'),
        888: 'Questão não respondida por problemas administrativos',
    }

# Indexes for the questions from section 'Percepção da Prova'
_index_co_rs_i1 = _index_co_rs_i2 = {
    'A': 'Muito fácil',
    'B': 'Fácil',
    'C': 'Médio',
    'D': 'Difícil',
    'E': 'Muito difícil',
    '*': 'Resposta anulada',
    '.': 'Não respondeu',
}

_index_co_rs_i3 = {
    'A': 'Muito longa',
    'B': 'Longa',
    'C': 'Adequada',
    'D': 'Curta',
    'E': 'Muito curta',
    '*': 'Resposta anulada',
    '.': 'Não respondeu',
}

_index_co_rs_i4 = _index_co_rs_i5 = {
    'A': 'Sim, todos',
    'B': 'Sim, a maioria',
    'C': 'Apenas cerca da metade',
    'D': 'Poucos se apresentam',
    'E': 'Não, nenhum',
    '*': 'Resposta anulada',
    '.': 'Não respondeu',
}

_index_co_rs_i6 = {
    'A': 'Sim, até excessivas',
    'B': 'Sim, em todas elas',
    'C': 'Sim, na maioria delas',
    'D': 'Sim, somente em algumas',
    'E': 'Não, em nenhuma delas',
    '*': 'Resposta anulada',
    '.': 'Não respondeu',
}

_index_co_rs_i7 = {
    'A': 'Desconhecimento do conteúdo',
    'B': 'Forma diferente de abordagem do conteúdo',
    'C': 'Espaço insuficiente para responder às questões',
    'D': 'Falta de motivação para fazer a prova',
    'E': 'Não tive qualquer tipo de dificuldade para responder à prova',
    '*': 'Resposta anulada',
    '.': 'Não respondeu',
}

_index_co_rs_i8 = {
    'A': 'Não estudou ainda a maioria desses conteúdos',
    'B': 'Estudou alguns desses conteúdos, mas não os aprendeu',
    'C': 'Estudou a maioria desses conteúdos, mas não os aprendeu',
    'D': 'Estudou e aprendeu muitos desses conteúdos',
    'E': 'Estudou e aprendeu todos esses conteúdos',
    '*': 'Resposta anulada',
    '.': 'Não respondeu',
}

_index_co_rs_i9 = {
    'A': 'Menos de uma hora',
    'B': 'Entre uma e duas horas',
    'C': 'Entre duas e três horas',
    'D': 'Entre três e quatro horas',
    'E': 'Quatro horas e não consegui terminar',
    '*': 'Resposta anulada',
    '.': 'Não respondeu',
}

# Indexes for the questions from section 'Questionário do Estudante'
_index_qe_i01 = {
    'A': 'Solteiro(a)',
    'B': 'Casado(a)',
    'C': 'Separado(a) judicialmente/divorciado(a)',
    'D': 'Viúvo(a)',
    'E': 'Outro',
}

_index_qe_i02 = {
    'A': 'Branca',
    'B': 'Preta',
    'C': 'Amarela',
    'D': 'Parda',
    'E': 'Indígena',
    'F': 'Não quero declarar',
}

_index_qe_i03 = {
    'A': 'Brasileira',
    'B': 'Brasileira naturalizada',
    'C': 'Estrangeira',
}

_index_qe_i04 = _index_qe_i05 = {
    'A': 'Nenhuma',
    'B': 'Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série)',
    'C': 'Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série)',
    'D': 'Ensino Médio',
    'E': 'Ensino Superior - Graduação',
    'F': 'Pós-graduação',
}

_index_qe_i06 = {
    'A':
    'Em casa ou apartamento, sozinho',
    'B':
    'Em casa ou apartamento, com pais e/ou parentes',
    'C':
    'Em casa ou apartamento, com cônjuge e/ou filhos',
    'D':
    'Em casa ou apartamento, com outras pessoas (incluindo república)',
    'E':
    'Em alojamento universitário da própria instituição',
    'F': (
        'Em outros tipos de habitação individual ou coletiva '
        '(hotel, hospedaria, pensão ou outro)'
    ),
}

_index_qe_i07 = {
    'A': 'Nenhuma',
    'B': 'Uma',
    'C': 'Duas',
    'D': 'Três',
    'E': 'Quatro',
    'F': 'Cinco',
    'G': 'Seis',
    'H': 'Sete ou mais',
}

_index_qe_i08 = {
    'A': 'Até 1,5 salário mínimo',
    'B': 'De 1,5 a 3 salários mínimos',
    'C': 'De 3 a 4,5 salários mínimos',
    'D': 'De 4,5 a 6 salários mínimos',
    'E': 'De 6 a 10 salários mínimos',
    'F': 'De 10 a 30 salários mínimos',
    'G': 'Acima de 30 salários mínimos',
}

_index_qe_i09 = {
    'A': (
        'Não tenho renda e meus gastos são financiados '
        'por programas governamentais'
    ),
    'B': (
        'Não tenho renda e meus gastos são financiados '
        'pela minha família ou por outras pessoas'
    ),
    'C': (
        'Tenho renda, mas recebo ajuda da família ou de'
        ' outras pessoas para financiar meus gastos'
    ),
    'D':
    'Tenho renda e não preciso de ajuda para financiar meus gastos',
    'E':
    'Tenho renda e contribuo com o sustento da família',
    'F':
    'Sou o principal responsável pelo sustento da família',
}

_index_qe_i10 = {
    'A': 'Não estou trabalhando',
    'B': 'Trabalho eventualmente',
    'C': 'Trabalho até 20 horas semanais',
    'D': 'Trabalho de 21 a 39 horas semanais',
    'E': 'Trabalho 40 horas semanais ou mais',
}

_index_qe_i11 = {
    'A': 'Nenhum, pois meu curso é gratuito',
    'B': 'Nenhum, embora meu curso não seja gratuito',
    'C': 'ProUni integral',
    'D': 'ProUni parcial, apenas',
    'E': 'FIES, apenas',
    'F': 'ProUni Parcial e FIES',
    'G': 'Bolsa oferecida por governo estadual, distrital ou municipal',
    'H': 'Bolsa oferecida pela própria instituição',
    'I': 'Bolsa oferecida por outra entidade (empresa, ONG, outra)',
    'J': 'Financiamento oferecido pela própria instituição',
    'K': 'Financiamento bancário',
}

_index_qe_i12 = {
    'A': 'Nenhum',
    'B': 'Auxílio moradia',
    'C': 'Auxílio alimentação',
    'D': 'Auxílio moradia e alimentação',
    'E': 'Auxílio permanência',
    'F': 'Outro tipo de auxílio',
}

_index_qe_i13 = {
    'A': 'Nenhum',
    'B': 'Bolsa de iniciação científica',
    'C': 'Bolsa de extensão',
    'D': 'Bolsa de monitoria/tutoria',
    'E': 'Bolsa PET',
    'F': 'Outro tipo de bolsa acadêmica',
}

_index_qe_i14 = {
    'A':
    'Não participei',
    'B':
    'Sim, Programa Ciência sem Fronteiras',
    'C': (
        'Sim, programa de intercâmbio financiado pelo '
        'Governo Federal (Marca; Brafitec; PLI; outro'
    ),
    'D':
    'Sim, programa de intercâmbio financiado pelo Governo Estadual',
    'E':
    'Sim, programa de intercâmbio da minha instituição',
    'F':
    'Sim, outro intercâmbio não institucional',
}

_index_qe_i15 = {
    'A':
    'Não',
    'B':
    'Sim, por critério étnico-racial',
    'C':
    'Sim, por critério de renda',
    'D': (
        'Sim, por ter estudado em escola pública ou particular '
        'com bolsa de estudos'
    ),
    'E':
    'Sim, por sistema que combina dois ou mais critérios anteriores',
    'F':
    'Sim, por sistema diferente dos anteriores',
}

_index_qe_i16 = {
    11: 'Rondônia (RO)',
    12: 'Acre (AC)',
    13: 'Amazonas (AM)',
    14: 'Roraima (RR)',
    15: 'Pará (PA)',
    16: 'Amapa (AP)',
    17: 'Tocantins (TO)',
    21: 'Maranhão (MA)',
    22: 'Piauí (PI)',
    23: 'Ceará (CE)',
    24: 'Rio Grande do Norte (RN)',
    25: 'Paraíba (PB)',
    26: 'Pernambuco (PE)',
    27: 'Alagoas (AL)',
    28: 'Sergipe (SE)',
    29: 'Bahia (BA)',
    31: 'Minas gerais (MG)',
    32: 'Espírito santo (ES)',
    33: 'Rio de janeiro (RJ)',
    35: 'São paulo (SP)',
    41: 'Paraná (PR)',
    42: 'Santa catarina (SC)',
    43: 'Rio grande do sul (RS)',
    50: 'Mato grosso do sul (MS)',
    51: 'Mato grosso (MT)',
    52: 'Goiás (GO)',
    53: 'Distrito federal (DF)',
    99: 'Não se aplica',
}

_index_qe_i17 = {
    'A': 'Todo em escola pública',
    'B': 'Todo em escola privada (particular)',
    'C': 'Todo no exterior',
    'D': 'A maior parte em escola pública',
    'E': 'A maior parte em escola privada (particular)',
    'F': 'Parte no Brasil e parte no exterior',
}

_index_qe_i18 = {
    'A':
    'Ensino médio tradicional',
    'B': (
        'Profissionalizante técnico '
        '(eletrônica, contabilidade, agrícola, outro)'
    ),
    'C':
    'Profissionalizante magistério (Curso Normal)',
    'D':
    'Educação de Jovens e Adultos (EJA) e/ou Supletivo',
    'E':
    'Outra modalidade',
}

_index_qe_i19 = {
    'A': 'Ninguém',
    'B': 'Pais',
    'C': 'Outros membros da família que não os pais',
    'D': 'Professores',
    'E': 'Líder ou representante religioso',
    'F': 'Colegas/Amigos',
    'G': 'Outras pessoas',
}

_index_qe_i20 = {
    'A': 'Não tive dificuldade',
    'B': 'Não recebi apoio para enfrentar dificuldades',
    'C': 'Pais',
    'D': 'Avós',
    'E': 'Irmãos, primos ou tios',
    'F': 'Líder ou representante religioso',
    'G': 'Colegas de curso ou amigos',
    'H': 'Professores do curso',
    'I': 'Profissionais do serviço de apoio ao estudante da IES',
    'J': 'Colegas de trabalho',
    'K': 'Outro grupo',
}

_index_qe_i21 = {
    'A': 'Sim',
    'B': 'Não',
}

_index_qe_i22 = {
    'A': 'Nenhum',
    'B': 'Um ou dois',
    'C': 'De três a cinco',
    'D': 'De seis a oito',
    'E': 'Mais de oito',
}

_index_qe_i23 = {
    'A': 'Nenhuma, apenas assisto às aulas',
    'B': 'De uma a três',
    'C': 'De quatro a sete',
    'D': 'De oito a doze',
    'E': 'Mais de doze',
}

_index_qe_i24 = {
    'A':
    'Sim, somente na modalidade presencial',
    'B':
    'Sim, somente na modalidade semipresencial',
    'C': (
        'Sim, parte na modalidade presencial '
        'e parte na modalidade semipresencial'
    ),
    'D':
    'Sim, na modalidade a distância',
    'E':
    'Não',
}

_index_qe_i25 = {
    'A': 'Inserção no mercado de trabalho',
    'B': 'Influência familiar',
    'C': 'Valorização profissional',
    'D': 'Prestígio Social',
    'E': 'Vocação',
    'F': 'Oferecido na modalidade a distância',
    'G': 'Baixa concorrência para ingresso',
    'H': 'Outro motivo',
}

_index_qe_i26 = {
    'A': 'Gratuidade',
    'B': 'Preço da mensalidade',
    'C': 'Proximidade da minha residência',
    'D': 'Proximidade do meu trabalho',
    'E': 'Facilidade de acesso',
    'F': 'Qualidade/reputação',
    'G': 'Foi a única onde tive aprovação',
    'H': 'Possibilidade de ter bolsa de estudo',
    'I': 'Outro motivo',
}

# Variables from QE_I27 TO QE_I68 take a scale format
_index_qe_i27_to_qe_i68 = {
    1: 'Discordo totalmente',
    2: 'Discordo consideravalmente',
    3: 'Discordo parcialmente',
    4: 'Concordo parcialmente',
    5: 'Concordo consideravelmente',
    6: 'Concordo totalmente',
    7: 'Não sei responder',
    8: 'Não se aplica',
}

# TODO: indexes from QE_I169 to QE_I81 (exclusive for licentiate)


def get_index_dict(varname: str) -> Dict:
    """Gets a map to translate indexes from a given variable.

    Given a variable name (column name from Enade microdata), returns
    a dictionary containing the values seen in microdata as dictionary's
    keys and the respective descriptions as dictionary's values.

    Args:
        varname (str): A variable or column name from Enade microdata.

    Raises:
        NameError: if a dictionary was not found for the given name.

    Returns:
        Dict: A dictionary mapping values to descriptions for a given
        variable or column name.
    """
    if not isinstance(varname, str):
        raise TypeError('Expected string as argument')

    if varname.upper() in list_cols_inst_eval():
        return _index_qe_i27_to_qe_i68

    dict_name = '_index_' + varname.lower()
    if dict_name in globals():
        return globals()[dict_name]
    else:
        raise NameError(f'Index for {varname} not found')
