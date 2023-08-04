FROM python:3.11.4

WORKDIR /src

COPY . /src

# パッケージの更新
RUN apt-get update
# キャッシュクリーンアップと不要なリストの削除
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
# リナックスコマンドのパッケージインストール
RUN apt-get update && apt-get install -y vim less sudo tree

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install questionary

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8080