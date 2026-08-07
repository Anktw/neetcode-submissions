class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        def rabin_karp(pattern, text):
            m, n = len(pattern), len(text)

            if m > n:
                return False

            base = 256
            mod = 10**9 + 7

            pattern_hash = 0
            text_hash = 0
            h = 1

            # Compute h = base^(m-1) % mod
            for _ in range(m - 1):
                h = (h * base) % mod

            # Compute initial hashes
            for i in range(m):
                pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
                text_hash = (text_hash * base + ord(text[i])) % mod

            # Slide the window
            for i in range(n - m + 1):

                # Hashes match, verify characters
                if pattern_hash == text_hash:
                    if text[i:i + m] == pattern:
                        return True

                # Compute next window hash
                if i < n - m:
                    text_hash = (
                        base * (text_hash - ord(text[i]) * h)
                        + ord(text[i + m])
                    ) % mod

                    if text_hash < 0:
                        text_hash += mod

            return False

        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if rabin_karp(words[i], words[j]):
                    res.append(words[i])
                    break

        return res