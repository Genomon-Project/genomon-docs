Quick Start DNA解析
===================

こちらはHGCスパコン利用者向けのページになります．HGCスパコン以外でGenomonをご使用の方はGenomonをインストールしていただく必要があります．Genomonインストール方法については，:doc:`install` を参照してください．

用意してあるサンプルデータを使用してGenomonを動かしてみましょう．

HGCスパコンでのDNA解析に必要な手順をまとめました．

| 1. サンプル設定ファイルをつくる
| 2．パイプライン設定ファイルをつくる
| 3．Genomonを実行する
| 4．結果ファイルを確認する

1. サンプル設定ファイルを作成する
---------------------------------

サンプル設定ファイルには解析対象のFASTQやBAMファイル，どの解析（変異コール，SV検出，BAMのQuality Control)を実行するのかを指定します．

サンプル設定ファイルの記載方法は  :doc:`dna_sample_csv` を参照ください．

2. パイプライン設定ファイルを作成する
-------------------------------------

最適化されたパラメータが記載されたパイプライン設定ファイルがHGCスパコンに用意してあります．

.. code-block:: bash

  # Exome解析用パイプライン設定ファイル
  /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_exome_genomon.cfg
  # Whole Genome解析用パイプライン設定ファイル
  /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_wgs_genomon.cfg


2-2. ANNOVARを使用したい場合、ANNOVARのインストールをします

| ANNOVARのダウンロードにはユーザ登録 (User License Agreement) が必要です．
| http://www.openbioinformatics.org/annovar/annovar_download_form.php
| ANNOVARのホームページにてユーザ登録 (User License Agreement) が完了した後に，登録したメールアドレスにANNOVARをダウンロードするためのリンクが記載されたメールが届きます．そのリンクを使用してANNOVARをダウンロードします．ダウンロード後はANNOVARのPerlスクリプトを使用して各種データ (dbsnp131など) をダウンロードします．

.. code-block:: bash

  # Genomonで必要なANNOVARのデータベースをダウンロードします．Copy and Pasteして使ってください． 
  DATABASE_LIST="
  refGene
  avsift
  ljb26_all
  cosmic68wgs
  cosmic70
  esp6500siv2_all
  1000g2010nov
  1000g2014oct
  snp131
  snp138
  snp131NonFlagged
  snp138NonFlagged
  clinvar_20150629
  "
  for DATABASE in $DATABASE_LIST
  do
    ./annotate_variation.pl -buildver hg19 -downdb -webfrom annovar $DATABASE humandb/
  done
  ./annotate_variation.pl -buildver hg19 -downdb cytoBand humandb/
  ./annotate_variation.pl -buildver hg19 -downdb genomicSuperDups humandb/

ANNOVARを使用するようにdna_genomon.cfgを編集する．以下の2か所の変更をお願いします．

.. code-block:: bash

  [SOFTWARE]
  annovar = [ANNOVARのパスをダウンロードしたANNOVAR]に変更する．
  (例)annovar = /home/genomon/tools/annovar

  [annotation]
  active_annovar_flag = False
  をTrueに変更する (ANNOVARの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．

2-3. HGVDの使用について

| HGVDのサイトのをお読みいただいた上、使用規約等に問題がなければdna_genomon.cfgを編集する
| http://www.genome.med.kyoto-u.ac.jp/SnpDB/about.html

.. code-block:: bash

  active_HGVD_flag = False
  をTrueに変更する (HGVDの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．

3．Genomonを実行する
--------------------

作成した設定ファイルを指定して、Genomonを実行しましょう．

.. code-block:: bash
  
  # qloginする
  $qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {解析タイプ：dna} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}
  # 解析タイプ
  #    'dna'を指定します．
  # サンプル設定ファイル
  #    1.で作成したサンプル設定ファイルを指定します．
  # 出力ルートディレクトリ
  #    任意の出力ルートディレクトリを指定します．
  # パイプライン設定ファイル
  #    2.で作成したパイプライン設定ファイルを指定します．

4．結果ファイルを確認する
-------------------------

結果ファイルは実行時に指定した 出力ルートディレクトリに以下に出力されます．

.. code-block:: bash

  # Mutation Call結果
  {出力ルートディレクトリ}/mutation/sample名/sample名_genomon_mutations.result.txt
  # SV検出結果
  {出力ルートディレクトリ}/sv/sample名/sample名.genomonSV.result.txt
  # summary
  {出力ルートディレクトリ}/sv/sample名/sample名.xls

結果ファイルの各項目の説明など詳細は :doc:`dna_results` を参照ください．

