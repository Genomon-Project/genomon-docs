========================================
Output
========================================

出力ディレクトリ階層
---------------------
::

  プロジェクトルートディレクトリ
    -bam
      -各サンプル名
        -サンプル名.markdup.bam
    	-サンプル名.markdup.bam.bai
	-サンプル名.markdup.bam.md5
	-サンプル名.markdup.metrics
    -fastq
	-各サンプル名
	  -1_1.fastq
	  -1_2.fastq
    -log
      -qsubのログ
    -mutation
      -各サンプル名
      -サンプル名.genomon_mutations.result.txt
    -script
      -qsub実行script
    -sv 
      -各サンプル名
      -サンプル名.genomon_SV.result.txt
	
	
bamディレクトリ
-----------

:sample名.markdup.bam: bamファイル
:sample名.markdup.bam.bai: bam indexファイル
:sample名.markdup.bam.md5: bamのmd5
:sample名.markdup.metrics: mark duplicateした時に出力されるduplicateリードの情報

| [fastq][bam_tofastq]から実行した場合は、上記4つのファイルが出力されます.
| [bam_import]から実行した場合は、対象のbamファイルがこのディレクトリにlinkされます.
  

fastqディレクトリ
-----------

:1_1.fastq 1_2.fastq: ペアエンドのfastqファイル.

| [fastq]から実行した場合は、このディレクトリにfastqファイルがlinkされます.
| [bam_tofastq]から実行した場合は、bamからconvertされたfastqファイルがこのディレクトリに出力されます.

  
logディレクトリ
-----------
  
qsubのログファイルが出力されます.


mutationディレクトリ
----------------

:サンプル名.genomon_mutations.result.txt: 変異Callの結果.

  
scriptディレクトリ
--------------

| qsubされたshell scriptです.
| こちらのscriptの中身をみると、どのような処理が実行されたか一目瞭然です.
  
  
SVディレクトリ
----------------

:サンプル名.genomon_SV.result.txt: SV検出の結果.
