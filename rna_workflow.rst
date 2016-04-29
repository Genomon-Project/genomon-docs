========================================
RNA 解析パイプラインSchemes
========================================

 .. image:: image/rna_workflow.png

 Inputの方法は[fastq]の1種類です．サンプル設定ファイルで定義します．記載方法は :doc:`rna_sample_csv` を参照ください．
 
融合遺伝子検出 Task
-------------------

* **task_star_align** -- Starによるリファレンスゲノムにアライメントを実行します．
* **task_fusion_fusion** -- 融合遺伝子を検出します．

その他Task
-----------

* **link_input_fastq** -- 出力ルートディレクトリにFASTQファイルをリンクします．
  
