.. genomon documentation master file, created by
   sphinx-quickstart on Thu Jul 30 15:55:28 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Genomon
========

Welcome
-------
Genomon は DNA,RNAseqのシークエンス結果を解析するパイプラインです．

DNA(Whole genome/Whole exome)の解析
  :変異call: non-codingの領域も高精度にCallできます！
  :SV検出:   数十～数百baseのindelも検出できます！
RNAseqの解析
  :Fusionの検出: 50bpのシークエンスリードでも解析できます！
  :発現解析    :


Quick start
-----------


Get Genomon
-----------
::

  git clone git@github.com:Genomon-Project/GenomonPipeline.git
Just run:
::

  python setup.py build
  python setup.py install [--user]
