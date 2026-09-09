#frequency identify

word = "python programming is simple"

set_word = set(word)

ch_count = {}

for ch in set_word:

    ch_count [ch] = word.count(ch)

print(ch_count)    

