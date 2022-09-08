def str2xor(messages, key):
    res = ""
    for index, msg in enumerate(messages):
        res += chr( ord(msg) ^ ord(key[index % len(key)]) )
    print(res)

if __name__ == '__main__':
    ip = "192.168.111.1"   # E\AZZSAZTBEET
    port = "7000"          # CUCD

    key = "testkey"
    str2xor(ip, key)
    str2xor(port, key)
