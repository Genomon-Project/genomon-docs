.. genomon documentation master file, created by
   sphinx-quickstart on Thu Jul 30 15:55:28 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========
Overview
========

.. contents
    :depth: 2


Introduction
============

Welcome to genomon's documentation!

Genomon-exome は Exome シークエンスの結果であるFASTQファイルのマッピング，データ解析を行い Mutation の候補の一覧を出力するソフトウェアです．

ライセンスの元で自由に使用・改変・再配布が可能です．

Genomon-exome は様々なオープンソフトウェアを組み合わせたパイプラインと呼ばれるソフトです．

.. attention::

   - ヒトゲノム(hg19)のみに対応しています． 
   - HGCのスーパーコンピュータ Shirokane3 上で行うことを前提として記載しております． 

Genomon
=======


Genomon-exome は以下の特徴を備えています．

    cutadapt を使用してPCRアーティファクト（アダプタシークエンス）の除去が可能です．
    BWA (Burrows-Wheeler Aligner) を使用してFASTQをヒトゲノム (hg19) へのマッピングを行います．
    GATK (The Genome Analysis Toolkit) を使用して bamファイルのリアライメントを行います．
    Picard を使用してマッピング率やカバレージの情報を出力します．
    データ解析を行い Mutation 候補の一覧をExcelで表示可能なTSV形式で出力します．
    ANNOVAR を使用して Mutation の候補の一覧にアノテーションを付与します．
    Bioconductor のDNAcopy パッケージを使用してCopy Number data 解析を実施します．
    ヒトゲノム解析センター (HGC) のスーパーコンピュータ にのみ対応しています．
    1サンプルの解析が1日で完了します．同時に最大10サンプル程度実行できます (同時実行数はスパコンの利用コースに依存します)．




Indices and tables
==================

.. toctree::
    :maxdepth: 2

    quick_start
    sample
    param_sheet
    command
    result
    error_code
    about
    developers

.. note::

   These docs are maintained by the genomon development team. 

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

