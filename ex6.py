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
    for s in input:
        if s != ' ':
            counter = 0
            charactor = s

            if s in input:
                    counter += 1

            output += s + '(' + str(counter) + ')'

    return output
