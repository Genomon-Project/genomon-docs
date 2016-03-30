========================================
RNA解析パイプラインschemes
========================================

 .. image:: image/rna_workflow.png

 | Inputの方法は
 | [fastq]の1種類です．sample confで定義します．
 | 記載方法は :doc:`sample_csv` をみてください．
 
 | Fustion検出が実行されます．
 

Fusion検出
-----------------------

  :task_star_align: starによるリファレンスゲノムにアライメントを実行します．
  :task_fusion_fusion: fusionを検出します．


その他Task
--------------------------

  :link_input_fastq: project root directory内にFASTQファイルをリンクします．
  
