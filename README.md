# Notification Examples

The single-executable Python file that sends stuff to LINE Notify and Discord (by Webhook).

- `line-notify.py`: send images to LINE with LINE Notify
  - You should provide your token with the environment variable, `LINE_NOTIFY_TOKEN`.
  - You should place the images to send in the directory, `imgs`.
- `discord-webhook.py`: send images to Discord with Webhook
  - You should provide your webhook URL with the environment variable, `DISCORD_WEBHOOK_URL`.
  - You should place your image in the working directory with the name, `image.jpg`.
