RNA 解析コマンドを実行する
==========================

コマンドの使用方法です．

.. code-block:: bash

  # Genomonを実行する
  genomon_pipeline {解析タイプ} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}
  # 実行例
  genomon_pipeline rna /home/genomon/sample_config_RNA.csv /home/genomon/output_test_RNA /home/genomon/rna_genomon.cfg
  
`解析タイプ　'dna'，'rna'`
    DNA解析をする場合は，dna を，RNA解析をする場合は，rna を指定します．
`サンプル設定ファイル　'sample_config.csv'`
    解析対象のファイル（FASTQ）のパスなどを記載したファイルを作成し，そのファイル名を指定します．
`出力ルートディレクトリ　'output_root_directory'`
    出力ルートディレクトリを指定します．結果がこのディレクトリ以下に出力されます．
`パイプライン設定ファイル　'genomon.cfg'`
    パイプライン設定ファイルを指定します．

