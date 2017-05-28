# s2a_fm インストーラ版使用方法

## インストール

1. FirmataPlus のインストール: https://github.com/MrYsLab/PyMata/tree/master/ArduinoSketch より library.zip をダウンロードし，Arduino のライブラリフォルダへ展開 (例: c:\users\<username>\Documents\Arduino)
1. s2a_fm のインストール dist/s2a_fm-1.5-amd64.msi (インストール先の例: "C:\Program Files\s2a_fm\s2a_fm.exe")
1. COMポートの設定
  Arduino IDE もしくはデバイスマネージャーで Arduino の接続されている COMポート番号 を確認 (以下 COM7 とする)
    1. デスクトップの s2a_fm のショートカットにて，リンク先を `"C:\Program Files\s2a_fm\s2a_fm.exe" COM7` のようにする (Default: COM5)

## 使用方法

1. Arduino 側の設定
    1. IDEの「ファイル」 -> 「スケッチの例」 -> Firmata -> StandardFirmataPlus を読み込み，Arduino へ書き込む
1. Scratch2 側の設定
    1. Scratch2 offline editor を立ち上げる
    1. シフトキーを押しながら「ファイル」を押し「実験的なHTTP拡張を読み込み」を選ぶ
    1. "C:\Program Files\s2a_fm\s2a_fm.exe\work\s2a_fm_ja2.s2e" を選択（このファイルは別の分かりやすい場所にコピーしておいてもよい) (他の言語は ScratchFiles/ExtensionDescriptors)
1. デスクトップ上の s2a_fm を立ち上げて，最後に「Scratch detected! Ready to rock and roll...」が表示されれば起動完了

## トラブルシューティング

- ウィンドウがすぐに閉じる場合
    - COMポートを再確認
    - 他に s2a_fm が立ち上がっていないか確認
    - 問題が解決しない場合は，ショートカットのリンク先を `cmd /k "C:\Program Files\s2a_fm\s2a_fm.exe" COM7` に変更してコンソーに表示されメッセージを読む．
    -「Could not instantiate PyMata - is your Arduino plugged in?」が表示されるなら，再度COMポートを確認．
 
 
