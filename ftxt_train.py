#!/usr/bin/env python

import fasttext
import sys


mode = 'cbow'  # 'cbow' or 'skipgram'
input_file = './corpus/ftxt_noclz_corp.seg'
model_file = 'fasttext_' + mode + '.model'

if mode == 'cbow':
    model = fasttext.cbow(
        input_file=input_file,
        output=model_file,
        dim=200,
        min_count=3,
        word_ngrams=2,
        minn=3,
        thread=12)

if mode == 'skipgram':
    model = fasttext.cbow(
        input_file=input_file,
        output=model_file)
