from collections import Counter


def shannon_fano_recursion(symbols, codes, current_code=''):
    n = len(symbols)

    if n == 1:
        char, _ = symbols[0]
        codes[char] = current_code
        return

    total_freq = sum(freq for _, freq in symbols)
    half_freq = total_freq / 2

    current_freq = 0
    split_idx = 0
    for idx, (_, freq) in enumerate(symbols):
        current_freq += freq
        split_idx = idx
        if current_freq > half_freq:
            if abs(current_freq - half_freq) > abs((current_freq - freq) - half_freq):
                split_idx -= 1
            break

    left_group = symbols[:split_idx + 1]
    right_group = symbols[split_idx + 1:]

    shannon_fano_recursion(left_group, codes, current_code + '0')
    shannon_fano_recursion(right_group, codes, current_code + '1')


def shannon_fano(text):
    frequencies = Counter(text).items()
    sorted_symbols = sorted(frequencies, key=lambda x: -x[1])

    codes = {}
    shannon_fano_recursion(sorted_symbols, codes)
    return codes


text = "this is an example for shannon fano encoding"
codes = shannon_fano(text)
print("Shannon-Fano Codes:", codes)
