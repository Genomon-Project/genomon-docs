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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
HGCスパコンでのRNA解析に必要な手順をまとめました．

1. パイプライン設定ファイルを作成する
-------------------------------------

一般的なRNA解析のためのパイプライン設定ファイルがHGCスパコンに用意してあります．
パラメータを変更する際，rna_genomon.cfgをローカルディレクトリにコピーしてご使用ください．

.. code-block:: bash

  # RNA解析用パイプライン設定ファイルはこちらにあります
  /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/rna_genomon.cfg
  
2．テストサンプルでGenomonを実行してみる
----------------------------------------

テストサンプルでGenomonを実行してみましょう．Genomonが正しく使用できるか，パイプライン設定ファイルの記述が正しくできているか確認することができます．テストサンプルはファイルサイズが小さいので数分で処理が完了します．

.. code-block:: bash
  
  # qloginする
  qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {解析タイプ：rna} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}
  # 実行例
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh rna /home/w3varann/genomon_pipeline-2.2.0/test_data/test_rna/sample_config_RNA.csv /home/genomon/output_test_RNA /home/genomon/rna_genomon.cfg
  #
  # 解析タイプ
  #   'rna'を指定します．
  # サンプル設定ファイル
  #   /home/w3varann/genomon_pipeline-2.2.0/test_data/test_rna/sample_config_RNA.csvを指定します．
  # 出力ルートディレクトリ
  #   任意の出力ルートディレクトリを指定します．
  # パイプライン設定ファイル
  #   2.で作成したパイプライン設定ファイルを指定します．

3. サンプル設定ファイルを作成する
---------------------------------

サンプル設定ファイルには解析対象のFASTQを指定します．

サンプル設定ファイルの記載方法は  :doc:`rna_sample_csv` を参照ください．

4．Genomonを実行する
--------------------

作成したサンプル設定ファイルを指定して，Genomonを実行しましょう．

.. code-block:: bash
  
  # qloginする
  qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {解析タイプ：rna} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}
  # 実行例
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh dna /home/genomon/sample_config.csv /home/genomon/output_RNA /home/genomon/rna_genomon.cfg
  #
  # 解析タイプ
  #   'rna'を指定します．
  # サンプル設定ファイル
  #    1.で作成したサンプル設定ファイルを指定します．
  # 出力ルートディレクトリ
  #    任意の出力ルートディレクトリを指定します．
  # パイプライン設定ファイル
  #    2.で作成したパイプライン設定ファイルを指定します．

5．結果ファイルを確認する
-------------------------

結果ファイルは実行時に指定した 出力ルートディレクトリ以下に出力されます．

.. code-block:: bash

  # 融合遺伝子検出結果
  {出力ルートディレクトリ}/fusion/{サンプル名}/fusion_fusion.result.txt

結果ファイルの説明は :doc:`rna_results` を参照ください．
