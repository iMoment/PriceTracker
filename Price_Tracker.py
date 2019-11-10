import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-MacBook-15-inch-512GB-Storage/dp/B07S58MHXF/ref=sr_1_1?keywords=New+Apple+MacBook+' \
      'Pro+%2815-inch%2C+16GB+RAM%2C+512GB+Storage%29+-+Space+Gray&qid=1573416231&sr=8-1'

header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                        'Version/13.0.3 Safari/605.1.15'}

def check_price():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_title = soup.find(id='productTitle').getText().strip()
    product_price = soup.find(id='priceblock_ourprice').getText()

    adjusted_price = product_price.replace(",", "")
    converted_price = float(adjusted_price[1:10])

    if (converted_price > 2499.98):
        send_email()

        print("Product title is: " + product_title)
        print("Product price is: " + str(converted_price))

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('imoment.developer@gmail.com', 'hkcgkvwwyzsrhddc')

    subject = 'STANLEY, THE  MACBOOK PRO PRICE FALL DOWN SOMETHING'
    body = 'Check this link fucker: https://www.amazon.com/Apple-MacBook-15-inch-512GB-Storage/dp/' \
           'B07S58MHXF/ref=sr_1_1?keywords=New+Apple+MacBook+Pro+%2815-inch%2C+16GB+RAM%2C+512GB+Sto' \
           'rage%29+-+Space+Gray&qid=1573416231&sr=8-1'

    message = "Subject: " + subject + "\n\n" + body

    server.sendmail(
        'imoment.developer@gmail.com',
        'imoment.developer@gmail.com',
        message
    )
    print('Email has been sent.')

    server.quit()

check_price()















