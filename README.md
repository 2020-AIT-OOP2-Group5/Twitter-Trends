# Twitter API を用いたWeb アプリ

## 仕様
### 大まかな仕様（pythonによって情報を取得する側）
1.現在時刻の取得  
2.APIを使ってトレンドの情報取得。  
3.取得したトレンドのリツイートの多い方から5つをリストに格納。  
4.リストの情報からAPIを使ってトレンドに関するツイートの情報取得。  
5.リツイートが一番多いものを取得。  
6.3～4をリストの分だけ行う。  

### 大まかな仕様(Webアプリケーション側)
APIによって撮ってきた情報と現在時刻をflaskを用いてwebにあげる。

## 必読
- configfile 
    - Twitter_Key&Token.json  

        {
  "CK":"XXXXXXXXXXXXXXXXXXXXXX",
  "CS":"XXXXXXXXXXXXXXXXXXXXXX",
  "AT":"XXXXXXXXXXXXXXXXXXXXXX",
  "AS":"XXXXXXXXXXXXXXXXXXXXXX"
}
- 上記のTwitter_Key&Token.jsonをmain.pyと同じ階層に入れてください。
- 班員へ
    - configfileはTeamsにアップしてあります。

## 使用しているライブラリ一覧
|ライブラリ名|インストール手法|
|:---:|:---:|
|pytrends|pip install pytrends|
|tweepy|pip install tweepy|
|twitter|pip install twitter|
|flask|pip install Flask|


## 実行手順
Twitter-Trendsをカレントディレクトリにし、main.pyを実行する。  
その際に表示されるurlを踏むとwebアプリケーションが実行されます。