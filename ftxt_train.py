#!/usr/bin/env python

import fasttext
import sys


mode = 'skipgram'  # 'cbow' or 'skipgram'
input_file = './corpus/ftxt_noclz_corp.seg'
model_file = 'fasttext_' + mode + '.model'

# Get understood of all the params!!!
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
    model = fasttext.skipgram(
        input_file=input_file,
        output=model_file,
        dim=200,
        epoch=3,
        min_count=5,
        neg=3,
        word_ngrams=2,
        bucket=3500000,
        minn=3,
        thread=16,
        silent=0)
