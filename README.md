## auto-anime-register

notionAPIとmy-anime-listAPIを使ってnotionデータベースに自動でアニメの詳細情報およびレビューを追加する。

個人用に作成しているのでnotion側の列名なども固定になっている。

## application

### before

<img width="400" alt="" src="https://user-images.githubusercontent.com/51878466/215313235-6ac5306f-e7a5-4b94-8b11-878460f9c94c.png">

### after

<img width="400" alt="" src="https://user-images.githubusercontent.com/51878466/215313261-bae5e120-9648-4123-9955-dcd9fdf85dec.png">

## env

- python 3.10^
- pipenv

### install

```shell
pipenv install 
```

### env file

```shell
# .env file
NOTION_API_TOKEN = "xxx"
NOTION_DATABASE_ID = "xxx"
MAL_CLIENT_ID = "xxx"
```

### run

#### 1. my-anime-listのデータがないアイテムについての付与

```shell
pipenv run give
# pipenv run update-notion in_progress todo
```

引数にstatusを指定することで、指定したstatusのアニメのみ更新する。

https://user-images.githubusercontent.com/51878466/215313869-ee96e9cb-e104-4e68-91e1-29a4a1117b1d.mov

#### 2. my-anime-listのデータがあるアイテムについての更新

```shell
pipenv run update
# pipenv run update-notion in_progress todo
```
my anime list のapi制限によりすべてできるとは限らない。
api 制限になった場合はしばらくの間実行できなくなるので注意が必要

## reference

- [notionAPI](https://developers.notion.com/docs/getting-started)
- [notion_client](https://blog.rmc-8.com/2021/06/using-notion-api-with-python.html)
- [how to use my anime list API](https://myanimelist.net/forum/?topicid=1973141)

## development

### stub
```shell
pyright --createstub <library-name>
```