========================================
Quick Start RNA解析
========================================

#. Genomonのインストール
#. コマンドの実行
#. 結果ファイルを見てみましょう


1. Genomonのインストール
^^^^^^^^
| HGCスパコンには、Genomonで使用する解析ソフトウェア(STAR等)が既にインストールされています。ご自身のユーザディレクトリにGenomonをインストールするだけで、解析をはじめることができます．
|
| → :doc:`install` にインストール方法を記載しました．
| DNA解析でインストールした場合は、再度インストールする必要はありません．GenomonはDNA解析とRNA解析の機能をもっています．
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
  $./genomon_pipeline rna /home/w3varann/testRNA/sample.csv {output_directory} genomon.cfg rna_task_param.cfg 
  # output_directoryには出力したいディレクトリを指定してください

| sample.csvの記載方法詳細は :doc:`sample_csv` にあります．
| testRNA/sample.csvの中身をみて、書き方を学んでいただくのも良いかと思います．
|
| commandの実行方法詳細は :doc:`command` に記載があります．
| 

実際のサンプルデータでも、sample.csvを記載して、上記のようにコマンドを実行すればOKです．

3. 結果ファイルを見てみましょう
^^^^^^^^

| 結果ファイルはこのように出力されます．

:fusion検出結果: {output_directory}/fusion/sample名/sample名_fusion_fusion.result.txt

| 我々が実行したサンプルデータの結果はこちらにありますので比べてみてください(v2.0.5で出力した結果)

:fusion検出結果: ~w3varann/test_rna/rna_result_v2.0.5/fusion/MCF-7_test/fusion_fusion.result.txt

| 結果ファイルの各項目の説明など詳細は :doc:`rna_results` に記述しました．



