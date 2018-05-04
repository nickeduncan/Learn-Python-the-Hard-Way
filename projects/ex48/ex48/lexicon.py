def check(word):
    lexicon = {
        'direction': 'north south east west down up left right back'.split(),
        'verb': 'go stop kill eat'.split(),
        'stop': 'the in of from at it'.split(),
        'noun': 'door bear princess cabinet'.split()
    }
    for key in lexicon:
        # if a word is in the lexicon
        if word in lexicon[key]:
            return (key, word)
        elif word.isdigit():
            return ('number', int(word))
        elif not word.isdigit():
            return ('error', word)

def scan(sentence):
    words = sentence.split()
    result = []
    for word in words:
        result.append(check(word))

    return result

