import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Apple-MacBook-13-inch' \
      '-Storage-Keyboard/dp/B0882DZPGK/ref=sr_1_1_sspa?crid=2069F24Y2HZE3&dchild=1&keywords=macbook+pro' \
      '&qid=1615326796&sprefix=macboo%2Caps%2C224&sr=8-1-spo' \
      'ns&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT1kyTFBES04yRjRVJmVuY3J5cHRlZElkPUEwMTY3N' \
      'zA0M0JFNFMwMFlZUDBMQyZlbmNyeXB0ZWRBZElkPU' \
      'EwMzY1ODMwMkpTU1BBOVFZRzlLNiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36(KHTML, "
                         "like Gecko) Chrome/88.0.4324.192 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6].replace(",", '.'))

    if converted_price == 1799.0:
        send_mail()

    print(converted_price)
    print(title.strip())

    if converted_price > 1899:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('justingrant373@gmail.com', 'Cameronjonas2')

    subject = 'Price Fell down!'
    body = 'Check the amazon link https://www.amazon.co.uk/Apple-MacBook-13-inch' \
           '-Storage-Keyboard/dp/B0882DZPGK/ref=sr_1_1_sspa?crid=2069F24Y2HZE3&dchild=1&keywords=macbook+pro' \
           '&qid=1615326796&sprefix=macboo%2Caps%2C224&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdG' \
           'VkUXVhbGlmaWVyPUExT1kyTFBES04yRjRVJmVuY3J5cHRlZElkPUEwMTY3NzA0M0JFNFMwMFlZUDBMQyZlbmNyeXB0ZWRBZElkPU' \
           'EwMzY1ODMwMkpTU1BBOVFZRzlLNiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZW' \
           'RpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'justingrant373@gmail.com',
        'joannehealey2@gmail.com',
        msg
    )
    print("The email has been sent")
    server.quit()


while True:
    check_price()
    time.sleep(60 * 60)
