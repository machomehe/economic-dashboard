import os
import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone

FRED_API_KEY = os.environ.get('FRED_API_KEY', '')

SERIES_IDS = [
    # 유동성
    'FEDFUNDS', 'DFII10', 'DGS10', 'DGS2', 'T10Y2Y', 'M2SL', 'WALCL',
    # 성장
    'DGORDER', 'UNRATE', 'PAYEMS', 'INDPRO', 'A191RL1Q225SBEA', 'NAPM', 'ICSA',
    # 인플레
    'CPIAUCSL', 'CPILFESL', 'PCEPILFE', 'T10YIE', 'DCOILWTICO',
    # 위험/시장
    'BAMLH0A0HYM2', 'BAMLC0A4CBBB', 'STLFSI4', 'VIXCLS', 'DTWEXBGS',
    # 시장지표
    'SP500', 'NASDAQCOM', 'DEXKOUS',
]

def fetch_series(series_id):
    params = urllib.parse.urlencode({
        'series_id': series_id,
        'api_key': FRED_API_KEY,
        'file_type': 'json',
        'sort_order': 'desc',
        'limit': 60,
    })
    url = 'https://api.stlouisfed.org/fred/series/observations?' + params
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
            if 'error_message' in data:
                print(f'  ERROR {series_id}: {data["error_message"]}')
                return []
            obs = data.get('observations', [])
            return [{'date': o['date'], 'value': o['value']} for o in obs]
    except Exception as e:
        print(f'  FAILED {series_id}: {e}')
        return []

def main():
    if not FRED_API_KEY:
        print('FRED_API_KEY not set')
        return

    result = {}
    for sid in SERIES_IDS:
        print(f'Fetching {sid}...')
        result[sid] = fetch_series(sid)

    output = {
        'updated': datetime.now(timezone.utc).isoformat(),
        'data': result,
    }

    with open('data.json', 'w') as f:
        json.dump(output, f, separators=(',', ':'))

    print(f'Done. data.json updated at {output["updated"]}')

if __name__ == '__main__':
    main()
