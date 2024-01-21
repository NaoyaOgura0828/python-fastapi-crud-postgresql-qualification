from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from cruds.qualification_crud import create_qualification, get_qualification, get_all_qualifications, update_qualification, delete_qualification
from db_connection import create_db_session
from schemas.qualification_schema import QualificationCreate, QualificationRead, QualificationUpdate


endpoint = APIRouter()


@endpoint.post("/api/qualification/", response_model=QualificationRead)
async def post_qualification_endpoint(qualification_data: QualificationCreate, db_session: Session = Depends(create_db_session)):
    """
    新しい資格を作成し、データベースに保存する。

    Args:
        qualification_data (QualificationCreate): 新しい資格のデータ。
        db_session (Session, optional): データベースセッション。デフォルトはcreate_db_session。

    Returns:
        QualificationRead: 作成された資格のデータ。

    Raises:
        HTTPException: 資格の作成中にエラーが発生した場合。
    """
    try:
        result = await create_qualification(qualification_data, db_session)
        return result
    except HTTPException as error:
        raise error


@endpoint.get("/api/qualification/{qualification_id}", response_model=QualificationRead)
async def get_qualification_endpoint(qualification_id: int, db_session: Session = Depends(create_db_session)):
    """
    指定されたIDを持つ資格をデータベースから取得する。

    Args:
        qualification_id (int): 取得する資格のID。
        db_session (Session, optional): データベースセッション。デフォルトはcreate_db_session。

    Returns:
        QualificationRead: 取得された資格のデータ。

    Raises:
        HTTPException: 指定されたIDの資格が見つからない場合。
    """
    try:
        result = await get_qualification(qualification_id, db_session)
        return result
    except HTTPException as error:
        raise error


@endpoint.get("/api/qualification/", response_model=List[QualificationRead])
async def get_all_qualifications_endpoint(db_session: Session = Depends(create_db_session)):
    """
    データベースから全ての資格データを取得する。

    Args:
        db_session (Session, optional): データベースセッション。デフォルトはcreate_db_session。

    Returns:
        List[QualificationRead]: データベースに存在する全ての資格のリスト。

    Raises:
        HTTPException: 資格データの取得中にエラーが発生した場合。
    """
    try:
        result = await get_all_qualifications(db_session)
        return result
    except HTTPException as error:
        raise error


@endpoint.put("/api/qualification/{qualification_id}", response_model=QualificationRead)
async def update_qualification_endpoint(qualification_id: int, qualification_data: QualificationUpdate, db_session: Session = Depends(create_db_session)):
    """
    指定されたIDの資格を更新する。

    Args:
        qualification_id (int): 更新する資格のID。
        qualification_data (QualificationCreate): 更新する資格の新しいデータ。
        db_session (Session, optional): データベースセッション。デフォルトはcreate_db_session。

    Returns:
        QualificationRead: 更新された資格のデータ。

    Raises:
        HTTPException: 資格の更新中にエラーが発生した場合。
    """
    try:
        result = await update_qualification(qualification_id, qualification_data, db_session)
        return result
    except HTTPException as error:
        raise error


@endpoint.delete("/api/qualification/{qualification_id}")
async def delete_qualification_endpoint(qualification_id: int, db_session: Session = Depends(create_db_session)):
    """
    指定されたIDの資格をデータベースから削除する。

    Args:
        qualification_id (int): 削除する資格のID。
        db_session (Session, optional): データベースセッション。デフォルトはcreate_db_session。

    Returns:
        result: 削除操作の成否。

    Raises:
        HTTPException: 資格の削除中にエラーが発生した場合。
    """
    try:
        result = await delete_qualification(qualification_id, db_session)
        return result
    except HTTPException as error:
        raise error
