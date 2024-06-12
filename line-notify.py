import requests
import os
import time

def send_image_via_line_notify(token, image_path, message=""):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "message": message
    }
    files = {
        "imageFile": open(image_path, "rb")
    }

    response = requests.post(url, headers=headers, data=payload, files=files)
    return response.status_code, response.text

message = 'Here is a strange person:'
folder_name = 'imgs'

line_notify_token = os.environ.get("LINE_NOTIFY_TOKEN")
if line_notify_token is None:
    raise RuntimeError("LINE_NOTIFY_TOKEN must be provided")

while True:
    # 記錄前一個資料夾的檔案列表
    prev_files = os.listdir(folder_name)

    # 等待一段時間以便檢測新的檔案
    time.sleep(1)

    # 記錄現在的資料夾的檔案列表
    curr_files = os.listdir(folder_name)

    # 將兩個檔案列表進行比較
    new_files = [f for f in curr_files if f not in prev_files]

    # 印出新的檔案的檔名
    for f in new_files:
        image_path = f'imgs/{f}'
        status_code, response_text = send_image_via_line_notify(line_notify_token, image_path, message)
        print(f"Status Code: {status_code}")
        print(f"Response: {response_text}")

