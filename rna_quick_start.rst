Quick Start RNA解析
===================

こちらはHGCスパコン利用者向けのページになります．HGCスパコン以外でGenomonをご使用の方はGenomonをインストールしていただく必要があります．Genomonインストール方法については，:doc:`install` を参照してください．

.. code-block:: none 

  HGCスパコンでRNA解析に必要な手順
    1．パイプライン設定ファイルをつくる
    2．テストサンプルでGenomonを実行してみる
    3. サンプル設定ファイルをつくる
    4．Genomonを実行する
    5．結果ファイルを確認する

HGCスパコンでRNA解析に必要な手順
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
HGCスパコンでのRNA解析に必要な手順をまとめました．

1. パイプライン設定ファイルを作成する
-------------------------------------

一般的なRNA解析のためのパイプライン設定ファイルがHGCスパコンに用意してあります．
パラメータを変更する際，rna_genomon.cfgをローカルディレクトリにコピーしてご使用ください．

.. code-block:: bash

  # RNA解析用パイプライン設定ファイルはこちらにあります
  /share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/rna_genomon.cfg
  
2．テストサンプルでGenomonを実行してみる
----------------------------------------

テストサンプルでGenomonを実行してみましょう．Genomonが正しく使用できるか，パイプライン設定ファイルの記述が正しくできているか確認することができます．テストサンプルはファイルサイズが小さいので数分で処理が完了します．

.. code-block:: bash
  
  # qloginする
  qlogin
  # Genomonを実行する
  bash /share/pub/genomon/genomon_pipeline-2.6.2/genomon_script/genomon_pipeline_HGC.sh rna /share/pub/genomon/genomon_pipeline-2.6.2/sample_sheet/test_rna/MCF-7_sample.csv {出力ルートディレクトリ} {1.で作成したパイプライン設定ファイル}
  #
  # 解析タイプ
  #   'rna'を指定します．
  # サンプル設定ファイル
  #   /share/pub/genomon/genomon_pipeline-2.6.2/sample_sheet/test_rna/MCF-7_sample.csv を指定します．
  # 出力ルートディレクトリ
  #   任意の出力ルートディレクトリを指定します．
  # パイプライン設定ファイル
  #   1.で作成したパイプライン設定ファイルを指定します．

3. サンプル設定ファイルを作成する
---------------------------------

| サンプル設定ファイルには解析対象のFASTQやBAMファイル，どの解析（融合遺伝子，発現量，BAMのQuality Control）を実行するのかを指定します．
| サンプル設定ファイルの記載方法は  :doc:`rna_sample_csv` を参照ください．
| サンプル設定ファイルの名前は任意で設定可能ですが，拡張子は ``.csv`` としてください．
| 

4．Genomonを実行する
--------------------

作成したサンプル設定ファイルを指定して，Genomonを実行しましょう．

.. code-block:: bash
  
  # qloginする
  qlogin
  # Genomonを実行する
  bash /share/pub/genomon/genomon_pipeline-2.6.2/genomon_script/genomon_pipeline_HGC.sh rna {3.で作成したサンプル設定ファイル} {出力ルートディレクトリ} {1.で作成したパイプライン設定ファイル}
  #
  # 解析タイプ
  #   'rna'を指定します．
  # サンプル設定ファイル
  #    3.で作成したサンプル設定ファイルを指定します．拡張子は.csvにしてください．
  # 出力ルートディレクトリ
  #    任意の出力ルートディレクトリを指定します．
  # パイプライン設定ファイル
  #    1.で作成したパイプライン設定ファイルを指定します．

5．結果ファイルを確認する
-------------------------

結果ファイルは実行時に指定した 出力ルートディレクトリ以下に出力されます．

.. code-block:: bash

  # 発現量解析結果
  {出力ルートディレクトリ}/expression/{サンプル名}/{サンプル名}.sym2fkpm.txt
  
  # 融合遺伝子検出結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion_filt.txt
  
  # BAMのQuality Controlの結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_starqc.txt
  
  # paplotの結果
  # index.htmlをクリックすることで結果が表示されます．
  {出力ルートディレクトリ}/paplot/{サンプル設定ファイル名}

結果ファイルの説明は :doc:`rna_results` を参照ください．
