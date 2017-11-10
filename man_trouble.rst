3. トラブルシューティング
=============================

解析ジョブがすべて完了しているのにも関わらず解析結果が出力されていない場合，異常終了した可能性があります．下記の手順をもとに原因の切り分けと対策を行います．

.. _error_job:

3-1. 異常終了したジョブの特定
-----------------------------------

``qreport`` コマンドを用いて異常終了したジョブをリストアップします．
（ジョブの実行結果の確認方法はお使いのUGEシステムによって異なることがあります．下記コマンドで確認できない場合はジョブの実行結果の確認方法をシステム管理者にご確認ください）

例えば，2017/8/10 13:00以降に実行したジョブのうち異常終了したものをリストアップする場合は，以下のように実行します．

.. code-block:: bash

  $ qreport -f -b 201708101300 -o lect-1 -l

:f: 異常終了したジョブのみ表示
:b: 指定した日時以降のジョブのみ表示
:o: 指定したユーザIDのジョブのみ表示
:l: 一覧表示モードで表示

.. code-block:: bash
  :caption: qreport コマンドの出力例
  
  # -f オプションを指定しているため失敗したジョブのみ表示されています
  $ qreport -f -b 201708101300 -o lect-1 -l
  | owner  | jobid    |~|ext|fail|~| jobname                            |~| mmem  | rmem  |~| Ropt                       |
  | lect-1 | 35171900 |~|152| 100|~| qsub_genomon_pipeline.sh           |~| 33.1G | 32.0G |~| -l s_vmem=32G,mem_req=32G  |
  | lect-1 | 35171943 |~|137| 100|~| qsub_genomon_pipeline.sh           |~| 32.9G | 32.0G |~| -l s_vmem=32G,mem_req=32G  |
  | lect-1 | 35172311 |~|137| 100|~| star_align_20170810_204030_806134  |~| 6.1G  | 5.3G  |~| -l s_vmem=8.0G,mem_req=8.0G|
  | lect-1 | 35172356 |~|137| 100|~| pmsignature_20170810_204030_806134 |~| 2.1G  | 2.0G  |~| -l s_vmem=5G,mem_req=5G    |
  ・・・・・・・
  ・・・・・・・
  (END)


:owner:   ユーザ名
:jobid:   ジョブID
:jobname: ジョブ名
:mmem:    実際に使用したメモリの最大値
:rmem:    スパコンに要求したメモリ量
:Ropt:    ジョブ再投入時に推奨されるqsubオプション

jobnameの列より，ジョブ名が ``qsub_genomon_pipeline.sh`` であるものがGenomon本体，それ以外はGenomon本体から呼び出された解析ジョブですが，Genomon以外にジョブを実行していた場合はその限りではありません．

なお，Genomonには，ジョブが異常終了した場合に自動的に再実行する機能が備わっています．このため ``qreport`` コマンドによってリストアップされたジョブであっても，再実行により解析が成功している場合もあります．

.. _main_mem:

3-2. Genomon本体の使用メモリを確認
--------------------------------------

まずGenomon本体のジョブが異常終了した原因を確認します．

``qreport`` コマンドを使用して使用したメモリを確認します．
該当しない場合は，次章 :ref:`3-3. Genomon本体のログファイルを確認 <main_log>` に進んでください．

.. code-block:: bash

  $ qreport -f -b 201708101300 -o lect-1 -l
  | owner  | jobid    |~|ext|fail|~| jobname                  |~| mmem  | rmem  |~| Ropt                      |
  | lect-1 | 35171943 |~|  1|   0|~| qsub_genomon_pipeline.sh |~| 32.9G | 32.0G |~| -l s_vmem=48G,mem_req=48G |
  ・・・・・・・
  ・・・・・・・
  (END)


【確認方法】

| 以下いずれかに当てはまる場合，メモリ超過エラーと考えられます．

 - ケース１：mmem (実際に使用したメモリの最大値) がrmem (スパコンに要求したメモリ量) を超過している．
 - ケース２：extが139もしくは152で終了している．
 
【対処法】

| Genomon解析コマンドの ``qsubオプション`` に，Ropt 列で示された qsub オプション値を指定し，Genomon を再実行します．

.. code-block:: bash

  $ bash
  /home/lect-1/script/genomon_pipeline.sh \
  rna \
  /home/lect-1/config/test5929.csv \
  /home/lect-1/test5929 \
  /home/lect-1/config/rna_genomon.cfg \
  '-l s_vmem=48G,mem_req=48G'

.. _main_log:

3-3. Genomon本体のログファイルを確認
----------------------------------------

``qreport`` コマンドの出力よりジョブIDを確認し，エラーが発生したジョブのログファイルを特定します．

.. code-block:: bash

  $ qreport -f -b 201708101300 -o lect-1 -l
  | owner  | jobid    |~| jobname                  |~| mmem  | rmem  |~| Ropt                      |
  | lect-1 | 35171943 |~| qsub_genomon_pipeline.sh |~| 32.9G | 32.0G |~| -l s_vmem=48G,mem_req=48G |
  ・・・・・・・
  ・・・・・・・
  (END)


上記の例では，ジョブIDは ``35171943`` であることがわかります．
Genomon本体のログファイルは解析の出力ディレクトリ内の ``log`` ディレクトリ配下に出力されます．

.. code-block:: bash
  :caption: Genomon本体のログファイルの場所
  
  $ ls /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e<ジョブID>


ログファイルを特定したら，その内容が以下のケースに該当するか確認ください．
解決しない場合は，次章 :ref:`3-4. 解析ジョブの使用メモリを確認 <job_mem>` に進んでください．

Genomon本体のログ出力例
****************************************

◆ケース1: RuntimeError: Job: xxxxx
+++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e1234567
  ・・・・・・・
  ・・・・・・・
  Traceback (most recent call last):
    File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/ruffus/task.py, line 751, in run_pooled_job_without_exceptions
      register_cleanup, touch_files_only)
    File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/ruffus/task.py, line 567, in job_wrapper_io_files
      ret_val = user_defined_work_func(*params)
    File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packageslib/python/genomon_pipeline/dna_pipeline.py, line 517, in identify_mutations
      mutation_call.task_exec(arguments, run_conf.project_root + '/log/' + sample_name, run_conf.project_root + '/script/' + sample_name, max_task_id)
    File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/genomon_pipeline/stage_task.py, line 105, in task_exec
      raise RuntimeError("Job: " + str(retval.jobId)  + ' failed at Date/Time: ' + date)
  'RuntimeError: Job: 35281321 failed at Date/Time: 2017-10-03 11:42:27'
  (END)
  
【原因】

| Genomonが呼び出した解析ジョブが何らかの原因で異常終了したことが原因です．
| 上記の場合，異常終了した解析ジョブのIDは ``35281321`` であることがわかります．

【対処法】

| 詳しい原因を調査するため，次章 :ref:`3-4. 解析ジョブの使用メモリを確認 <job_mem>` に進んでください．


◆ケース2: DRMAA sessionエラー
++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e1234567
  ・・・・・・・
  ・・・・・・・
  'AlreadyActiveSessionException: code 11: Initialization failed due to existing DRMAA session.'
  (END)

【原因】

| Genomon本体が使用するメモリ量がグリッドエンジン側で不足し，グリッドエンジンのセッションエラーが発生することで解析が異常終了したためと考えられます．

【対処法】

| 本エラーを以ってGenomon本体が異常終了することによりメモリは開放されているため，Genomon解析コマンドを再度実行してください．
| 繰り返し本ケースが生じるようであればGenomon解析コマンドの ``qsubオプション`` にてより多くのメモリをスパコンに要求し，再度実行してください．
| なお， ``qsubオプション`` を指定しない場合，Genomon解析コマンドは ``64GB`` のメモリをスパコンに要求します．

再実行例：

.. code-block:: bash

  $ bash
  /home/lect-1/script/genomon_pipeline.sh \
  rna \
  /home/lect-1/config/test5929.csv \
  /home/lect-1/test5929 \
  /home/lect-1/config/rna_genomon.cfg \
  '-l s_vmem=96G,mem_req=96G'


◆ケース3: DrmCommunicationExceptionエラー
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e1234567
  ・・・・・・・
  ・・・・・・・
  File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/genomon_pipeline/stage_task.py, line 56, in task_exec
  jobid = s.runJob (jt)
  File build/bdist.linux-x86_64/egg/drmaa/session.py, line 314, in runJob
  c (drmaa_run_job, jid, sizeof (jid) , jobTemplate)
  File build/bdist.linux-x86_64/egg/drmaa/helpers.py, line 299, in c
  return f (\* (args + (error_buffer, sizeof (error_buffer) ) ) )
  File build/bdist.linux-x86_64/egg/drmaa/errors.py, line 151, in error_check
  raise _ERRORS[code - 1] (error_string)
  'DrmCommunicationException: code 2: failed receiving gdi request response for mid=4 (got syncron message receive timeout error) .'
  (END)

【原因】

| 解析実行時，スパコン側においてグリッドエンジンのマスタホストの負荷が高かったことにより，グリッドエンジンのコミュニケーションエラーが発生し解析が異常終了した可能性が考えられます．

【対処法】

| Genomon解析コマンドを再実行してください．


◆ケース4: DatabaseError
++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e1234567
  ・・・・・・・
  ・・・・・・・
  File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/ruffus/file_name_parameters.py, line 548, in needs_update_check_modify_time
  if os.path.relpath (p) not in job_history and p not in set_incomplete_files:
  File /home/w3varann/python/2.7.10/lib/python2.7/_abcoll.py, line 388, in __contains__
  self[key]
  File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/ruffus/dbdict.py, line 174, in __getitem__
  (key, ) ) .fetchone ()
  'DatabaseError: database disk image is malformed'
  (END)


【原因】

| Genomonがパイプラインの進捗管理に使用しているデータベースファイル (.ruffus_history.splite) に対する読み取りまたは書き込みに失敗し，解析が異常終了したためと考えられます．

【対処法】

| ①データベースファイル (.ruffus_history.) を削除してください．データベースファイルはGenomonコマンドを実行したディレクトリに作成されています．
| ②Genomon解析コマンドを再実行してください．


◆ケース5: 強制終了
++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e1234567
  ・・・・・・・
  ・・・・・・・
  genomon_pipeline: line 47: 21714 '強制終了'
  (END)

【原因】

入力サンプル数が多いとき，スパコン側で計算リソースが不足し強制終了することがあります．

【対処法】

| ①入力サンプル数が多い場合は (目安: 数1000以上) ，サンプル設定ファイル中の解析対象サンプルが500程度になるようにサンプル設定ファイルを分割して複数作成してください．
| ②Genomon解析コマンドに，①で作成したサンプル設定ファイルを指定して，サンプル設定ファイル数ぶんGenomon解析コマンドを再実行してください．

◆ケース6: （サンプル名）.markdup.bam does not exists
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e1234567
  ・・・・・・・
  ・・・・・・・
  Genomon is checking parameters ...
  Traceback (most recent call last):
  File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/bin/genomon_pipeline, line 29, in <module>
  main(args)
  File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/genomon_pipeline/run.py, line 21, in main
  sample_conf.parse_file(run_conf.sample_conf_file)
  File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/genomon_pipeline/config/sample_conf.py, line 61, in parse_file
  self.parse_data(file_data_trimmed)
  File {path to genomon installed}/genomon_pipeline-2.5.3/python2.7-packages/lib/python/genomon_pipeline/config/sample_conf.py, line 237, in parse_data
  raise ValueError(err_msg)
  ValueError: test_1:
  '/home/lect-1/raw/bam/test_1/test_1.markdup.bam does not exists'
  (END)


【原因】

当該解析対象ファイルがサンプル設定ファイルに記載したディレクトリ下に配置されていないため，解析対象ファイルが読み込めていない状態と考えられます．

【対処法】

| ①サンプル設定ファイルに記載したディレクトリに記載した通り当該解析対象ファイルが配置されていることや，サンプル設定ファイルの記載内容を確認してください．
| ②Genomon解析コマンドを再実行してください．


◆ケース7: Disk quota exceeded
+++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/qsub_genomon_pipeline_HGC.sh.e1234567
  ・・・・・・・
  ・・・・・・・
  Original exceptions:
  
  Exception #1
      'exceptions.IOError([Errno 122] Disk quota exceeded)' raised in ...
       Task = def genomon_pipeline.dna_pipeline.post_analysis_mutation(...):
  ・・・・・・・
  ・・・・・・・

【原因】

出力するファイルサイズが大きすぎると発生します．主に変異の数が多いWGSのmutation結果マージの工程で発生します．

【対処法】

| ①主にGenomonPostAnalysisの工程で，変異結果をマージする際に発生しますので，マージファイルが不要であれば設定をOFFにします．
|   詳しい手順は `レポート作成機能について <./qa.html#merge_skip>`__ を参照ください．

.. _job_mem:

3-4. 解析ジョブの使用メモリを確認
------------------------------------------

Genomon本体ではなく，解析ジョブに問題が発生した場合は各解析ジョブを確認することで原因が特定できることがあります．

まず，``qreport`` コマンドを使用してジョブの結果を確認します．
該当しない場合は，次章 :ref:`3-5. 解析ジョブのログファイルを確認 <job_log>` に進んでください．

異常終了したジョブが特定できている場合は以下のようにして確認します．

.. code-block:: bash

  $ qreport -j 34753787 -l
  | owner  | jobid    |~|ext|fail|~| jobname                             |~| mmem|  rmem|~|Ropt                    |
  | lect-1 | 34753787 |~|137|100 |~| fusionfusion_20170825_160352_970695 |~| 3.2G|  6.0G|~|-l s_vmem=6G,mem_req=6G |
  

ジョブが特定できていない場合は以下のようにして探します．

.. code-block:: bash
  
  $ qreport -f -b 201708101300 -o lect-1 -l
  | owner  | jobid    |~|ext|fail|~| jobname                           |~| mmem | rmem |~| Ropt                        |
  | lect-1 | 35172311 |~|137|100 |~| star_align_20170810_204030_806134 |~| 6.1G | 5.3G |~| -l s_vmem=8.0G,mem_req=8.0G |


【確認方法】

以下いずれかに当てはまる場合，メモリ超過エラーと考えられます．

 - ケース１：mmem (実際に使用したメモリの最大値) がrmem (スパコンに要求したメモリ量) を超過している．
 - ケース２：extが139もしくは152で終了している．

【対処法】

| ①パイプライン設定ファイルを編集し，該当するジョブに対するqsubオプションに，(Ropt) 列で示されたqsubオプション値を指定し，Genomonを再実行します．

◆STARによるアライメントジョブのqsubオプション値の変更例

.. code-block:: bash

  $ pwd
  /home/lect-1/config/
  $ vi rna_genomon.cfg
  ##########
  # parameters for star alignment
  [star_align]
  
  # 変更前
  qsub_option = -l s_vmem=5.3G,mem_req=5.3G -pe def_slot 6
  # 変更後
  qsub_option = -l s_vmem=8.0G,mem_req=8.0G -pe def_slot 6


◆pmsignatureジョブのqsubオプション値の変更例

.. code-block:: bash

  $ pwd
  /home/lect-1/config/
  $ vi dna_exome_genomon.cfg
  ############
  
  # pmsignature full の場合
  [pmsignature_full]
  
  # 変更前
  qsub_option = -l s_vmem=2G,mem_req=2G
  # 変更後
  qsub_option = -l s_vmem=5.3G,mem_req=5.3G
  
  # pmsignature ind の場合
  [pmsignature_ind]
  
  # 変更前
  qsub_option = -l s_vmem=2G,mem_req=2G
  # 変更後
  qsub_option = -l s_vmem=5.3G,mem_req=5.3G


②Genomon解析コマンドを再度実行してください．

.. _job_log:

3-5. 解析ジョブのログファイルを確認
---------------------------------------

今回は異常終了した解析ジョブのIDが ``35172322`` であると仮定します．

各ジョブのログファイルは，解析の出力ディレクトリ内の ``log`` ディレクトリ配下に出力されますので，下記のコマンドを用いて，そのジョブIDに該当するジョブのログファイルを特定します．

.. code-block:: bash
  :caption: ログファイルの特定方法
  
  $ ls -l /home/lect-1/test5929/log/*/*.e<ジョブID>

.. code-block:: bash
  :caption: ログファイルの特定例
  
  $ ls -l /home/lect-1/test5929/log/*/*.e35172322
  /home/lect-1/test5929/log/pmsignature/pmsignatutre_YYYYMMDD_123456_123456.e35172322.1
  $


ログファイルを特定したら，その内容が以下のケースに該当するか確認ください．

pmsignature
*******************

◆ケース1: Error: cannot allocate vector
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/pmsignature/pmsignatutre_YYYYMMDD_123456_123456.e12345678.1
  ・・・・・・・
  ・・・・・・・
  'Error: cannot allocate vector' of size 111.9 Mb
  In addition: Warning messages:
  1: In readMPFile(inputFile, numBases = 5, trDir = trDirFlag, bs_genome = eval(parse(text = bs_genome)), :
  The central bases are inconsistent in 214424 mutations. We have removed them.
  2: In readMPFile(inputFile, numBases = 5, trDir = trDirFlag, bs_genome = eval(parse(text = bs_genome)), :
  The characters other than (A, C, G, T) are included in alternate bases of 184931 mutations. We have removed them.
  Execution halted
  ・・・・・・・
  ・・・・・・・
  (END)


【原因】

| mmem (実際に使用したメモリの最大値) がrmem (スパコンに要求したメモリ量) を超過したことによるメモリ不足のためと考えられます．

【対処法】

| pmsignatureで利用するメモリ量を増やしてジョブを再実行してください．:ref:`3-4. 解析ジョブの使用メモリを確認 <job_mem>` を参照ください．

STAR
***********

◆ケース1: 期待してない token \` (' のあたりにシンタックスエラー
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/test_1/star_align_YYYYMMDD_123456_123456.e1234567
  ・・・・・・・
  ・・・・・・・
  /home/lect-1/config/test5929/script/test_(1) /star_align
  '_20170824_152847_296876.sh: line 13: 期待してない token \` (' のあたりにシンタックスエラー'
  /home/lect-1/test5929/script/test_(1) /star_align_20170824_152847_296876.sh: line 13: \`{path to genomon installed}/genomon_pipeline-2.5.3/tools/STAR-2.5.2a/bin/Linux_x86_64_static/STAR --genomeDir {path to genomon installed}/genomon_pipeline-2.5.3/database/GRCh37.STAR-2.5.2a --readFilesIn /home/lect-1/raw/fastq/test_(1) /1_1.fastq /home/lect-1/raw/fastq/test_(1) /1_2.fastq --outFileNamePrefix /home/lect-1/test5929/star/test_(1) /test_(1) ) . --runThreadN 6 --outSAMstrandField intronMotif --outSAMunmapped Within --alignMatesGapMax 500000 --alignIntronMax 500000 --alignSJstitchMismatchNmax -1 -1 -1 -1 --outSJfilterDistToOtherSJmin 0 0 0 0 --outSJfilterOverhangMin 12 12 12 12 --outSJfilterCountUniqueMin 1 1 1 1 --outSJfilterCountTotalMin 1 1 1 1 --chimSegmentMin 12 --chimJunctionOverhangMin 12 --outSAMtype BAM Unsorted '
  ・・・・・・・
  ・・・・・・・
  (END)


【原因】

| 上記エラーにおいてはサンプル名が ``test_(1)`` であり，括弧” (“がサンプル名内に含まれてることが原因でした．
| サンプル設定ファイル内に記述されているディレクトリ名・ファイル名・サンプル名に特殊文字が含まれているとSTARで読み込めないことがあります．

【対処法】

| ①サンプル設定ファイル内の特殊文字を削除してください．Genomonでは，半角英数字・ハイフン( `-` )・ピリオド( '.' ) のみを推奨しています．
| ②Genomon解析コマンドを再実行してください．


◆ケース2: ReadAlignChunk_processChunks.cpp:115:processChunks EXITING because of FATAL ERROR in input reads: unknown file format: ....
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/test_1/star_align_YYYYMMDD_123456_123456.e1234567
  ・・・・・・・
  ・・・・・・・
  'ReadAlignChunk_processChunks.cpp:115:processChunks EXITING because of FATAL ERROR in input reads: unknown file format: the read ID should start with @ or >'
  Aug 23 18:12:04 …… FATAL ERROR, exiting
  ・・・・・・・
  ・・・・・・・
  (END)

【原因】

| (1) 入力されたFastqファイルの記述内容が不正のためと考えられます．
| (2)  ``gzip`` 等で圧縮されたFastqファイルを入力しているためと考えられます．アライメントに使用しているツール ``STAR`` では，gzip等で圧縮された形式でのFastqファイルの入力をサポートしておらず，Fastqフォーマットエラーと出力されます．

【対処法】

| ①原因ごとに以下を実行してください．
| (1) Fastqファイルの中身を確認してください．
| (2) 解凍して入力してください．合わせて，サンプル設定ファイルにおけるFastqファイルパスの記述も，解凍後のものへと変更してください．
| 
| ②Genomon解析コマンドを再実行してください．

◆ケース3: FATAL ERROR: Read1 and Read2 are not consistent
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/test_1/star_align_YYYYMMDD_123456_123456.e1234567
  ・・・・・・・
  ・・・・・・・
  EXITING because of 'FATAL ERROR: Read1 and Read2 are not consistent, reached the end of the one before the other one'
  SOLUTION: Check you your input files: they may be corrupted
  Aug 24 17:39:14 ...... FATAL ERROR, exiting
  ・・・・・・・
  ・・・・・・・
  (END)


【原因】

| ペアとなるRead1とRead2のリード数が一致していないためと考えられます．

【対処法】

| ①Genomonではリード数が不一致の場合使用できませんので，当該サンプルをサンプル設定ファイル上から削除してください．
| ②Genomon解析コマンドを再実行してください．


SV
*******************

◆ケース1: Error: sequence depth exceeds the threshould
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  $ tail /home/lect-1/test5929/log/test_1/sv_filt_YYYYMMDD_123456_123456.e12345678
  ・・・・・・・
  ・・・・・・・
  sequence depth exceeds the threshould for: 16,46474950,-,6,26731656,+
  ・・・・・・・


【原因】

| ログに記載されているブレークポイント (Chr16: 46474950, Chr6: 26731656) のどちらかでdepthが深すぎることがと考えられます．

【対処法】

| ①シーケンスデータファイルを見直してください．使用しないデータがあれば除いてください（MTなど）
| ②depthの上限を変更する場合はパイプライン設定ファイルを以下のように変更し，ジョブを再実行してください．

.. code-block:: bash

  $ pwd
  /home/lect-1/config/
  $ vi dna_exome_genomon.cfg
  ############
  
  [sv_filt]
  # 最後に--max_depthをつけ足してください．デフォルトのdepth上限は5000です
  params = --min_junc_num 2 --max_control_variant_read_pair 10 --min_overhang_size 30 --max_depth MAX_DEPTH


