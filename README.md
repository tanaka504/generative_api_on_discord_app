# Discordでいろんな生成AIを試すやつ

## 動かし方
1. 以下の環境変数を設定する
DISCORD_APP_TOKEN
DEEPL_API_KEY

2. 

## 構造
discord_app:
  discord bot 用のサーバー
  /img コマンドでdiffusion APIを叩く
  それ以外は rwkvの応答
  ユーザー制限かける

diffusion_app:
  stable diffusion用のサーバー
  画像生成してくれるAPI
  VRAMに乗らないようであればどちらか削る

chat_app:
  応答生成用のサーバー
  RWKVモデルで生成
  スタイル制御してもいいかも
  VRAMに乗らないようであればどちらか
