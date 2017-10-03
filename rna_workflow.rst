========================================
RNA 解析パイプラインSchemes
========================================

 .. image:: image/rna_workflow.png

 | Inputの方法は [fastq], [bam_tofastq], [bam_import] の3種類あります．これらはサンプル設定ファイルで定義します．
 |
 | 解析は融合遺伝子検出, 発現量解析, Quality Control出力の3種類あり， [fusion], [expression], [qc] の項目をサンプル設定ファイルで定義すると実行されます．
 |
 | [fusion], [expression], [qc]の各解析が完了した後，自動的にpost Analysis Taskが実行されます．実行したくない場合は，パイプライン設定ファイルを変更する必要があります．
 |
 | サンプル設定ファイルの記載方法は :doc:`rna_sample_csv` をご参照ください．
 | パイプライン設定ファイルを変更する場合は :doc:`rna_config_info` をご参照ください．
 
マッピング Task
-----------------------
* **task_star_align** -- Starによるリファレンスゲノムにアライメントを実行します．副生成物として，QCの結果を出力します.

融合遺伝子検出 Task
-------------------

* **task_fusion_count** -- Count supporting read pairs for each chimera junction．
* **task_fusion_merge** -- Merge chimeric junction count file.
* **task_fusion_fusion** -- 融合遺伝子を検出します．

発現量解析 Task
-------------------

* **task_genomon_expression** -- 発現量解析を行います．

| 発現量解析の概要については https://github.com/Genomon-Project/GenomonExpression を参照してください．
|

Post Analysis Task
-------------------
* **paplot** -- 各結果をplotしグラフを出力します．
* **post_analysis_starqc** -- 全サンプルのfastqのQuality Control結果を１つのファイルにマージして出力します．
* **post_analysis_fusionfusion** -- 全サンプルの融合遺伝子を検出を１つのファイルにマージして出力します．

その他Task
----------
* **link_input_fastq** -- 指定したFASTQを出力ルートディレクトリ内にリンクします．
* **link_import_bam** -- 指定したBAMを出力ルートディレクトリ内にリンクします．
* **bam2fastq** -- 指定したBAMをFASTQにConvertし出力ルートディレクトリ内に出力します．

