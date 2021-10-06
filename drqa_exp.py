import drqa.tokenizers
drqa.tokenizers.set_default('corenlp_classpath', '..\libraries\corenlp\*')

from drqa.tokenizers import CoreNLPTokenizer
tok = CoreNLPTokenizer()
print(tok.tokenize('hello world').words())
