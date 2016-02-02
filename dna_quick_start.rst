========================================
Quick Start DNA解析
========================================

#. Genomon2のインストール
#. コマンドの実行
#. 結果ファイルを見てみましょう

1. Genomonのインストール
^^^^^^^^
| HGCスパコンには、Genomonで使用する解析ソフトウェア(BWA,Samtools等)が既にインストールされています(ANNOVARは別途インストールが必要です)。そのためご自身のユーザディレクトリにGenomonをインストールするだけで、解析をはじめることができます．
|
| → :doc:`install` にインストール方法を記載しました．
|

2. テストサンプルの実行
^^^^^^^^

テストサンプルを実行してインストールが正しくされたか確かめましょう．テストサンプルは用意されていますので、それを使用しましょう．

.. code-block:: bash
  
  # qloginする
  $qlogin
  # GenomonPipelineに移動
  $cd GenomonPipeline-v{バージョン}
  # 実行
  $./genomon_pipeline dna /home/w3varann/testdata/sample.csv {output_directory} genomon.cfg dna_task_param.cfg 
  # output_directoryには出力したいディレクトリを指定してください

| sample.csvの記載方法は :doc:`sample_csv` に記載があります．
| testdata/sample.csvの中身をみて、書き方を学んでいただくのも良いかと思います．
|
| commandの実行方法詳細は :doc:`command` に記載があります．
| 

実際のサンプルデータでも、sample.csvを記載して、上記のようにコマンドを実行すればOKです．

結果ファイルを見てみましょう
^^^^^^^^
:bam: output_root_directory/bam/sample/sample_markdup.bam
:変異Call結果: output_root_directory/mutation/sample名/sample名_genomon_mutations.result.txt
:SV検出結果: output_root_directory/sv/sample名/sample名.genomonSV.result.txt

| 結果ファイルの各項目の説明は :doc:`dna_results` に記載があります．

