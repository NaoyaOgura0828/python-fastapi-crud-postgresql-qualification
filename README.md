# python-fastapi-crud-postgresql-qualification
PythonのFastAPIでPostgreSQLへCRUDするAPIを実行する。

<br>

# Settings
## Nginx セットアップ
### nginx.conf 設定

1. [nginx.conf](./middle_conf/nginx.conf)を参考に、`/etc/nginx/nginx.conf`を設定する。

2. 下記コマンドを実行しNginxを再起動する。

    ```bash
    sudo service nginx restart
    ```

<br>

## DB セットアップ
### DB User 作成

1. デフォルトユーザーでログイン<br>
    bashで下記コマンドを実行する

    ```bash
    sudo -u postgres psql
    ```

2. ユーザーをSuperUserロールで作成

    ```sql
    CREATE USER satoasu WITH SUPERUSER;
    ```

3. ユーザーパスワード設定

    ```sql
    ALTER USER satoasu WITH PASSWORD 'your_password';
    ```

<br>

### データベース 作成

1. デフォルトユーザーでログイン

    ```bash
    sudo -u postgres psql
    ```

2. データベースを作成

    ```sql
    CREATE DATABASE app;
    ```

<br>

### テーブル 作成

1. 作成したユーザーでログイン

    ```bash
    psql -U satoasu -d app
    ```

2. テーブルを作成

    ```sql
    CREATE TABLE qualifications (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        description TEXT
    );
    ```

<br>

### pg_hba.conf 設定
[pg_hba.conf](./middle_conf/pg_hba.conf)を参考に、`/etc/postgresql/[postgresql_version]/main/pg_hba.conf`を設定する。

<br>

# Usage
## FastAPI 実行

[本リポジトリ直下](.)で下記コマンドを実行する。

```bash
uvicorn main:api --reload --port 8080
```

<br>

## 動作確認
### FastAPI docsでの動作確認

http://localhost:8080/docs へアクセスし、各メソッドの動作確認を行う。

<br>

### FastAPI実行環境内での動作確認

各テスト用リクエストは下記の通り。

```bash
# CREATE
curl -X 'POST' 'http://localhost:8080/api/qualification/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"name": "Python3エンジニア認定基礎試験", "description": "Python初学者向け認定資格"}'

# READ
## id指定取得
## ${id}を任意のid番号へ置換すること
curl -X 'GET' 'http://localhost:8080/api/qualification/${id}' \
    -H 'accept: application/json'

## 全件取得
curl -X 'GET' 'http://localhost:8080/api/qualification/' \
    -H 'accept: application/json'

# UPDATE
## ${id}を任意のid番号へ置換すること
curl -X 'PUT' 'http://localhost:8080/api/qualification/${id}' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"name": "Python3エンジニア認定データ分析試験", "description": "Python初学者向けデータ分析資格"}'

# DELETE
## ${id}を任意のid番号へ置換すること
curl -X 'DELETE' 'http://localhost:8080/api/qualification/${id}' \
    -H 'accept: application/json'

```

<br>

### ローカル環境での動作確認 (nginx経由)

各テスト用リクエストは下記の通り。

```bash
# CREATE
curl -X 'POST' 'http://localhost:50080/api/qualification/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"name": "Python3エンジニア認定基礎試験", "description": "Python初学者向け認定資格"}'

# READ
## id指定取得
## ${id}を任意のid番号へ置換すること
curl -X 'GET' 'http://localhost:50080/api/qualification/${id}' \
    -H 'accept: application/json'

## 全件取得
curl -X 'GET' 'http://localhost:50080/api/qualification/' \
    -H 'accept: application/json'

# UPDATE
## ${id}を任意のid番号へ置換すること
curl -X 'PUT' 'http://localhost:50080/api/qualification/${id}' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"name": "Python3エンジニア認定データ分析試験", "description": "Python初学者向けデータ分析資格"}'

# DELETE
## ${id}を任意のid番号へ置換すること
curl -X 'DELETE' 'http://localhost:50080/api/qualification/${id}' \
    -H 'accept: application/json'

```
