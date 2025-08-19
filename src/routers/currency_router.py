from fastapi import Body
from fastapi.routing import APIRouter
from src.models.money_model import MoneyModel
from src.services.currency_service import CurrencyService

router = APIRouter(
    prefix='/currency',
    tags=['Currency']
)

@router.post('/convert-currency')
async def convert_currency(money: MoneyModel = Body()):
    return await CurrencyService.convert_currency(money=money)