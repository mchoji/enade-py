"""A module for frequent itemsets mining."""

import pandas as pd
from mlxtend.frequent_patterns import association_rules, fpgrowth, fpmax


def freq_itemsets(dataframe, max=False, **kwargs):
    if max:
        res = fpmax(dataframe, **kwargs)
    else:
        res = fpgrowth(dataframe, **kwargs)
    res['length'] = res['itemsets'].apply(lambda x: len(x))

    return res


def _is_closed(itemset, same_sup_itemsets):
    check = [itemset.issubset(x) for x in same_sup_itemsets if x != itemset]
    return not bool(check.count(True))


def closed_freq_itemsets(dataframe, **kwargs):
    freq_isets = fpgrowth(dataframe, **kwargs)
    sup_uniq = freq_isets.support.unique()
    sup_dict = {}

    for sup in sup_uniq:
        samesup_isets = list(
            freq_isets.loc[freq_isets.support == sup, 'itemsets']
        )
        sup_dict[sup] = samesup_isets

    freq_isets['isclosed'] = freq_isets.apply(
        lambda x: _is_closed(x.itemsets, sup_dict[x.support]),
        axis=1,
    )
    freq_isets['length'] = freq_isets['itemsets'].apply(lambda x: len(x))
    return freq_isets


def freq_itemsets_sort(
    dataframe, max=False, sort_by='support', ascending=False, **kwargs
):
    res = freq_itemsets(dataframe, max=max, **kwargs)
    if sort_by not in ['support', 'length']:
        raise ValueError(
            'Argument sort_by should be either "support" or "length"'
        )
    res.sort_values(by=sort_by, ascending=ascending, inplace=True)
    return res


def closed_freq_itemsets_sort(
    dataframe, sort_by='support', ascending=False, **kwargs
):
    res = closed_freq_itemsets(dataframe, **kwargs)
    if sort_by not in ['support', 'length']:
        raise ValueError(
            'Argument sort_by should be either "support" or "length"'
        )
    res.sort_values(by=sort_by, ascending=ascending, inplace=True)
    return res


def find_itemsets_all(
    freq_itemsets,
    search=set(),
    exact=False,
    col_name='itemsets',
):
    if exact:
        res = freq_itemsets.query(f'{col_name} == @search')
    else:
        idx = freq_itemsets[col_name].apply(lambda x: x.issuperset(search))
        res = freq_itemsets.loc[idx, :]

    return res


def find_itemsets_any(
    freq_itemsets,
    search=set(),
    col_name='itemsets',
):
    found = []
    for x in search:
        x_found = find_itemsets_all(freq_itemsets, {x}, col_name=col_name)
        if x_found is not None:
            found.append(x_found)
    res = pd.concat(found)
    res.drop_duplicates(inplace=True)
    return res


def find_itemsets_without(freq_itemsets, search=set(), col_name='itemsets'):
    exclude = find_itemsets_any(freq_itemsets, search, col_name)
    res = freq_itemsets.drop(index=exclude.index)
    return res


def association_rules_ext(freq_itemsets, **kwargs):
    rules = association_rules(freq_itemsets, **kwargs)
    rules['A_length'] = rules['antecedents'].apply(lambda x: len(x))
    rules['C_length'] = rules['consequents'].apply(lambda x: len(x))
    if 'isclosed' in freq_itemsets.columns:
        rules['A_isclosed'] = rules.merge(
            freq_itemsets[['itemsets', 'isclosed']],
            how='left',
            left_on='antecedents',
            right_on='itemsets'
        ).isclosed
        rules['C_isclosed'] = rules.merge(
            freq_itemsets[['itemsets', 'isclosed']],
            how='left',
            left_on='consequents',
            right_on='itemsets'
        ).isclosed
    return rules


def filter_rules(rules, by=['conviction', 'support', 'lift']):
    res = rules.sort_values(by=by, ascending=False)
    res['union'] = res.apply(
        lambda x: x.antecedents.union(x.consequents), axis=1
    )
    res.drop_duplicates(subset='union', inplace=True)
    res.drop(columns='union', inplace=True)
    return res
