========================================
RNA 解析パイプラインSchemes
========================================

GenomonパイプラインのDNA解析において，各工程の流れを解説します．

 .. image:: image/rna_workflow.png

 | サンプル設定ファイルの記載方法は :doc:`rna_sample_csv` を参照ください．
 | パイプライン設定ファイルを変更する場合は :doc:`rna_config_info` を参照ください．
 
1. 入力とアライメント
--------------------------------

Inputの方法は [fastq], [bam_tofastq], [bam_import] の3種類あります．これらはサンプル設定ファイルで定義します．

:fastq: fastqを扱いやすい大きさに分割してからアライメントを行います
:bam_tofastq: bamファイルを一旦fastqに変換し，アライメントします．Genomon以外でアライメントしたbamなどはこちらを使用してください
:bam_import: アライメント済みのbamファイルが対象です．アライメントは行わず解析を行います
:task_star_align: Starによるリファレンスゲノムにアライメントを実行します．副生成物として，QCの結果を出力します

2. 融合遺伝子検出 (fusion)
------------------------------

[fusion], [expression], [qc] の項目をサンプル設定ファイルで定義すると実行されます．

:task_fusion_count, task_fusion_merge, task_fusion_fusion: 融合遺伝子を検出します．
:post_analysis: 全サンプルのfusionを１つのファイルにマージして出力します．
:paplot: レポートを出力します．

3. 発現量解析 (expression)
--------------------------------

[fusion], [expression], [qc] の項目をサンプル設定ファイルで定義すると実行されます．

* **task_genomon_expression** -- 発現量解析を行います．

| 発現量解析の概要については https://github.com/Genomon-Project/GenomonExpression を参照してください．

4. Quality Control (qc)
--------------------------------------

RNAではQCの値がStarの副生成物として作成されるため，DNAのような専用の工程はありません．
[qc] の項目をサンプル設定ファイルで定義するとレポートとして出力されます．

:post_analysis: 全サンプルのfusionを１つのファイルにマージして出力します．
:paplot: レポートを出力します．

