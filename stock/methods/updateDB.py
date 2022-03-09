import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock.settings")
import django
django.setup()

import pandas as pd
from stock.methods.scrapWebData import get_risingstock_df, get_latest_news_df
from risingstock.models import RisingStock, NewsOfRisingStock
from mynews.models import Keyword, NewsOfKeyword


def update_risingstock_db(num=80, pages=3):
    stocks = get_risingstock_df(num)
    news = get_latest_news_df(keywords=stocks['name'], pages=pages)
    news_with_code = pd.merge(stocks[['code', 'name']], news, left_on='name', right_on='keyword', how='inner')

    RisingStock.objects.all().delete()

    for r in stocks.itertuples():
        RisingStock(code=r.code, name=r.name, curprice=r.curprice, ratio=r.ratio, diff=r.diff,
                    volume=r.volume, per=r.per, roe=r.roe).save()

    for r in news_with_code.itertuples():
        NewsOfRisingStock(code_id=r.code, keyword=r.keyword, title=r.title, url=r.url, written_at=r.written_at).save()


def update_mynews_db(pages=2):
    keywords = Keyword.objects.all()
    mynews = get_latest_news_df(keywords=keywords, pages=pages)

    NewsOfKeyword.objects.all().delete()

    for r in mynews.itertuples():
        NewsOfKeyword(keyword=r.keyword, title=r.title, url=r.url, written_at=r.written_at).save()


update_risingstock_db()
update_mynews_db()
