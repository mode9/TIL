# Converter Binary/Decimal/Hexadecimal
def converter(num, base):
    if base <= 10:
        result = convert_to_decimal(num, base)
    elif base <= 16:
        result = convert_hex_to_decimal(num)
    else:
        raise AttributeError('Base must be 1~16')

    return result


def convert_to_decimal(num, base):
    multiplier, result = 1, 0
    num = int(num)
    while num != 0:
        result += num % 10 * multiplier
        multiplier *= base
        num = num // 10

    return result


def convert_str_to_decimal(string):
    num = False
    try:
        num = int(string)
    except ValueError:
        for i in map(chr, range(97, 103)):
            if string == i:
                num = ord(i) - 87
                break

    assert num is False

    return num


def convert_hex_to_decimal(string):
    result = 0
    for index, value in enumerate(string):
        value = value.upper()
        hex = '0123456789ABCDEF'
        dec = hex.index(value)
        power = (len(string) - (index+1))
        result += dec * pow(16, power)

    return result


def main():
    target = 45883
    binary = bin(target).replace('0b', '')
    oc = oct(target).replace('0o', '')
    hexadecimal = hex(target).replace('0x', '')
    b_to_d = convert_to_decimal(binary, 2)
    o_to_d = convert_to_decimal(oc, 8)
    h_to_d = convert_str_to_decimal(hexadecimal)
    print(f'Binary: {binary} to {b_to_d}')
    print(f'Octal: {oc} to {o_to_d}')
    print(f'Hex: {hexadecimal} to {h_to_d}')

    print(converter(binary, 2))


if __name__ == '__main__':
    main()
