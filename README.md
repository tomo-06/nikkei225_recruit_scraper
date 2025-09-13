#============================================
必要ライブラリをインストール
#============================================
pip install python-dotenv google-generativeai


#============================================
Ubuntuの環境にChromeをインストール
#============================================
#Googleの公開キーを追加
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

#リポジトリを追加
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

#更新とインストール
sudo apt-get update
sudo apt-get install -y google-chrome-stable
