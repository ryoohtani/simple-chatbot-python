## Creating a chat application in Python (for learning)
## Pythonでチャットアプリの作成(学習用)

<sub> Developing a chat app with basic Python learning. </sub>

<sub> Pythonの基礎学習でチャットアプリを開発中 </sub>

**環境構築**

*dockerコマンド*

* ビルドコマンド
```
docker-compose build
```
* 環境の立ち上げ
```
docker-compose up -d
```
* コンテナにアクセス
```
docker exec -it コンテナの名前 /bin/bash
```

*Pythonのコマンド*

* set.py(Pythonのパッケージをビルド、インストール、配布する際の必要情報記載)
```
python setup.py sdist
```

*gitコマンド*

* ローカルリポジトリの新規作成
```
git init
```

* ファイルの追跡(変更分全て)
```
git add .
```

* コミット
```
git commit
```

* ローカルリポジトリにリモートリポジトリのURLを貼り付ける
```
git remote add origin URLを貼り付ける
```

* リモートリポジトリへプッシュ
```
git push -u origin main
```