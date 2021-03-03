import sys
import spacy
import re
from collections import Counter
from spacy.tokenizer import Tokenizer
from spacy.util import compile_infix_regex, compile_prefix_regex, compile_suffix_regex


def custom_tokenizer(nlp):
    infix_re = re.compile(r'''/''')
    prefix_re = compile_prefix_regex(nlp.Defaults.prefixes)
    suffix_re = compile_suffix_regex(nlp.Defaults.suffixes)

    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
                     suffix_search=suffix_re.search,
                     infix_finditer=infix_re.finditer,
                     token_match=None)


if __name__ == '__main__':
    input_filename, output_filename = sys.argv[1], sys.argv[2]
    with open(input_filename, 'r') as f:
        content = f.read()

    nlp = spacy.load("en_core_web_sm")
    nlp.tokenizer = custom_tokenizer(nlp)
    doc = nlp(content)
    result = list(filter(lambda x: x.pos_ == 'NUM' or x.pos_ == 'PROPN', doc))
    result = [str(i) for i in result]

    lines = list('<div>'+str(x)+'</div>' for x in Counter(result).values())
    with open(output_filename, 'w') as f:
        f.write('<div style="text-align: right;">')
        f.writelines(lines)
        f.write('</div>')