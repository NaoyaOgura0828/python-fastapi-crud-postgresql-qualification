from pydantic import BaseModel


class QualificationBase(BaseModel):
    """
    資格データの共通基底クラス。

    このクラスは資格データの基本フィールドを定義しており、他の資格モデルで再利用される。

    Attributes:
        name (str): 資格の名前。
        description (str): 資格の説明。
    """
    name: str
    description: str


class QualificationCreate(QualificationBase):
    """
    資格データを作成するためのモデル。

    このクラスは資格データの作成に使用される。
    """
    pass


class QualificationRead(QualificationBase):
    """
    読み取り時に使用する資格モデル。

    このクラスはデータベースから資格データを取得する際に使用される。

    読み取り専用のフィールドを含む。

    Attributes:
        id (int): 資格の一意な識別子。

    Config:
        from_attributes: True - モデルの属性から追加の設定を読み込むための設定。
    """
    id: int

    class Config:
        from_attributes = True


class QualificationUpdate(QualificationBase):
    """
    資格情報を更新するためのモデル。

    このクラスは資格データの更新に使用される。

    更新する際には、対象の資格を一意に識別するためのidが必要である。

    Attributes:
        id (int): 更新する資格の一意な識別子。
        name (str): 資格の名前。
        description (str): 資格の説明。
    """
    pass
