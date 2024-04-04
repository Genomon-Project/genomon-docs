RNA 解析コマンドを実行する
==========================

コマンドの使用方法です．

.. code-block:: bash

  # Genomonを実行する
  genomon_pipeline {解析タイプ} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}



:解析タイプ: ``dna`` / ``rna``

  | rna を指定します．

:サンプル設定ファイル: ``/path/to/sample_config.csv``

  | 解析対象のファイル（FASTQやBAM）のパスなどを記載したファイルです．ファイル名は任意です．
  | Genomonコマンドを実行するには，まずこのファイルを作成する必要があります．
  | 作成方法は :doc:`rna_sample_csv` を参照してください．
  
:出力ルートディレクトリ:  ``/path/to/output_root_directory``
  
  | Genomonの結果を出力するディレクトリです．
  | Genomonの結果はこのディレクトリ配下にすべて出力されます．
  
:パイプライン設定ファイル:  ``/path/to/genomon.cfg``
  
  | GenomonのRNA解析用のパイプライン設定ファイルです．ファイル名は任意です．
  | 詳しくは :doc:`rna_config_info` を参照してください．
  
  
  