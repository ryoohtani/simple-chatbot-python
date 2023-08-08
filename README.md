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

*実際のアプリの画像*
* アプリ実行前のデータ(aggregation.csv)
<img width="361" alt="part0" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/1ab55e10-074c-493f-9880-7be1a2e7e936">

*アプリの起動*
* use_arrow_keys=Trueにより、キーボードの十字キーで操作可能
<img width="394" alt="part1" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/739ed7b0-9cb4-45fd-a3df-7959107733b2">

*最終設問*
<img width="402" alt="part2" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/c514a2b2-98c1-4aba-b66a-9fcbde30b7bf">

*アプリ実行後のデータ(aggregation.csv)*
* model_section.pyによりデータの取集を行なったアウトプットの結果をcsvに記載
<img width="234" alt="part3" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/528ffd45-aecc-4677-8338-a6feb205dcf4">

