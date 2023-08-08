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
docker exec -it python-chatbot /bin/bash
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
git remote add origin2 URLを貼り付ける
```

* リモートリポジトリへプッシュ
```
git push -u origin2 main
```

実際のアプリの画像

<img width="361" alt="part0" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/1ab55e10-074c-493f-9880-7be1a2e7e936">
