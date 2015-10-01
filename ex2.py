# coding: UTF-8


def reverse(input):
    u"""与えられた文字列を反対にする

    :param input: 文字列
    :returns: 反対になった文字列
    """
    # test result : NG
    #output = input

    # test result : OK
    #output = 'gnirts'

    output = ''
    for i in range(0, len(input)):
        #output = output +  str(input[i])
        j = len(input) - i - 1
        output += input[j]
    return output
