# postリクエストをline notify APIに送るためにrequestsのimport
import time
import csv
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import slackweb

# webdriverの設定
option = Options()
option.add_argument('--incognito')
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

info_list = []
with open('config.csv', newline='', encoding='UTF-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    url_list = []
    for row in reader:
        for url in row:
            content = []
            driver.get(url)
            time.sleep(1)

            content0 = driver.find_element_by_xpath('//*[@id="v2_contents"]/div[1]/div/div[2]/div[1]/p')

            content1 = driver.find_element_by_css_selector("#v2_contents > div.v2_contents > div > div.v2_headingH1.v2_headingRoute > h1")

            content2 = driver.find_element_by_css_selector("#v2_contents > div.v2_contents > div > div.v2_gridC.v2_section.v2_clear.v2_stationUnkouMap.v3_stationUnkouMap > div.v2_sectionS.v2_gridCRow > div.v2_unkouReportInfo > div > div > div.v2_unkouReportTxtCaption.v3_unkouReportTxtCaption > p")

            content3 = driver.find_elements_by_css_selector("#v2_contents > div.v2_contents > div > div.v2_gridC.v2_section.v2_clear.v2_stationUnkouMap.v3_stationUnkouMap > div.v2_sectionS.v2_gridCRow > div.v2_unkouReportInfo > div > p")

            # lineに通知したいメッセージを入力
            content.append("●" + content1.text[:-5])
            content.append(content2.text)
            for content3s in content3:
                content.append(content3s.text)

            info_list.append(content)

content_text = []
for i in range(9):
    content_text.append('\n'.join(info_list[i]))

notification_message = (content0.text[:-4])+'\n' + '\n\n'.join(content_text)

driver.quit()

# line：token.txtからトークンの読み込み
with open('token.txt', 'r') as f:
	token = f.read().strip()
# print(token)
# line notify APIのトークンの読み込み
line_notify_token = token
# line notify APIのエンドポイントの設定
line_notify_api = 'https://notify-api.line.me/api/notify'
# ヘッダーの指定
headers = {'Authorization': f'Bearer {line_notify_token}'}
# 送信するデータの指定
data = {'message': f'{notification_message}'}
# line notify apiにpostリクエストを送る
requests.post(line_notify_api, headers=headers, data=data)

"""
slack = slackweb.Slack(url="<Webhook URL>")
slack.notify(text=content_text)
"""
