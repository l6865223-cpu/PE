#!/usr/bin/env python3
"""
Pikmin Bloom Threads Info Organizer for PE repository
幫助整理與新增來自 Threads 的皮克敏文章資訊至當月或下個月的 Markdown 檔案中。
"""

import os
from datetime import datetime

def add_thread_info(month_type, title, source, content):
    """
    month_type: 'current' 或 'next'
    title: 文章標題或主題
    source: Threads 作者或連結
    content: 筆記內容
    """
    filename = "current_month.md" if month_type == "current" else "next_month.md"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    entry = f"\n- **{title}**\n  - 來源/作者：{source}\n  - 內容摘要：{content}\n  - 記錄時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = f.read()
        # 簡單附加到檔案結尾
        data += entry
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"已成功新增資訊至 {filename}！")
    else:
        print(f"找不到檔案 {filepath}")

if __name__ == "__main__":
    print("=== Pikmin Bloom Threads 資訊整理工具 ===")
    print("你可以透過此腳本快速將 Threads 收集到的皮克敏資訊寫入對應的 Markdown 檔案中。")
    # 範例使用：
    # add_thread_info('current', '9月社群日花朵討論', '@player_threads', '本月石蒜機率很高...')
