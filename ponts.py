from decimal import Decimal, getcontext

def arithmetic_encode(input_string, probabilities, initial_precision=4):  
    low, high = Decimal(0.0), Decimal(1.0)  
    precision = initial_precision  
    getcontext().prec = 64

    for char in input_string:
        range_size = high - low  
        char_low, char_high = map(Decimal, probabilities[char])

        high = low + range_size * char_high  
        low = low + range_size * char_low  

        low = low.quantize(Decimal('1e-{0}'.format(precision)))  
        high = high.quantize(Decimal('1e-{0}'.format(precision)))  

        print(f"{char}  {low}  {high} ")

        precision = min(precision + 1, 32)

    return low, high  

def calculate_probabilities(s):  
    char_count = {}  

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1  

    total_count = sum(char_count.values())  
    probabilities = {}
    cumulative_sum = 0.0

    for char in sorted(char_count.keys()):  
        char_prob = char_count[char] / total_count  
        probabilities[char] = (cumulative_sum, cumulative_sum + char_prob)  
        cumulative_sum += char_prob

    return probabilities  

def find_binary_code(low, high):
    q = Decimal(2) ** 10
    for i in range(1, 10000):
        value = Decimal(i) / q
        if low < value < high:
            return value
    return None

s = "зантариякристинаамеевна"

probabilities = calculate_probabilities(s)

low, high = arithmetic_encode(s, probabilities)

print(f"\nФинальная левая граница: {low}")  
print(f"Финальная правая граница: {high}")

input_string = "3688646496105178507855595"

number = int(input_string)

binary_representation = bin(number)[2:]

print("Двоичное представление:", '0' + binary_representation)

def calculate_parity_bits(data):
    n = len(data)
    r = 0
    while (2**r) < (n + r + 1):
        r += 1

    hamming_code = [''] * (n + r)

    j = 0
    for i in range(1, n + r + 1):
        if (i & (i - 1)) != 0:
            hamming_code[i - 1] = data[j]
            j += 1

    for i in range(r):
        parity_bit_position = 2**i
        parity_value = 0

        for j in range(1, n + r + 1):
            if j & parity_bit_position:
                if hamming_code[j - 1] != '':
                    parity_value ^= int(hamming_code[j - 1])

        hamming_code[parity_bit_position - 1] = str(parity_value)

    return ''.join(hamming_code)

input_string = "01100001101000110011110110101011110111110001110111110011111100010010100011011101011"

hamming_code = calculate_parity_bits(input_string)

print("Код Хэмминга для строки:", hamming_code)

