# ライブラリのインポート
import pandas as pd
import numpy as np
import time
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# ======================
# 1. 日経225銘柄リスト取得
# ======================

# Chromeのオプション設定
chrome_options = Options()
chrome_options.add_argument("--lang=ja")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless=new")

# 日経225銘柄一覧ページURL
nikkei_url = "https://www.traders.co.jp/market_jp/nikkei225"
# スクレイピング間隔（秒）
SLEEP_TIME = 1

def get_nikkei225_list():
    # chromeドライバーのオプション設定
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 日経225銘柄一覧ページにアクセス
    driver.get(nikkei_url)
    time.sleep(SLEEP_TIME)

    # 銘柄名・リンク・業種を取得
    link_list = []
    link_text = driver.find_elements(By.CSS_SELECTOR, ".text-nowrap a")
    for link in link_text:
        # 銘柄名を取得して、\u3000を空白に置換
        text = link.text.strip().replace("\u3000", " ")
        href = link.get_attribute("href")
        # 銘柄名が空白の場合は除外する
        if not text.split():
            continue
        link_list.append({"銘柄名": text, "詳細ページ": href})
    # 公式HPリンクを取得
    company_list = []
    for company in link_list:
        driver.get(company["詳細ページ"])
        time.sleep(SLEEP_TIME)
        try:
            official_link = driver.find_element(By.CSS_SELECTOR, ".data_table a").get_attribute("href")
        except:
            official_link = None
        company_list.append({"銘柄名": company["銘柄名"], "公式HP": official_link})
    driver.quit()
    return company_list


# ======================
# 2. 各企業の採用ページ取得
# ======================

def get_recruit_page(base_url):
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(base_url)
        time.sleep(3)  # JS描画待ち
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
        keywords = ["採用", "新卒", "recruit", "saiyo", "career"]
        candidates = []
        for a in soup.find_all("a", href=True):
            text = a.get_text(strip=True).replace("\u3000", " ").lower()
            href = a["href"].lower()
            if any(kw in text for kw in keywords) or any(kw in href for kw in keywords):
                candidates.append(urljoin(base_url, a["href"]))
        if candidates:
            return candidates[0]
    except Exception as e:
        print(f"Error fetching {base_url}: {e}")

    return None


# ======================
# 実行処理
# ======================
if __name__ == "__main__":
    # ① 銘柄リスト取得
    nikkei225_list = get_nikkei225_list()

    # ② 採用ページ探索
    results = []
    for company in nikkei225_list:
        name = company["銘柄名"]
        official_url = company["公式HP"]

        recruit_url = None
        if official_url:
            recruit_url = get_recruit_page(official_url)

        results.append({
            "銘柄名": name,
            "公式HP": official_url,
            "新卒採用ページ": recruit_url if recruit_url else "Not Found"
        })
        print(f"{name}: {recruit_url}")

    # ③ CSV出力
    df = pd.DataFrame(results)
    df.to_csv("nikkei225_recruit_list.csv", index=False, encoding="utf-8-sig")
    print("新卒採用ページリストを保存しました！")