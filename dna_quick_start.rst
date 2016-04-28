Quick Start DNA解析 (HGCスパコン)
=================================

サンプル設定ファイルをつくる
----------------------------

サンプル設定ファイルには解析対象のFASTQやBAMファイルや，どの解析(Mutation Call，SV検出，BAMのQuality Check)を実行するのかを指定します．

結果ファイルの各項目の説明など詳細は :doc:`sample_conf` に記述しました．

パイプライン設定ファイルをつくる
--------------------------------

最適化されたパラメータが記載されたパイプライン設定ファイルをHGCスパコンにあります。こちらのファイルを


DNA解析を実行する
-----------------

.. code-block:: bash
  
  # qloginする
  $qlogin
  # GenomonPipelineに移動
  $cd GenomonPipeline-v{バージョン}
  # 実行
  $./genomon_pipeline dna /home/w3varann/testdata/sample.csv {output_directory} dna_genomon.cfg
  # output_directoryには出力したいディレクトリを指定してください

| 実際のデータでも、ファイルパスとサンプルデータをsample.csv(ファイル名変更可)に記載して、上記のようにコマンドを実行すればOKです．まずはsample.csvの中身をみて、書き方を学んでいただくのが良いかと思います．commandの実行方法詳細は :doc:`dna_command` に記載があります．

結果ファイルを見てみましょう
^^^^^^^^

| 結果ファイルは実行時に指定した output_directory に出力されます．

.. code-block:: bash

  # bam
  {output_directory}/bam/sample名/sample名_markdup.bam
  # 変異Call(13件)
  {output_directory}/mutation/sample名/sample名_genomon_mutations.result.txt
  # SV(0件)
  {output_directory}/sv/sample名/sample名.genomonSV.result.txt
  # summary
  {output_directory}/sv/sample名/sample名.xls

| 我々が実行したサンプルデータの結果はこちらにありますので比べてみてください．

.. code-block:: bash

  # bam
  ~w3varann/testdata/dna_result_v2.2.0/bam/sample_tumor/sample_tumor.markdup.bam
  # 変異Call(13件)
  ~w3varann/testdata/dna_result_v2.2.0/mutation/sample_tumor/sample_tumor_genomon_mutations.result.txt
  # SV(0件)
  ~w3varann/testdata/dna_result_v2.2.0/sv/sample_tumor/sample_tumor.genomonSV.result.txt
  # summary
  ~w3varann/testdata/dna_result_v2.2.0/summary/sample_tumor/sample_tumor.xls

| 結果ファイルの各項目の説明など詳細は :doc:`dna_results` に記述しました．
|
