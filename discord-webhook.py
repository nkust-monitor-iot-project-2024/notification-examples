import os
from discord_webhook import DiscordWebhook

# 定義 webhook URL
webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
if webhook_url is None:
    raise RuntimeError("DISCORD_WEBHOOK_URL must be provided")

# 創建一個 webhook 實例
webhook = DiscordWebhook(url=webhook_url, content='Here is a strange person:')

# 以二進制模式打開本地照片文件
with open(r'', 'rb') as file:
    webhook.add_file(file=file.read(), filename='image.jpg')

# 發送 webhook
response = webhook.execute()

# 檢查響應
print(response.status_code)
print(response.content)


