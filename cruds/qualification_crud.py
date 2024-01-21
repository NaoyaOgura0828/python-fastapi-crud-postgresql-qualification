from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session


from models.qualification_model import QualificationModel
from schemas.qualification_schema import QualificationCreate, QualificationUpdate


async def create_qualification(qualification_data: QualificationCreate, db_session: Session) -> QualificationModel:
    """
    新しい資格情報をデータベースに作成する。

    Args:
        qualification_data (QualificationCreate): 作成する資格のデータ。
        db_session (Session): SQLAlchemyのセッションインスタンス。

    Returns:
        QualificationModel: 作成された資格のモデルインスタンス。

    Raises:
        Exception: データベース操作中に例外が発生した場合。
    """
    try:
        new_qualification_data = QualificationModel(
            name=qualification_data.name,
            description=qualification_data.description
        )
        db_session.add(new_qualification_data)
        await db_session.commit()
        await db_session.refresh(new_qualification_data)
        return new_qualification_data

    except Exception as exception:
        raise exception


async def get_qualification(qualification_id: int, db_session: Session) -> QualificationModel:
    """
    特定のIDを持つ資格情報をデータベースから取得する。

    Args:
        qualification_id (int): 取得する資格のID。
        db_session (Session): SQLAlchemyのセッションインスタンス。

    Returns:
        QualificationModel: 取得された資格のモデルインスタンス。

    Raises:
        Exception: データベース操作中に例外が発生した場合。
    """
    try:
        result: Result = await db_session.execute(
            select(QualificationModel).filter(
                QualificationModel.id == qualification_id)
        )
        get_qualification_data = result.scalar()
        return get_qualification_data

    except Exception as exception:
        raise exception


async def get_all_qualifications(db_session: Session) -> list[QualificationModel]:
    """
    すべての資格情報をデータベースから取得する。

    Args:
        db_session (Session): SQLAlchemyのセッションインスタンス。

    Returns:
        list[QualificationModel]: すべての資格のモデルインスタンスのリスト。

    Raises:
        Exception: データベース操作中に例外が発生した場合。
    """
    try:
        result: Result = await db_session.execute(
            select(
                QualificationModel.id,
                QualificationModel.name,
                QualificationModel.description
            )
        )
        get_all_qualifications_data = result.all()
        return get_all_qualifications_data

    except Exception as exception:
        raise exception


async def update_qualification(qualification_id: int, qualification_data: QualificationUpdate, db_session: Session) -> QualificationModel:
    """
    特定のIDを持つ資格情報を更新する。

    Args:
        qualification_id (int): 更新する資格のID。
        qualification_data (QualificationUpdate): 更新する資格の新しいデータ。
        db_session (Session): SQLAlchemyのセッションインスタンス。

    Returns:
        QualificationModel: 更新された資格のモデルインスタンス。

    Raises:
        Exception: データベース操作中に例外が発生した場合。
    """
    try:
        result: Result = await db_session.execute(
            select(QualificationModel).filter(
                QualificationModel.id == qualification_id)
        )
        existing_qualification = result.scalar()

        existing_qualification.name = qualification_data.name
        existing_qualification.description = qualification_data.description
        db_session.add(existing_qualification)
        await db_session.commit()
        await db_session.refresh(existing_qualification)
        return existing_qualification

    except Exception as exception:
        raise exception


async def delete_qualification(qualification_id: int, db_session: Session) -> bool:
    """
    特定のIDを持つ資格情報をデータベースから削除する。

    Args:
        qualification_id (int): 削除する資格のID。
        db_session (Session): SQLAlchemyのセッションインスタンス。

    Returns:
        bool: 削除操作が成功した場合はTrue、失敗した場合はFalse。

    Raises:
        Exception: データベース操作中に例外が発生した場合。
    """
    try:
        result: Result = await db_session.execute(
            select(QualificationModel).filter(
                QualificationModel.id == qualification_id)
        )
        qualification_to_delete = result.scalar()

        await db_session.delete(qualification_to_delete)
        await db_session.commit()
        return True

    except Exception as exception:
        raise exception
