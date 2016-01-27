--------------------------------
Genomonインストール
--------------------------------
・Human Genome Center(HGC)スパコン向けです
・Pythonの設定と、Genomonと必要なパッケージをインストールします．


pythonの環境設定
----------------
バージョンが2.7以外である場合は以下をExportしてください.

.. code-block:: bash

  $export PYTHONHOME=/usr/local/package/python2.7/current
  $export PATH=$PYTHONHOME/bin:$PATH
  $export LD_LIBRARY_PATH=/usr/local/package/python2.7/current/lib:$LD_LIBRARY_PATH
  $export PYTHONPATH=~/.local/lib/python2.7/site-packages
  $export DRMAA_LIBRARY_PATH=/geadmin/N1GE/lib/lx-amd64/libdrmaa.so.1.0

これらを~/.bash_profileに記載しておいた方がいいです．

Genomonと必要なパッケージのインストール
---------------------------------------
必要なパッケージはこちら→GenomonPipeline,ruffus,PyYAML,drmaa, xlwt,xlrd

.. code-block:: bash

  # genomon-pipeline(本体)のダウンロード
  $wget https://github.com/Genomon-Project/GenomonPipeline/archive/v2.0.2.tar.gz
  $tar xzvf v2.0.2.tar.gz
  # ruffusのダウンロード
  $wget https://github.com/bunbun/ruffus/archive/v2.6.3.tar.gz
  $tar xzvf v2.6.3.tar.gz
  # PyYAMLのダウンロード
  $git clone https://github.com/ravenac95/PyYAML
  # drmaa,xlwt,xlrdのインストール
  $pip install drmaa --user
  $pip install xlwt --user
  $pip install xlrd --user
  # genomon-pipeline(本体)のインストール
  $cd GenomonPipeline-2.0.2
  $python setup.py install --user
  # ruffusのインストール
  $cd ../ruffus-2.6.3
  $python setup.py install --user
  # PyYAMLのインストール
  $cd ../PyYAML
  $python setup.py install --user

