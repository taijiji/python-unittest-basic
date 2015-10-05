# coding: UTF-8


def count(input):
    # Not implement

    u"""各数字の出現数を表す文字列を返す

    :param input:　数列の文字列。例えば"1 3 1 1 3 3"
    :returns: 各数字の出現数を表す文字列。例えば"1(3) 3(3)"
    """
    # NG case
    # output = input

    output = ''
    d = {}

    # create dictotionay
    # key: charactor, value: counter
    for s in input:
        if s != ' ' :
            if s not in d.keys() :
                d.update({ s : 1 })
            else :
                d[s] += 1

    # convert from dictionary to string
    for charactor in d.keys() :
        if output != '' :
            output += ' '
        output += str(charactor) + '(' + str(d[charactor])+ ')'

    return output
