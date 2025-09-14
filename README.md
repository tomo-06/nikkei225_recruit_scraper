
# nikkei225_recruit_scraper
このリポジトリは、日経225に採用されている企業の公式ホームページから「採用ページ」のリンクを自動収集するスクレイピングツールです。  
クラウドソーシング案件のポートフォリオとして作成しました。

# 注意
取得できない企業があります（約35社/225社）。
主に 航空会社・ガス会社などサービス提供企業は、公式サイトが「サービス利用ページ」中心で構成されており、採用情報へのリンクが存在しない場合があります。

---

## 機能概要

1. **日経225銘柄一覧ページから銘柄リストを取得**
   - 企業名と詳細ページのリンクを収集
   - Selenium を利用してブラウザ操作を自動化

2. **各企業の公式HPを取得**
   - 詳細ページから公式HPリンクを抽出

3. **公式HPから新卒採用ページを探索**
   - BeautifulSoup を利用して HTML を解析
   - 「採用」「新卒」「recruit」「saiyo」「career」といったキーワードを含むリンクを探索

4. **結果をCSVファイルとして保存**
   - `nikkei225_recruit_list.csv` に出力

---

## 使用技術

- Python 3.x
- Selenium
- BeautifulSoup4
- pandas
- requests
- ChromeDriver（webdriver-manager経由）

---

## 実行方法

### 1. リポジトリをクローン
任意のディレクトリにリポジトリをクローンします。

```bash
git clone https://github.com/<ユーザー名>/cnikkei225_recruit_scraper
cd nikkei225_recruit_scraper
````

### 2. 仮想環境の作成（任意）

他のプロジェクトに影響を与えずに実行する場合は仮想環境を作成します。

```bash
python -m venv venv
```

### 3. 仮想環境を有効化

* Linux / macOS:

```bash
source venv/bin/activate
```

* Windows:

```cmd
venv\Scripts\activate
```

### 4. 必要ライブラリのインストール

```bash
pip install -r requirements.txt
```

### 5. スクリプトの実行

```bash
python main.py
```

### 6. 仮想環境の無効化（終了時）

```bash
deactivate
```

