# coding: UTF-8


def unique(args):
    u"""与えられた数字の配列から、重複した数字を消した配列を取得する

    :param args: 数列
    :returns: 重複した数字が消された数列
    """
    #  NG case
    #uniq_list = args

    uniq_list = []
    for i in args :
        if i not in uniq_list :
            uniq_list.append(i)
    return uniq_list
