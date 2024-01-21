from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


# DBエンドポイント設定
DB_ENDPOINT = "postgresql+asyncpg://satoasu:satoasu@localhost:5432/app"

# 非同期エンジンの作成
async_engine = create_async_engine(DB_ENDPOINT, echo=True)

# 非同期セッションファクトリーの作成
async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# SQLAlchemyのdeclarative base クラスのインスタンスを作成
Base = declarative_base()


async def create_db_session():
    """
    非同期データベースセッションを作成し、コンテキストマネージャとして使用するためのジェネレーター関数。

    この関数は、非同期セッションを使用してデータベースとの接続を確立し、そのセッションを呼び出し元に提供する。

    セッションは自動的に管理され、関数のコンテキストが終了するとセッションが閉じられる。

    Yields:
        AsyncSession: SQLAlchemyの非同期セッションオブジェクト。
    """
    async with async_session() as session:
        yield session
