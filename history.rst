

リリースノート
-------------------


Genomon2.4.1
^^^^^^^^^^^^
 | ・mutation_merge.pyのファイルにバイナリ文字列が挿入されているのを修正．HGVDのヘッダーに影響がありました．

 | ・pysamのバージョンを0.9.1.4で固定にしました．

Genomon2.4.0
^^^^^^^^^^^^

 | DNA解析パイプライン
 | ・変異コールがskip duplicate ON/OFFの設定ができるようになりました．SVはskip duplicate ON/OFFできません． skip duplicateのON/OFFはパイプライン設定ファイル(dna_genomon.cfg)で変更が可能です．デフォルトではskip duplicateします．  

 | パイプライン設定ファイルの変更する箇所：  
 | [fisher_mutation_call]、[indel_filter]タグ  
 | 変更前）skip duplicateする  
 | --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"  
 | 変更後）skip duplicate しない  
 | --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL"  

 | [realignment_filter]タグ  
 | 変更前）skip duplicateする  
 | --exclude_sam_flags 3328  
 | 変更後）skip duplicate しない  
 | --exclude_sam_flags 2304  

 | [breakpoint_filter]  
 | 変更前）skip duplicateする  
 | --exclude_sam_flags 3332  
 | 変更前）skip duplicate しない  
 | --exclude_sam_flags 2308  

 | [eb_filter]
 | 変更前）skip duplicateする  
 | filter_flags = UNMAP,SECONDARY,QCFAIL,DUP  
 | 変更前）skip duplicate しない  
 | filter_flags = UNMAP,SECONDARY,QCFAIL  

 | 変更するパターンとしては、sam flagsを操作するものと、samtools mpileupの ffオプションで特定のリードをスキップしないようにする2パターンがあります．samflagsについては以下のページを参照してフラグを確認してください．  
 | https://broadinstitute.github.io/picard/explain-flags.html  
 | samtools mpileup オプションについては、samtools mpileupのヘルプを出してご確認ください．  

 | ・変異コールでHGVDの最新バージョンとExACのアノテーションが付くようになりました。パイプライン設定ファイルの以下のフラグをTrueにすることでご使用いただけます。Genomon2.3で出力されるHGVDはHGVD_2013へと名称を変更しました。
 | active_HGVD_2013_flag = False
 | active_HGVD_2016_flag = False
 | active_ExAC_flag = False

 | ・パイプライン設定ファイル(dna_genomon.cfg)の変異コールのパラメータの記載方法がv2.3と異なります． v2.3のパラメータの「fisher_thres_hold」と 
 | 「fisher_pval-log10_thres」の違いがわかり難いなどの、ご指摘をうけ変更しました．v2.4では直感的に分かりやすいように変更し全体的に統一性を持たせました．
 
 | RNA解析パイプライン
 | ・	STARのバージョンアップをしました.
 | 2.4.0k→2.5.2aにしました．それに伴いSTARのオプションも変更しております．これにより特異度が高くなります．

 | ・	fusionfusionでcontrolpanelが使用できるようになりました．

 | ・	発現量解析ができるようになりました．

 | ・	[bam_import]と[bam_tofastq]機能がRNAパイプラインにも追加されました

 | ・	QCが出力されるようになりました．

 | 新機能の追加により、サンプル設定ファイルの記載方法が変わります．記載方法につきましてはドキュメントをご確認ください．
 | http://genomon.readthedocs.io/ja/latest/rna_sample_csv.html

 | ・	fusionfusionにxxxxx.result.filt.txtが新たに出力されます．こちらはDNAパイプラインと同様に適切な値でフィルタ済みのファイルになります．
 | フィルタ機能の詳細：
 |  １．候補のポジションが“MT”か“GL0”で始まるヒトゲノムのscaffold  (assembled contigs separated by gaps)であった場合、候補からフィルタされます．
 |  ２．fusion元とfusion先の遺伝子名が同じで合ったら候補からフィルタします．こちらはrna_genomon.cfgの以下のパラメータ filt_paramsを変更することにより、このフィルタをなくすことができます．xxxxx.result.txtにはフィルタ前の候補一覧が出力されるので、このフィルタにより、必要な候補が削除されていないか確認できます．
 | [fusionfusion]
 | filt_params = --filter_same_gene

 | ・bam_importはGenomonパイプラインのSTARでアライメントされたBAMファイルを前提としています．以下の4つのファイルが存在していなければbam importエラーとなります．
 | {サンプル名}.Aligned.sortedByCoord.out.bam
 | {サンプル名}.Aligned.sortedByCoord.out.bam.bai
 | {サンプル名}.Chimeric.out.sam
 | {サンプル名}.Log.final.out
 | サンプルCSVに記載する方法はDNAパイプラインと同じでBAMファイルのみを指定してください．指定したBAMファイルのprefixから同じディレクトリの上記のファイルを探します．[bam_tofastq]はBAMファイルだけあれば大丈夫です．記載方法もDNAパイプラインと同じです．

 | ・ RNA パイプラインにfusionfusionとQC(starにより生成)のプロジェクト単位にマージしたファイルが(post_analysisで)出力されるようになりました.
 | post_analysisのfusionfusionは、xxxxxx.result.filt.txtの結果をマージしています．QCはstarディレクトリのxxxxxx.Log.final.outを利用しています． 

 | ・fusionfusionとQC情報がpaplotで出力されるようになりました． 

 | ・mm10(GRCm38)でも解析できるようになりました．mm10で解析する際には以下のGRCm38と記載されているパイプライン設定ファイルをご使用ください．mm10以 外の解析も可能です．その場合はユーザ様ご自身で設定ください．

 | ・下位バージョン（v2.3.0）のパイプライン設定ファイルはご使用できません．以下のv2.4.0用のファイルをご使用ください．ANNOVARやinhouseの設定がFALSEになっているので再設定をお願いします．

 | /home/w3varann/genomon_pipeline-2.4.0/genomon_conf/
 | ├ dna_exome_genomon.cfg
 | ├ dna_exome_genomon_GRCm38.cfg
 | ├ dna_target_genomon.cfg
 | ├ dna_wgs_genomon.cfg
 | ├ rna_genomon.cfg
 | ├ rna_genomon_GRCm38.cfg
 | └ paplot　　　　　　　　　　　　←新規追加
 | ├ paplot_dna.cfg
 | ├ paplot_dna_GRCm38.cfg
 | ├ paplot_rna.cfg
 | └ paplot_rna_GRCm38.cfg


Genomon2.3.0
^^^^^^^^^^^^

 | ・下位バージョン（v2.2.0）のパイプライン設定ファイルはご使用できません．以下のv2.3.0用のファイルをご使用ください．ANNOVARやinhouseの設定がFALSEになっているので再設定をお願いします．
 | /home/w3varann/genomon_pipeline-2.3.0/genomon_conf/
 | dna_exome_genomon.cfg
 | dna_target_genomon.cfg (TargetSeq用の設定ファイルが新たに追加されました)
 | dna_wgs_genomon.cfg
 | rna_genomon.cfg

 | ・SVの特定のサンプルで起こっていたエラーを修正しました．レアパターンです．エラーになっていなければ影響はありません．

 | ・変異コールのレポート(paplot)が出力されるようになりました．検出される候補の数に変更はありません．

Genomon2.2.0
^^^^^^^^^^^^

 | ・2つのパイプライン設定ファイル「genomon.cfg」[dna(rna)_task_param.cfg」が統合されて「dna(rna)_genomon.cfg」になりました．内容はv2.0.5のパイプライン設定ファイルとほとんど変わりません．

 | ・SV検出の感度がより良くなりました．TCGAデータを使用して確認したところ、候補の結果が1.2倍程度増えた癌種もあります．Genomon v2.2.0でSV検出を再実行することをお奨めします．(v2.0.5とBAMファイルに変更はないので、サンプル設定ファイルに[bam_import]でBAMファイルをインポートして、[sv_detection]を実行しましょう．

 | ・名称の変更summary→qc(quality control)になりました．結果ファイルのExcelファイルが出力されないようになりました．出力内容に変更はございません．

 | ・変異コール、SV検出の結果ディレクトリにxxxxx.result.filt.txtが新たに出力されます．こちらは適切な値でフィルタ済みのファイルになります．上級者である先生方には今まで通りのフィルタされていない結果ファイル(xxxx.result.txt(.filtがファイル名にない結果ファイル))をご使用いただければと思います．

 | ・解析結果のレポートが出力されるようになりました．出力ルートディレクトリに‘paplot’ディレクトリが追加されました．こちらをディレクトリごとwinSCPなどでローカルのマシンにダウンロードしていただき、index.htmlをダブルクリックしてください．SVやBam Quality Controlの結果がリッチテキストで確認できます．

 | ・サンプル毎に分かれて出力される変異コール、SV検出及びBamQCの結果ファイルをマージしたファイルが出力されるようになりました． 出力ルートディレクトリ内のpost_analysisディレクトリにマージされた結果ファイルが出力されます．

