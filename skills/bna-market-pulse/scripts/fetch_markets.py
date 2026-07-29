#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BNA market-pulse: live multi-market snapshot + cross-market period comparison.

Sources:
  - yfinance (unofficial Yahoo Finance): indices, FX, commodities. Live-tested symbols only.
  - Bank of Israel official public API: the official USD/ILS representative rate.
Requires: pip install yfinance

Usage:
  python3 fetch_markets.py snapshot
  python3 fetch_markets.py compare --period ytd
  python3 fetch_markets.py compare --period 1y --usd-adjust
Periods: 5d, 1mo, 3mo, 6mo, ytd, 1y, 5y
Output: JSON to stdout.
"""
import argparse
import json
import sys
import urllib.request

# Live-tested 2026-07: note TA-35 works WITHOUT the caret prefix.
GROUPS = {
    'israel': [('^TA125.TA', 'ת"א 125'), ('TA35.TA', 'ת"א 35')],
    'us': [('^GSPC', 'S&P 500'), ('^IXIC', 'נאסד"ק'), ('^DJI', "דאו ג'ונס"), ('^VIX', 'VIX (מדד התנודתיות)')],
    'europe_asia': [('^GDAXI', 'דאקס (גרמניה)'), ('^FTSE', 'פוטסי (לונדון)'), ('^N225', 'ניקיי (יפן)'), ('^HSI', 'האנג סנג (הונג קונג)')],
    'fx': [('ILS=X', 'דולר/שקל'), ('EURILS=X', 'אירו/שקל')],
    'commodities': [('GC=F', 'זהב'), ('CL=F', 'נפט WTI')],
    'crypto': [('BTC-USD', 'ביטקוין (דולר)')],
}
COMPARE_SET = [('^TA125.TA', 'ת"א 125'), ('^GSPC', 'S&P 500'), ('^IXIC', 'נאסד"ק'),
               ('^GDAXI', 'דאקס'), ('^N225', 'ניקיי'), ('^HSI', 'האנג סנג')]


def boi_official_usd():
    """Official Bank of Israel representative USD/ILS rate (שער יציג)."""
    try:
        with urllib.request.urlopen('https://boi.org.il/PublicApi/GetExchangeRates?asJson=true', timeout=20) as r:
            data = json.load(r)
        usd = next(x for x in data['exchangeRates'] if x['key'] == 'USD')
        return {'rate': usd['currentExchangeRate'], 'last_update': usd['lastUpdate'],
                'source': 'Bank of Israel official API (שער יציג)'}
    except Exception as e:
        return {'error': f'BOI API unavailable: {e}'}


def snapshot():
    import yfinance as yf
    out = {'mode': 'snapshot', 'groups': {}, 'boi_official_usd_ils': boi_official_usd(),
           'source_note': 'Index/FX/commodity quotes via yfinance (unofficial, may be delayed); official ILS rate from Bank of Israel.'}
    for group, symbols in GROUPS.items():
        rows = []
        for sym, name in symbols:
            try:
                fi = yf.Ticker(sym).fast_info
                price, prev = fi['lastPrice'], fi.get('previousClose')
                rows.append({'name': name, 'symbol': sym, 'price': round(price, 2),
                             'day_change_pct': round((price / prev - 1) * 100, 2) if prev else None})
            except Exception as e:
                rows.append({'name': name, 'symbol': sym, 'error': type(e).__name__})
        out['groups'][group] = rows
    return out


def compare(period, usd_adjust):
    import yfinance as yf

    def pct_change(sym):
        h = yf.Ticker(sym).history(period=period)['Close'].dropna()
        if len(h) < 2:
            return None, None, None
        return float(h.iloc[0]), float(h.iloc[-1]), (float(h.iloc[-1]) / float(h.iloc[0]) - 1) * 100

    fx_first = fx_last = None
    if usd_adjust:
        fx_first, fx_last, _ = pct_change('ILS=X')  # USD/ILS

    rows = []
    for sym, name in COMPARE_SET:
        try:
            first, last, chg = pct_change(sym)
            if chg is None:
                rows.append({'name': name, 'symbol': sym, 'error': 'not enough history'})
                continue
            row = {'name': name, 'symbol': sym, 'change_pct': round(chg, 2)}
            if usd_adjust and sym.endswith('.TA') and fx_first and fx_last:
                # TA index is shekel-denominated; convert both ends to USD terms
                usd_chg = ((last / fx_last) / (first / fx_first) - 1) * 100
                row['change_pct_usd_terms'] = round(usd_chg, 2)
            rows.append(row)
        except Exception as e:
            rows.append({'name': name, 'symbol': sym, 'error': type(e).__name__})
    out = {'mode': 'compare', 'period': period, 'indices': rows,
           'source_note': 'yfinance history (unofficial). Percent change over the requested period.'}
    if usd_adjust:
        out['usd_ils_move_pct'] = round((fx_last / fx_first - 1) * 100, 2) if fx_first and fx_last else None
        out['note'] = 'change_pct_usd_terms shows TASE indices converted to dollar terms - comparable to US indices.'
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['snapshot', 'compare'])
    ap.add_argument('--period', default='ytd', choices=['5d', '1mo', '3mo', '6mo', 'ytd', '1y', '5y'])
    ap.add_argument('--usd-adjust', action='store_true')
    args = ap.parse_args()
    try:
        import yfinance  # noqa: F401
    except ImportError:
        print(json.dumps({'error': 'yfinance not installed - run: pip install yfinance'}))
        sys.exit(1)
    result = snapshot() if args.mode == 'snapshot' else compare(args.period, args.usd_adjust)
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
