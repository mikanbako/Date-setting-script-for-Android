Androidデバイスの時刻を設定するスクリプト

注意：
本スクリプトは、rootパーミッションでshellを実行できる
Androidデバイスでないと動作しません。

1. 使い方

  1. AndroidデバイスをPCと接続します。

  2. コンソールを開きます。
    
  3. 現在時刻を設定する場合は、コンソール上で以下を実行します。
    （ここでの例は、すべてbash上での実行です）

    ./set_android_date.py now

     特定の時刻を設定する場合は以下を実行します。
     （この例では、PC上での時刻2011/05/19 23:57を設定しています）

    ./set_android_date.py 20110519.2357

  詳細は、以下を実行してください。
  
    ./set_android_date.py -h

2. 動作条件

  以下のソフトウェアのインストールが必要です。

  * Python 2.7 (http://www.python.org/)
  * Android SDK (http://developer.android.com/sdk/)

  PATH環境変数に、Android SDK内のadbを含むディレクトリへのパスを含めてください。

3. 制限

  1. 本スクリプトでは、Android上のタイムゾーンは設定できません。

  2. Androidエミュレータでは、時刻を設定できても「settimeofday failed Invalid
     argument」とコンソール上に出力されます。そのような出力がなされても、
     動作に問題はありません。

