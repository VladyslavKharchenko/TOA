def binary(n):
    nbin = bin(n)[2:]
    print('Decimal {0} equals to binary {1}'.format(n, nbin))

    ones = zeros = ''
    for digit in nbin:
        if digit == '0':
            zeros += digit
        else:
            ones += digit

    ones_len = len(ones)
    biggest_bin = ones + zeros
    smallest_bin = zeros + ones
    print('There are {0} occurrences of "1" in {1}'.format(ones_len, nbin))
    print('The biggest number with the same number of occurrences is \t{0} which equals to {1}'
          .format(biggest_bin, int(ones + zeros, 2)))
    print('The smallest number with the same number of occurrences is \t{0} which equals to {1}'
          .format(smallest_bin, int(zeros + ones, 2)))

    return biggest_bin, smallest_bin
