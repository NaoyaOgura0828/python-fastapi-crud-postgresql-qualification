from fastapi import FastAPI

from endpoints import qualification_endpoint


# FastAPI アプリケーションのインスタンスを作成
api = FastAPI()

# エンドポイントをAPIルータに含める
api.include_router(qualification_endpoint.endpoint)
