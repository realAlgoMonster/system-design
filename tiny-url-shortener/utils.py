class Base:
    alphabet: str
    size: int
    decode_map: dict

    def __init__(self, alphabet: str):
        self.alphabet = alphabet
        self.size = len(alphabet)
        self.decode_map = dict()
        for i in range(self.size):
            self.decode_map[alphabet[i]] = i

    def encode_int(self, i: int) -> str:
        out = ''
        while i:
            i, idx = divmod(i, self.size)
            out = self.alphabet[idx] + out
        return out

    def decode_int(self, data: bytes) -> int:
        i = 0
        for char in data:
            i = i * self.size + self.decode_map[char]
        return i


BASE58 = Base('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')
