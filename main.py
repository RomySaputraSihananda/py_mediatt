import requests as rq;
from bs4 import BeautifulSoup;

url = "https://www.tiktok.com/@freyajkt48/video/7305074556123761926";


headers = {
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent":
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
}

body =  f"id={url}&locale=en&tt=SGlSc1Q_";

req = rq.post("https://ssstik.io/abc?url=dl", data=body, headers=headers);

soup = BeautifulSoup(req.text, 'html.parser');

print(soup.find(".pure-button.pure-button-primary.is-center.u-bl.dl-button.download_link.without_watermark.vignette_active.notranslate").attrs['href']);