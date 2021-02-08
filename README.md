# line_notify_tokyometro_lambda

東京メトロの運行情報をLINE Notifyで通知する

- AWS Lambda で定期実行するように対応　（JST:6時～22時の間、毎時00分と30分に実行）
- トリガーは、EventBridge (CloudWatch Events)で設定
- ログは、Amazon SNS により、Cloud Trail Logs へ送信

　

![notify_metro_problem.PNG](https://github.com/whitecat-22/line_notify_tokyometro_lambda/blob/main/notify_metro_problem.PNG "notify_metro_problem.PNG")
