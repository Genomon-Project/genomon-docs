========================================
Quick Start DNA解析
========================================

*サンプルシートを記載してGenomonコマンドを1回実行するだけで、変異コール, SV, BamSummaryの結果がでてきます！*

1. Genomonのインストール
^^^^^^^^
| HGCスパコンには、Genomonで使用する解析ソフトウェアが既にインストールされています(ANNOVARは別途インストールが必要です)。そのためご自身のユーザディレクトリにGenomonをインストールするだけで、解析をはじめることができます．
|
| → :doc:`install` にインストール方法の記載があります．
|

2. コマンドの実行
^^^^^^^^

テストサンプルを実行してインストールが正しくされたか確かめましょう．テストサンプルは用意されていますので、それ実行してみましょう．

.. code-block:: bash
  
  # qloginする
  $qlogin
  # GenomonPipelineに移動
  $cd GenomonPipeline-v{バージョン}
  # 実行
  $./genomon_pipeline dna /home/w3varann/testdata/sample.csv {output_directory} dna_genomon.cfg
  # output_directoryには出力したいディレクトリを指定してください

| 実際のデータでも、ファイルパスとサンプルデータをsample.csv(ファイル名変更可)に記載して、上記のようにコマンドを実行すればOKです．まずはsample.csvの中身をみて、書き方を学んでいただくのが良いかと思います．commandの実行方法詳細は :doc:`dna_command` に記載があります．

3. 結果ファイルを見てみましょう
^^^^^^^^

* **bam** -- {output_directory}/bam/sample名/sample名_markdup.bam
* **変異Call(13件)** -- {output_directory}/mutation/sample名/sample名_genomon_mutations.result.txt
* **SV(0件)** -- {output_directory}/sv/sample名/sample名.genomonSV.result.txt
* **summary** -- {output_directory}/sv/sample名/sample名.xls

| 我々が実行したサンプルデータの結果はこちらにありますので比べてみてください

* **bam** -- ~w3varann/testdata/dna_result_v2.2.0/bam/sample_tumor/sample_tumor.markdup.bam
* **変異Call(13件)** -- ~w3varann/testdata/dna_result_v2.2.0/mutation/sample_tumor/sample_tumor_genomon_mutations.result.txt
* **SV(0件)** -- ~w3varann/testdata/dna_result_v2.2.0/sv/sample_tumor/sample_tumor.genomonSV.result.txt
* **summary** -- ~w3varann/testdata/dna_result_v2.2.0/summary/sample_tumor/sample_tumor.xls

| 結果ファイルの各項目の説明など詳細は :doc:`dna_results` に記述しました．
|
