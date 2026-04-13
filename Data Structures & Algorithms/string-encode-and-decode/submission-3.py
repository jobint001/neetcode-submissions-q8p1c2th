class Solution:

    def encode(self, strs: List[str]) -> str:
        enstr = ""
        for word in strs:
            enstr+="`"+word
        enstr+="`"
        print(enstr)
        return enstr

    def decode(self, s: str) -> List[str]:
        words = []
        i=1
        j=1
        for k in range (0,len(s)):
            if k==0:
                continue
            if s[k]=="`":
                words.append(s[i:j])
                i=j+1
                j+=1
            else:
                j+=1
        return words