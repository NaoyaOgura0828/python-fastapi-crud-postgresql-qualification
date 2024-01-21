from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.schema import Identity

from db_connection import Base


class QualificationModel(Base):
    """
    資格に関する情報を格納するためのデータベースモデル。

    このクラスは SQLAlchemy の Base クラスを継承し、資格データを格納するためのテーブル構造を定義する。

    各資格は一意のID、名前、および詳細説明を持つ。

    Attributes:
        id (Column): 資格の一意な識別子。自動でインクリメントされる整数。
        name (Column): 資格の名前。最大255文字の文字列。
        description (Column): 資格の詳細説明。長さ制限のないテキスト。
    """
    __tablename__ = 'qualifications'

    id = Column(Integer, Identity(), primary_key=True)
    name = Column(String(255))
    description = Column(Text)
