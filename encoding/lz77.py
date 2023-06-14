def lz77_encode(data, window_size=20):
    encoded = []
    i = 0

    while i < len(data):
        match_pos = 0
        match_len = 0
        for j in range(max(0, i - window_size), i):
            k = 0
            while i + k < len(data) and data[j + k] == data[i + k]:
                k += 1
            if k > match_len:
                match_pos = j
                match_len = k

        if match_len > 0 and i + match_len < len(data):
            next_char = data[i + match_len]
            encoded.append((i - match_pos, match_len, next_char))
            i += match_len + 1
        else:
            encoded.append((0, 0, data[i]))
            i += 1

    return encoded


data = "abracadabraaracadabra"
encoded_data = lz77_encode(data)
print("Encoded data:", encoded_data)
