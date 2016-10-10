#!/bin/bash

corp_raw=/data1/qspace/travischen/corpus/doc_clz_corpus

cat $corp_raw/* | awk -F'\t' '{if($2!="") print $2}' | sort | uniq > ftxt_noclz_corp
