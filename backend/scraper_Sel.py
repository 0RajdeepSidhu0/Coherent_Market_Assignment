import time
import pandas as pd
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# create data folder
os.makedirs("data", exist_ok=True)

def setup_driver():
    options = Options()
    options.add_argument("--headless")  # run without opening browser
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_yc():
    driver = setup_driver()
    driver.get("https://www.ycombinator.com/companies")

    time.sleep(5)

    # scroll to load more startups
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    companies = driver.find_elements(By.CSS_SELECTOR, "a[href^='/companies/']")

    data = []

    for c in companies:
        try:
            name = c.text.split("\n")[0]
            link = "https://www.ycombinator.com" + c.get_attribute("href")

            data.append({
                "name": name,
                "link": link
            })

        except:
            continue

    driver.quit()
    return data

def main():
    print("Scraping YC startups...")
    data = scrape_yc()

    df = pd.DataFrame(data).drop_duplicates()
    df.to_csv("data/startups_raw.csv", index=False)

    print(f"Saved {len(df)} startups!")

if __name__ == "__main__":
    main()