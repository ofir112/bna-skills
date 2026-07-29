#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BNA stock-report: fetch real company data for a US or Israeli (TASE) ticker.

Sources:
  - SEC EDGAR official API (US-listed): real filed financials. Requires User-Agent header.
  - yfinance (unofficial Yahoo Finance): prices + financial statements, incl. TASE (.TA).
GOTCHA: yfinance returns TASE prices in AGOROT (currency code "ILA") - divide by 100 for ILS.

Usage:
  python3 fetch_company.py AAPL
  python3 fetch_company.py ESLT.TA
Requires: pip install yfinance
Output: JSON to stdout.
"""
import json
import sys
import urllib.request

UA = {'User-Agent': 'BNA-Skills research contact@bna.ai'}


def edgar_lookup(ticker):
    """US tickers: resolve CIK and pull key annual facts from official EDGAR filings."""
    try:
        req = urllib.request.Request('https://www.sec.gov/files/company_tickers.json', headers=UA)
        tickers = json.load(urllib.request.urlopen(req, timeout=30))
        match = next((v for v in tickers.values() if v['ticker'] == ticker.upper()), None)
        if not match:
            return None
        cik = f"CIK{match['cik_str']:010d}"
        req = urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/{cik}.json', headers=UA)
        facts = json.load(urllib.request.urlopen(req, timeout=60))

        def annual_series(tags, unit='USD', n=5):
            gaap = facts['facts'].get('us-gaap', {})
            for tag in tags:
                if tag not in gaap or unit not in gaap[tag].get('units', {}):
                    continue
                rows = [u for u in gaap[tag]['units'][unit] if u.get('form') == '10-K' and u.get('fp') == 'FY']
                dedup = {}
                for u in rows:
                    dedup[u['end']] = u['val']
                if dedup:
                    return [{'period_end': k, 'value': v} for k, v in sorted(dedup.items())][-n:]
            return None

        return {
            'source': 'SEC EDGAR (official filings)',
            'entity': facts.get('entityName'),
            'cik': cik,
            'revenue_annual': annual_series(['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues', 'SalesRevenueNet']),
            'net_income_annual': annual_series(['NetIncomeLoss']),
            'total_assets': annual_series(['Assets']),
            'total_liabilities': annual_series(['Liabilities']),
            'operating_cash_flow': annual_series(['NetCashProvidedByUsedInOperatingActivities']),
            'filings_url': f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=10-K",
        }
    except Exception as e:
        return {'error': f'EDGAR unavailable: {e}'}


def yahoo_lookup(ticker):
    """Prices + statements via yfinance. Handles the TASE agorot gotcha."""
    try:
        import yfinance as yf
    except ImportError:
        return {'error': 'yfinance not installed - run: pip install yfinance'}
    try:
        t = yf.Ticker(ticker)
        fi = t.fast_info
        price, currency = fi['lastPrice'], fi['currency']
        mcap = fi.get('marketCap')
        note = None
        if currency == 'ILA':  # Tel Aviv prices arrive in agorot
            price, mcap = price / 100, (mcap / 100 if mcap else None)
            currency, note = 'ILS', 'converted from agorot (ILA/100)'
        out = {
            'source': 'Yahoo Finance via yfinance (unofficial)',
            'price': round(price, 2),
            'currency': currency,
            'market_cap': mcap,
            'note': note,
            'high_52w': fi.get('yearHigh'),
            'low_52w': fi.get('yearLow'),
        }
        try:
            inc = t.income_stmt
            years = [str(c)[:10] for c in inc.columns[:4]]
            def row(name):
                if name in inc.index:
                    return {years[i]: (None if inc.loc[name].iloc[i] != inc.loc[name].iloc[i] else float(inc.loc[name].iloc[i]))
                            for i in range(min(4, len(years)))}
                return None
            out['income_statement'] = {
                'statement_currency': t.info.get('financialCurrency'),
                'total_revenue': row('Total Revenue'),
                'gross_profit': row('Gross Profit'),
                'operating_income': row('Operating Income'),
                'net_income': row('Net Income'),
            }
        except Exception as e:
            out['income_statement'] = {'error': str(e)}
        return out
    except Exception as e:
        return {'error': f'yfinance failed: {e}'}


def main():
    if len(sys.argv) != 2:
        print(json.dumps({'error': 'usage: fetch_company.py TICKER (e.g. AAPL or ESLT.TA)'}))
        sys.exit(1)
    ticker = sys.argv[1].upper()
    is_tase = ticker.endswith('.TA')
    result = {'ticker': ticker, 'market': 'TASE (Tel Aviv)' if is_tase else 'US'}
    result['yahoo'] = yahoo_lookup(ticker)
    if not is_tase:
        result['edgar'] = edgar_lookup(ticker)
    else:
        result['maya_note'] = ('Official Israeli filings are on Maya (maya.tase.co.il) - it blocks automated '
                               'access, so link the user there for the actual reports.')
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
