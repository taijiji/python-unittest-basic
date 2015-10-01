# coding: UTF-8


def min(args):
    u"""与えられた数列から最も小さな数字を取得

    :param args: 数列
    :returns: 最も小さな数字
    """
    minimum = args[0]
    for i in args:
        if i < minimum:
            minimum = i
    return minimum
