from src.models.money_model import MoneyModel
import httpx

class CurrencyService:

    @staticmethod
    async def convert_currency(money: MoneyModel):
        api_url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{money.source_currency.lower()}.json"
        
        async with httpx.AsyncClient() as client:
                response = await client.get(api_url)
                data = response.json()
        
        exchange_rate = float(
                data[money.source_currency][money.target_currency]
        )

        return {
                'amount': round(money.amount * exchange_rate, 2),
                'currency': money.target_currency
                }
