#!/bin/bash

# prepare corpus and segmentations
#cat corpus/ftxt_noclz_corp | /data1/qspace/travischen/segmentation/seg_jieba/seg_ftxt.py > corpus/ftxt_noclz_corp.seg.tmp
#cat corpus/ftxt_noclz_corp.seg.tmp | sort | uniq | perl -MList::Util=shuffle -e'print shuffle<>' > corpus/ftxt_noclz_corp.seg
#rm -f corpus/ftxt_noclz_corp.seg.tmp

# train fasttext model
ftxt_train.py

# test fastext model
ftxt_test.py
