========================================
Quick Start DNA解析
========================================

#. Genomonのインストール
#. コマンドの実行
#. 結果ファイルを見てみましょう

1. Genomonのインストール
^^^^^^^^
| HGCスパコンには、Genomonで使用する解析ソフトウェア(BWA,Samtools等)が既にインストールされています(ANNOVARは別途インストールが必要です)。そのためご自身のユーザディレクトリにGenomonをインストールするだけで、解析をはじめることができます．
|
| → :doc:`install` にインストール方法を記載しました．
|

2. コマンドの実行
^^^^^^^^

テストサンプルを実行してインストールが正しくされたか確かめましょう．テストサンプルは用意されていますので、それを使用して実行してみましょう．

.. code-block:: bash
  
  # qloginする
  $qlogin
  # GenomonPipelineに移動
  $cd GenomonPipeline-v{バージョン}
  # 実行
  $./genomon_pipeline dna /home/w3varann/testdata/sample.csv {output_directory} genomon.cfg dna_task_param.cfg 
  # output_directoryには出力したいディレクトリを指定してください

| sample.csvの記載方法詳細は :doc:`sample_csv` にあります．
| testdata/sample.csvの中身をみて、書き方を学んでいただくのも良いかと思います．
|
| commandの実行方法詳細は :doc:`command` に記載があります．
| 

実際のサンプルデータでも、sample.csvを記載して、上記のようにコマンドを実行すればOKです．

3. 結果ファイルを見てみましょう
^^^^^^^^

| 結果ファイルはこのように出力されます．

:bam: {output_directory}/bam/sample名/sample名_markdup.bam
:変異Call結果: {output_directory}/mutation/sample名/sample名_genomon_mutations.result.txt
:SV検出結果: {output_directory}/sv/sample名/sample名.genomonSV.result.txt
:summary結果: {output_directory}/sv/sample名/sample名.xls

| 我々が実行したサンプルデータの結果はこちらにありますので比べてみてください(v2.0.5で出力した結果)

:bam: ~w3varann/testdata/dna_result_v2.0.5/bam/sample_tumor/sample_tumor.markdup.bam
:変異Call(13件): ~w3varann/testdata/dna_result_v2.0.5/mutation/sample_tumor/sample_tumor_genomon_mutations.result.txt
:SV(0件): ~w3varann/testdata/dna_result_v2.0.5/sv/sample_tumor/sample_tumor.genomonSV.result.txt
:summary: ~w3varann/testdata/dna_result_v2.0.5/summary/sample_tumor/sample_tumor.xls

| 結果ファイルの各項目の説明など詳細は :doc:`dna_results` に記述しました．
|
| *サンプルシートを記載してGenomonコマンドを1回実行するだけで、*
| *変異コール, SV, BamSummaryの結果がでてきます！*
