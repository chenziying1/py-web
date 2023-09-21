# -*- coding: utf-8 -*-
# time:2023/7/28 10:26
# file wayfair2.py
# outhor:czy
# email:1060324818@qq.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv

# 品牌和信息
brands = {
    "DeerValley": {"search_term": "DeerValley", "series_class": "Series", "rating_class": "rPQRE"},
    "TOTO": {"search_term": "TOTO", "series_class": "Series", "rating_class": "hHNoVh"},
    "Swiss Madison": {"search_term": "Swiss Madison", "series_class": "Series", "rating_class": "rPQRE"},
    "American Standard": {"search_term": "American Standard", "series_class": "Series", "rating_class": "rPQRE"},
    "Kohler": {"search_term": "Kohler", "series_class": "Series", "rating_class": "rPQRE"},
    "HOROW": {"search_term": "HOROW", "series_class": "series", "rating_class": "rPQRE"},
    "MOHOME": {"search_term": "MOHOME", "series_class": "Series", "rating_class": "rPQRE"},
    "Fine Fixtures": {"search_term": "Fine Fixtures", "series_class": "Series", "rating_class": "rPQRE"},
    "Woodbridge": {"search_term": "Woodbridge", "series_class": "Series", "rating_class": "rPQRE"}
}
filename = "products.csv"


def get_information(product_url, series_class, rating_class):
    driver.get(product_url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    series = soup.find(class_=series_class).text.strip() if soup.find(class_=series_class) else ""
    rating_value = soup.find(class_=rating_class)["aria-label"].split()[0] if soup.find(class_=rating_class) else ""
    rating_count = soup.find(class_="reviews-count").text.split()[0].replace(",", "") if soup.find(class_="reviews-count") else ""
    weekly_review_count = soup.find(class_="reviews-count").text.split()[-3].replace(",", "") if soup.find(class_="reviews-count") else ""
    return series, rating_value, rating_count, weekly_review_count


# 打开网站
paths = "D:\\egde\\edgedriver_win64 (2)\\msedgedriver.exe"
options = webdriver.EdgeOptions()
options.use_chromium = True  # 使用 Chromium 内核
driver = webdriver.Edge(options=options,executable_path=paths)
driver.get("https://www.wayfair.com")

# 遍历品牌
for brand, info in brands.items():
    search_term = info["search_term"]
    series_class = info["series_class"]
    rating_class = info["rating_class"]

    # 搜索品牌
    search_bar = driver.find_element(By.NAME,"Ntt")
    search_bar.clear()
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)

    # 获取搜索结果
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    products = soup.find_all(class_="ProductCard__cardContainer")

    # 遍历商品
    for product in products:
        sku = product["data-product-id"]
        name = product["data-product-name"]
        price = product.find(class_="ProductCard__price").text.replace("\n", "")
        image_url = product.find(class_="ProductCard__image").img["src"]
        product_url = "https://www.wayfair.com" + product.find(class_="ProductCard__link").get("href")
        series, rating, rating_count, weekly_review_count = get_information(product_url, series_class, rating_class)
        with open(filename, 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([sku, name, price, image_url, product_url, series, rating, rating_count, weekly_review_count])

# 关闭网站
driver.quit()

