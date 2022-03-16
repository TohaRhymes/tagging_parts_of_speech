from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    Doc
)

from input_functions import (
    file_text_input,
    manual_text_input,
    file_pattern_input,
    manual_pattern_input)
import argparse


def prepare_doc(text: str, segmenter: Segmenter, morph_tagger: NewsMorphTagger) -> Doc:
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    return doc


def return_fragments_morphology(doc: Doc, pattern_len: int, pattern: list) -> list:
    text_len = len(doc.tokens)
    for index in range(text_len - pattern_len + 1):
        if pattern == [doc.tokens[j].pos for j in range(index, index + pattern_len)]:
            print(' '.join([doc.tokens[j].text for j in range(index, index + pattern_len)]))


def processing(text: str, pattern_len: int, pattern: str):
    print('Обработка...\n')
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)

    doc = prepare_doc(text, segmenter, morph_tagger)
    print('ОТВЕТ:')
    return_fragments_morphology(doc, pattern_len, pattern)


def parse_args() -> (str, str):
    parser = argparse.ArgumentParser()

    parser.add_argument("-text", "--text_path", help="Path to file with input text.", type=str)
    parser.add_argument("-tmpl", "--template_path", help="Path to file with tag template", type=str)

    args = parser.parse_args()
    return args.text_path, args.template_path


def main():
    text_path, template_path = parse_args()

    if text_path:
        text = file_text_input(text_path)
    else:
        text = manual_text_input()

    if template_path:
        pattern, pattern_len = file_pattern_input(template_path)
    else:
        pattern, pattern_len = manual_pattern_input()

    processing(text, pattern_len, pattern)


if __name__ == '__main__':
    main()
