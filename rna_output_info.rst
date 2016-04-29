RNA 解析で出力されるファイルについて
====================================

出力ディレクトリ階層
---------------------

 .. image:: image/rna_tree.png
  :scale: 110%
	
	
マッピング結果（Bamファイル)
-----------------------
| {出力ルートディレクトリ}/star/{サンプル名}ディレクトリ内に出力されます．

* **{サンプル名}.Aligned.sortedByCoord.out.bam** -- Bamファイル．
* **{サンプル名}.Aligned.sortedByCoord.out.bam.bai** -- Bam indexファイル．


Fusion検出結果
-----------------------
| {出力ルートディレクトリ}/fusion/{サンプル名}ディレクトリ内に出力されます．

* **{サンプル名}_fusion_fusion.result.txt** -- 融合遺伝子検出結果ファイル．
* **{サンプル名}_star.fusion.result.txt** -- 中間ファイル．デバッグ用．

config log script
-----------------------

| 実行時のパラメータやツールの設定情報，log，使用したScriptが保存されます．

