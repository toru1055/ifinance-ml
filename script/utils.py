from janome.tokenizer import Tokenizer

def stems(text):
  t = Tokenizer()
  token_list = [token.surface for token in t.tokenize(text) if token.part_of_speech.count(u"数") == 0]
  return set(token_list)
