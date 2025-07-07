from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date

router = APIRouter()


@router.get("/items", summary="Get all items")
async def get_all_items():
    # DB에서 아이템 목록 조회
    return [{"id": 1, "name": "아이템1"}, {"id": 2, "name": "아이템2"}]


@router.get("/items/{item_id}", summary="Get item detail")
async def get_item_detail(item_id: int):
    # DB에서 item_id에 해당하는 정보 조회
    return {"id": item_id, "name": "아이템1", "category": "재료", "grade": "희귀"}


@router.get("/prices/{item_id}", summary="Get item price history")
async def get_price_history(item_id: int):
    # 해당 아이템의 시세 타임라인 조회
    return {
        "item_id": item_id,
        "prices": [
            {"timestamp": "2025-07-01", "price": 1200},
            {"timestamp": "2025-07-02", "price": 1350},
        ]
    }


@router.get("/predict/{item_id}", summary="Get prediction for specific item")
async def get_prediction(item_id: int):
    # 예측 결과 반환
    return {
        "item_id": item_id,
        "model": "ARIMA",
        "predictions": [
            {"date": "2025-07-08", "predicted_price": 1400},
            {"date": "2025-07-09", "predicted_price": 1450},
        ]
    }


@router.get("/predict", summary="Get predictions for all items")
async def get_all_predictions():
    # 전체 예측 결과 리스트 요약
    return [
        {"item_id": 1, "predicted_price": 1400},
        {"item_id": 2, "predicted_price": 2300}
    ]


@router.post("/predict/train", summary="Trigger training and prediction")
async def trigger_train():
    # Airflow trigger or 내부 학습 로직 실행
    return {"message": "Training and prediction triggered"}


@router.get("/logs/train", summary="Get training logs")
async def get_training_logs():
    return [
        {"model": "ARIMA", "trained_at": "2025-07-07", "status": "SUCCESS"},
        {"model": "LSTM", "trained_at": "2025-07-05", "status": "FAILURE"}
    ]


@router.get("/health", summary="API health check")
async def health_check():
    return {"status": "ok"}
