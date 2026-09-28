class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder =""
        for s in strs:
            encoder += str(len(s)) + "#" + s
        return encoder

    def decode(self, encoder: str) -> List[str]:
        decoder = []
        i =0
        while i < len(encoder):
            j = i
            while encoder[j] != "#":
                j += 1
            length = int(encoder[i:j])
            i = j+1
            s= encoder[i:i+length]
            decoder.append(s)
            i = i + length

        return decoder

    