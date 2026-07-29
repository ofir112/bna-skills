#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BNA fund-compare: fetch official Israeli fund data (Gemelnet/Pensianet) from data.gov.il.

Official Ministry of Finance open data. No API key needed.
Usage examples:
  python3 fetch_funds.py --db gemel --classification "קרנות השתלמות" --sort fee
  python3 fetch_funds.py --db gemel --classification "קרנות השתלמות" --sort yield5 --top 20
  python3 fetch_funds.py --db pensia --sort yield5
  python3 fetch_funds.py --db gemel --name הראל
Output: JSON to stdout (latest report period only), ready for analysis/tables.
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

RESOURCES = {
    # data.gov.il CKAN datastore resource IDs (verified live 2026-07)
    'gemel': 'a30dcbea-a1d2-482c-ae29-8f781f5025fb',   # נתוני הגמל-נט 2024-היום
    'pensia': '6d47d6b5-cb08-488b-b333-f1e717b1e1bd',  # נתוני הפנסיה-נט 2024-היום
}
API = 'https://data.gov.il/api/3/action/datastore_search'
PAGE = 1000


def fetch_all(resource_id, filters=None, q=None):
    records, offset = [], 0
    while True:
        params = {'resource_id': resource_id, 'limit': PAGE, 'offset': offset}
        if filters:
            params['filters'] = json.dumps(filters, ensure_ascii=False)
        if q:
            params['q'] = q
        url = API + '?' + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=60) as resp:
            data = json.load(resp)
        if not data.get('success'):
            raise RuntimeError('data.gov.il returned success=false')
        batch = data['result']['records']
        records.extend(batch)
        offset += PAGE
        if offset >= data['result']['total'] or not batch:
            return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', choices=['gemel', 'pensia'], default='gemel')
    ap.add_argument('--classification', help='FUND_CLASSIFICATION exact filter, e.g. "קרנות השתלמות"')
    ap.add_argument('--name', help='free-text search across fields (fund/company name)')
    ap.add_argument('--sort', choices=['fee', 'yield5', 'yield3', 'sharpe', 'assets'], default='fee')
    ap.add_argument('--top', type=int, default=0, help='limit output rows (0 = all)')
    args = ap.parse_args()

    filters = {'FUND_CLASSIFICATION': args.classification} if args.classification else None
    records = fetch_all(RESOURCES[args.db], filters=filters, q=args.name)
    if not records:
        print(json.dumps({'error': 'no records', 'hint': 'check classification spelling'}, ensure_ascii=False))
        return

    latest = max(r['REPORT_PERIOD'] for r in records)
    rows = [r for r in records if r['REPORT_PERIOD'] == latest]

    def num(r, k):
        v = r.get(k)
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    out = []
    for r in rows:
        out.append({
            'fund_id': r.get('FUND_ID'),
            'name': (r.get('FUND_NAME') or '').strip(),
            'classification': r.get('FUND_CLASSIFICATION'),
            'company': r.get('MANAGING_CORPORATION'),
            'specialization': r.get('SPECIALIZATION'),
            'sub_specialization': r.get('SUB_SPECIALIZATION'),
            'report_period': r.get('REPORT_PERIOD'),
            'fee_from_balance_pct': num(r, 'AVG_ANNUAL_MANAGEMENT_FEE'),
            'fee_from_deposit_pct': num(r, 'AVG_DEPOSIT_FEE'),
            'yield_ytd_pct': num(r, 'YEAR_TO_DATE_YIELD'),
            'avg_annual_yield_3y_pct': num(r, 'AVG_ANNUAL_YIELD_TRAILING_3YRS'),
            'avg_annual_yield_5y_pct': num(r, 'AVG_ANNUAL_YIELD_TRAILING_5YRS'),
            'std_dev': num(r, 'STANDARD_DEVIATION'),
            'sharpe': num(r, 'SHARPE_RATIO'),
            'total_assets_mils': num(r, 'TOTAL_ASSETS'),
        })

    sort_key = {
        'fee': lambda x: (x['fee_from_balance_pct'] is None, x['fee_from_balance_pct'] or 0),
        'yield5': lambda x: (x['avg_annual_yield_5y_pct'] is None, -(x['avg_annual_yield_5y_pct'] or 0)),
        'yield3': lambda x: (x['avg_annual_yield_3y_pct'] is None, -(x['avg_annual_yield_3y_pct'] or 0)),
        'sharpe': lambda x: (x['sharpe'] is None, -(x['sharpe'] or 0)),
        'assets': lambda x: (x['total_assets_mils'] is None, -(x['total_assets_mils'] or 0)),
    }[args.sort]
    out.sort(key=sort_key)
    if args.top:
        out = out[:args.top]

    print(json.dumps({
        'source': f'data.gov.il ({args.db}net) - Ministry of Finance official open data',
        'latest_report_period': latest,
        'fund_count': len(out),
        'funds': out,
    }, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
