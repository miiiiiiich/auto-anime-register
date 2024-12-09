![](https://github.com/miiiiiiich/auto-anime-register/actions/workflows/python-lint.yml/badge.svg)
[![Code style: ruff](https://camo.githubusercontent.com/051a04ae958f4a1a5d6444df4cdc520305eef93d5028e6d4c7cd16efa3136cd4/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f61737472616c2d73682f727566662f6d61696e2f6173736574732f62616467652f76322e6a736f6e)](https://github.com/psf/black)

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![github_action](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white)
![intellij](https://img.shields.io/badge/IntelliJ_IDEA-000000.svg?style=for-the-badge&logo=intellij-idea&logoColor=white)

## auto-anime-register

notionAPIとmy-anime-listAPIを使ってnotionデータベースに自動でアニメの詳細情報およびレビューを追加する。

個人用に作成しているのでnotion側の列名なども固定になっている。

## application

### before

<img width="400" alt="" src="https://user-images.githubusercontent.com/51878466/215313235-6ac5306f-e7a5-4b94-8b11-878460f9c94c.png">

### after

<img width="400" alt="" src="https://user-images.githubusercontent.com/51878466/215313261-bae5e120-9648-4123-9955-dcd9fdf85dec.png">

## env

- python 3.12^
- poetry

### install

```shell
poetry install 
```

### env file

```shell
# .env file
NOTION_API_TOKEN = "xxx"
NOTION_DATABASE_ID = "xxx"
```

### run

#### 1. my-anime-listのデータがないアイテムについての付与

```shell
poetry run poe give
```

引数にstatusを指定することで、指定したstatusのアニメのみ更新する。

https://user-images.githubusercontent.com/51878466/215313869-ee96e9cb-e104-4e68-91e1-29a4a1117b1d.mov

#### 2. my-anime-listのデータがあるアイテムについての更新

```shell
poetry run poe update
```

my anime list のapi制限によりすべてできるとは限らない。
api 制限になった場合はしばらくの間実行できなくなるので注意が必要

## reference

- [notionAPI](https://developers.notion.com/docs/getting-started)
- [notion_client](https://blog.rmc-8.com/2021/06/using-notion-api-with-python.html)
- [how to use my anime list API](https://myanimelist.net/forum/?topicid=1973141)
- [Awesome Badges](https://dev.to/envoy_/150-badges-for-github-pnk)

## development

### stub

```shell
pyright --createstub <library-name>
```