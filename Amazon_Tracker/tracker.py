import requests
from bs4 import BeautifulSoup
import smtplib

# This is Amazon Price Tracker Using WebScrapper


def send_mail(): # THis functions lets User send the Mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your email id', 'password') # Here is the Address and password of the sender
    subject = f"Price fell down for {title}"
    body = f"Check this link {URL}"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'hetandnap321@gmail.com',
        Email_id,
        msg
    )
    print("Email Succesfully sent")
    server.quit()

# The Below Block of the Code Determines the URL and Scraps the Object


print("Welcome to The Amazon Tracker")
URL = input("Enter the URl of the Product on Amazon:")
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = price[5:10]
converted_price = converted_price.replace(',', '')
prize_want = input("Enter the Price You neeed")
Email_id = input("Enter the Email ID ")

if float(converted_price) < int(prize_want): # This is Simple Condition to send the Mail
    send_mail()



