#!/usr/bin/env python
# -*- coding=utf-8 -*-

import fasttext
import sys
from sklearn.metrics.pairwise import cosine_similarity


mode = 'cbow'  # 'cbow' or 'skipgram'
model_file = 'fasttext_' + mode + '.model.bin'

model = fasttext.load_model(model_file)

tar_words = ['大学', '刺激']
can_words = ['学校', '高校', '大学', '男子', '惊悚', '惊讶', '开心', '猥琐']


for tar_word in tar_words:
    for can_word in can_words:
        dist = cosine_similarity([model[tar_word.decode('utf8')]],
                                 [model[can_word.decode('utf8')]])[0][0]
        print '\t'.join([tar_word, can_word, str(dist)])

