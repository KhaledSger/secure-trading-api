from django.shortcuts import render
from .models import Trade, Asset
import requests

def trade_list(request):
    assets = Asset.objects.all()
    asset_ids = [asset.name.lower() for asset in assets]
    
    if asset_ids:
        api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(asset_ids)}&vs_currencies=usd"
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for bad status codes
            prices = response.json()
            
            for asset in assets:
                asset_name_lower = asset.name.lower()
                if asset_name_lower in prices and 'usd' in prices[asset_name_lower]:
                    asset.current_price = prices[asset_name_lower]['usd']
                    asset.save()
        except requests.exceptions.RequestException as e:
            # Handle API errors gracefully
            print(f"Error fetching prices from CoinGecko: {e}")

    trades = Trade.objects.all().order_by('-timestamp')
    return render(request, 'trades/trade_list.html', {'trades': trades, 'assets': assets})

def handler404(request, exception):
    return render(request, '404.html', status=404)

