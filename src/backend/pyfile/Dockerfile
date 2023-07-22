FROM python:3.11.4

WORKDIR /src

COPY . /src

COPY . /src/requirements.txt

# パッケージの更新
RUN apt-get update
# キャッシュクリーンアップと不要なリストの削除
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
# リナックスコマンドのパッケージインストール
RUN apt-get update && apt-get install -y vim less sudo tree

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8888

# docker-compose.yml作成したら不要:ビルド後にdocker runで対象ファイルを出力するコマンド
# CMD ["python", "main.py"]