========================================
RNA解析で出力されるファイルについて
========================================

出力ディレクトリ階層
---------------------

 .. image:: image/rna_tree.png
  :scale: 100%
	
	
マッピング結果（BAM)
-----------------------
| star/$sample(各サンプル)ディレクトリ内に出力されます．

* **${sample}.Aligned.sortedByCoord.out.bam** -- BAMファイル．
* **${sample}.Aligned.sortedByCoord.out.bam.bai** -- BAM indexファイル．


Fusion検出結果
-----------------------
| fusion/$sample(各サンプル)ディレクトリ内に出力されます．

* **${sample}_fusion_fusion.result.txt** -- fusionfusion結果ファイル．
* **${sample}_star.fusion.result.txt** -- 中間ファイル．デバッグ用．

config log script
-----------------------

| 実行時のパラメータやツールの設定情報、log、使用したScriptが保存されます．

