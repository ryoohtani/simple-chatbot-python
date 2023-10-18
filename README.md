## Creating a chat application in Python (for learning)
## Pythonでチャットアプリの作成(学習用)

<sub> Developing a chat app with basic Python learning. </sub>

<sub> Pythonの基礎学習でチャットアプリを開発中 </sub>

**環境構築**

*dockerコマンド*

* ビルドコマンド
```
docker compose build
```
* 環境の立ち上げ
```
docker compose up -d
```
* コンテナにアクセス
```
docker exec -it python-chatbot bash
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

* リモートリポジトリからローカルに反映
```
git fetch
```

* ブランチの移動
```
git checkout main
```

* マージ
```
git merge origin2/main
```

**Pythonコードスタイルガイド**
* pep8
```
pep8 対象ファイル
```

* flake8
```
flake8 対象ファイル
```

* pylint
```
pylint 対象ファイル
```
---
*実際のアプリの画像*
* アプリ実行前のデータ(aggregation.csv)

<img width="361" alt="part0" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/1ab55e10-074c-493f-9880-7be1a2e7e936">

*アプリの起動*
* use_arrow_keys=Trueにより、キーボードの十字キーで操作可能

<img width="388" alt="スクリーンショット 2023-08-09 9 03 31" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/f081d7f1-bf26-4909-bd05-7fac3393c67a">

*最終設問*

<img width="413" alt="スクリーンショット 2023-08-09 9 04 04" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/66c17167-233a-4da6-b55c-ac3e113797d4">

*アプリ終了*
*終了画面

<img width="404" alt="スクリーンショット 2023-08-09 9 04 33" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/29f7f42b-5c6f-4f83-ad45-610b127a95b2">

*アプリ実行後のデータ(aggregation.csv)*
* model_section.pyによりデータの取集を行なったアウトプットの結果をcsvに記載

<img width="234" alt="part3" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/528ffd45-aecc-4677-8338-a6feb205dcf4">

