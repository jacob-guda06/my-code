def add_binary(a,b):
    decimal_result = a + b
    binary_result = ""
    while decimal_result > 0:
        remainder = decimal_result % 2
        decimal_result = decimal_result // 2
        binary_result = binary_result + str(remainder)
    return binary_result[::-1]