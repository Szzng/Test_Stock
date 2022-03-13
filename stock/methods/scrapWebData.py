import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/92.0.4515.107 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = bs(res.text, 'lxml')
    return soup


def get_risingstock_df(num=100):
    columns = ['rank', 'name', 'code', 'curprice', 'diff', 'ratio', 'volume',
               '매수호가', '매도호가', '매수총잔량', '매도총잔량', 'per', 'roe']
    df = pd.DataFrame(columns=columns)

    for n in range(2):
        url = f'https://finance.naver.com/sise/sise_rise.nhn?sosok={n}'
        soup = create_soup(url)
        rows = soup.find("table", class_="type_2").find_all("tr")
        for row in rows[1:]:
            items = row.find_all('td')
            if len(items) <= 1: continue
            data = []
            for item in items:
                data.append(item.get_text().strip())
                code = item.find('a', class_='tltle')
                if code:
                    data.append(code['href'][-6:])
            df.loc[len(df)] = data

    df = df[['code', 'name', 'curprice', 'diff', 'ratio', 'volume', 'per', 'roe']]

    df['ratio'] = df['ratio'].apply(lambda x: re.search('[0-9]+[.][0-9]+', x).group())
    df['ratio'] = df['ratio'].astype(float)
    df = df.sort_values(by=['ratio'], ascending=False)[:num]

    for i in ['curprice', 'diff', 'volume', 'per', 'roe']:
        df[i] = df[i].apply(lambda x: x.replace(',', ''))
    df.replace('N/A', -999, inplace=True)
    df[['curprice', 'diff', 'volume']] = df[['curprice', 'diff', 'volume']].astype(int)
    df[['per', 'roe']] = df[['per', 'roe']].astype(float)

    return df


def get_latest_news_df(keywords, pages=3):
    columns = ['keyword', 'title', 'url', 'written_at']
    df = pd.DataFrame(columns=columns)

    for keyword in keywords:
        for page in range(pages):
            url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=1&photo=0&field' \
                  f'=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,' \
                  f'p:all,a:all&start={page}1 '
            soup = create_soup(url)
            newsgroup = soup.find('ul', class_='list_news')
            if newsgroup:
                newslist = newsgroup.find_all('li')
                for news in newslist:
                    a_tag = news.find('a', class_='news_tit')
                    title = a_tag['title']
                    link = a_tag['href']
                    written_at = news.find('span', class_='info').get_text().strip()
                    df.loc[len(df)] = [keyword, title, link, written_at]
            else:
                break
    return df
