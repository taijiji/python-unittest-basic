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
    # answer 1
    '''
    for i in range(0, len(input)):
        #output = output +  str(input[i])
        j = len(input) - i - 1
        output += input[j]
    '''

    #answer 2
    '''
    for i in reversed( range(0, len(input)) ):
        output += input[i]
    '''

    #answer 3
    #output = output.join(reversed(input))

    #anser4
    # リストスライスの3項目は、インクリメントする数を示す.
    #[::2]であれば[0],[2],[4],[6]....
    # [::-1]の場合は、逆向きに 1つずつリストをたどる
    output = input[::-1]

    return output
