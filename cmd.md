# ping with windows
ping 8.8.8.8 -c 4  

# ping forom windows to kali-linux
wsl ping 8.8.8.8 -c 4

🔹 1. nmap

用途：網路掃描器。

功能：偵測一台電腦或伺服器有哪些「開放的 Port」、執行什麼服務（HTTP、FTP、SSH…）、可能的作業系統。

舉例：

nmap -sV -p 4173 192.168.0.132


-sV = 掃描並嘗試判斷服務版本

-p 4173 = 只掃 port 4173（你的網站）
👉 可以幫你確認「4173 port 是不是 Vite / Node.js 在跑」。

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
