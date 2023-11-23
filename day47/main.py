from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
email = "zgetnet24@gmail.com"
passowrd = "zelalem1249"

link = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(class="a-offscreen").get_text().strip()
title = soup.find(id="producttitle").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
# if price < 100:
with smtplib.SMTP(@gmail.com, port= 587) as l:
    l.starttls()
    result = l.login(email, passowrd)
    l.sendmail(
        from_addr= "zgetnet24@gmail.com"
        to_addr=email,
        message=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
)


