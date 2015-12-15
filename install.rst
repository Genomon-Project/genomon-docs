--------------------------------
インストールします．Human Genome Center(HGC)スパコン向け．
--------------------------------

pythonの環境設定
-------
$qlogin
$python --version
バージョンが2.7であることを確認する．リビジョンは何でもいいです．

バージョンが2.7以外である場合は以下をExportしてから作業すること.
以下はバージョン2.7/currentの例です．currentとはHGCスパコンが用意している最新のリビジョンを示す
$export PYTHONHOME=/usr/local/package/python2.7/current
$export PATH=$PYTHONHOME/bin:$PATH
$export LD_LIBRARY_PATH=/usr/local/package/python2.7/current/lib:$LD_LIBRARY_PATH
$export PYTHONPATH=~/.local/lib/python2.7/site-packages
$export DRMAA_LIBRARY_PATH=/geadmin/N1GE/lib/lx-amd64/libdrmaa.so.1.0
これらを~/.bash_profileに記載しておいた方がいいです．

genomon2と必要なパッケージのインストール 
-------
必要なパッケージ： GenomonPipeline,ruffus,PyYAML,drmaa, xlwt,xlrd
$wget https://github.com/Genomon-Project/GenomonPipeline/archive/v2.0.2.tar.gz
$tar xzvf v2.0.2.tar.gz
$wget https://github.com/bunbun/ruffus/archive/v2.6.3.tar.gz
$tar xzvf v2.6.3.tar.gz
$git clone https://github.com/ravenac95/PyYAML
$pip install drmaa --user
$pip install xlwt --user
$pip install xlrd --user

ダウンロードしたツールのディレクトリにchange directoryしてinstallコマンドをたたく
$cd GenomonPipeline-2.0.2
$python setup.py install --user
$cd ../ruffus-2.6.3
$python setup.py install --user
$cd ../PyYAML
$python setup.py install --user
