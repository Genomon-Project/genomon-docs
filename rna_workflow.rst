========================================
RNA 解析パイプラインSchemes
========================================

 .. image:: image/rna_workflow.png

 Inputの方法は[fastq]の1種類です．サンプル設定ファイルで定義します．記載方法は :doc:`rna_sample_csv` を参照ください．
 
融合遺伝子検出 Task
-------------------

* **task_star_align** -- Starによるリファレンスゲノムにアライメントを実行します．
* **task_fusion_fusion** -- 融合遺伝子を検出します．

Post Analysis Task
-------------------
* **paplot** -- 各結果をplotしグラフを出力します．
* **post_analysis_starqc** -- 全サンプルのfastqのQuality Control結果を１つのファイルにマージして出力します．
* **post_analysis_fusionfusion** -- 全サンプルの融合遺伝子を検出を１つのファイルにマージして出力します．

その他Task
-----------

* **link_input_fastq** -- 出力ルートディレクトリにFASTQファイルをリンクします．
  
