# coding: UTF-8

def sum(args):
    u"""与えられた数列を合計する

    :param args: 数列
    :returns: 合計
    argsで引数をいくつでも取れる
    """
    result = 0
    for i in args:
        #result = result + i
        result += i
    return result
