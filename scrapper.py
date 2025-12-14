import time
import csv
import os
import re
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# ============================================================
#                       CONFIGURATION
# ============================================================

OUTPUT = "gurgaon_maps_scraped_click.csv"

# Create CSV with header
if not os.path.exists(OUTPUT):
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["SearchQuery", "Name", "Address", "Phone", "Email", "Website", "Rating", "MapsLink"])


QUERIES = [
    "PG",
    "Boys PG",
    "Girls PG",
    "Co-living",
    "Hostel",
    "Student accommodation",
    "Guest house",
    "Hotel",
    "Service apartment",
    "Paying guest",
]


ADDRESS_LIST = [

# --- SECTORS 1 to 115 ---
"Sector 1 Gurgaon","Sector 1 Gurugram",
"Sector 2 Gurgaon","Sector 2 Gurugram",
"Sector 3 Gurgaon","Sector 3 Gurugram",
"Sector 4 Gurgaon","Sector 4 Gurugram",
"Sector 5 Gurgaon","Sector 5 Gurugram",
"Sector 6 Gurgaon","Sector 6 Gurugram",
"Sector 7 Gurgaon","Sector 7 Gurugram",
"Sector 8 Gurgaon","Sector 8 Gurugram",
"Sector 9 Gurgaon","Sector 9 Gurugram",
"Sector 9A Gurgaon","Sector 9A Gurugram",
"Sector 10 Gurgaon","Sector 10 Gurugram",
"Sector 10A Gurgaon","Sector 10A Gurugram",
"Sector 11 Gurgaon","Sector 11 Gurugram",
"Sector 12 Gurgaon","Sector 12 Gurugram",
"Sector 12A Gurgaon","Sector 12A Gurugram",
"Sector 13 Gurgaon","Sector 13 Gurugram",
"Sector 14 Gurgaon","Sector 14 Gurugram",
"Sector 15 Gurgaon","Sector 15 Gurugram",
"Sector 15 Part 1 Gurgaon","Sector 15 Part 1 Gurugram",
"Sector 15 Part 2 Gurgaon","Sector 15 Part 2 Gurugram",
"Sector 16 Gurgaon","Sector 16 Gurugram",
"Sector 16A Gurgaon","Sector 16A Gurugram",
"Sector 17 Gurgaon","Sector 17 Gurugram",
"Sector 18 Gurgaon","Sector 18 Gurugram",
"Sector 19 Gurgaon","Sector 19 Gurugram",
"Sector 20 Gurgaon","Sector 20 Gurugram",
"Sector 21 Gurgaon","Sector 21 Gurugram",
"Sector 22 Gurgaon","Sector 22 Gurugram",
"Sector 23 Gurgaon","Sector 23 Gurugram",
"Sector 23A Gurgaon","Sector 23A Gurugram",
"Sector 24 Gurgaon","Sector 24 Gurugram",
"Sector 25 Gurgaon","Sector 25 Gurugram",
"Sector 26 Gurgaon","Sector 26 Gurugram",
"Sector 27 Gurgaon","Sector 27 Gurugram",
"Sector 28 Gurgaon","Sector 28 Gurugram",
"Sector 29 Gurgaon","Sector 29 Gurugram",
"Sector 30 Gurgaon","Sector 30 Gurugram",
"Sector 31 Gurgaon","Sector 31 Gurugram",
"Sector 32 Gurgaon","Sector 32 Gurugram",
"Sector 33 Gurgaon","Sector 33 Gurugram",
"Sector 34 Gurgaon","Sector 34 Gurugram",
"Sector 35 Gurgaon","Sector 35 Gurugram",
"Sector 36 Gurgaon","Sector 36 Gurugram",
"Sector 37 Gurgaon","Sector 37 Gurugram",
"Sector 37C Gurgaon","Sector 37C Gurugram",
"Sector 38 Gurgaon","Sector 38 Gurugram",
"Sector 39 Gurgaon","Sector 39 Gurugram",
"Sector 40 Gurgaon","Sector 40 Gurugram",
"Sector 41 Gurgaon","Sector 41 Gurugram",
"Sector 42 Gurgaon","Sector 42 Gurugram",
"Sector 43 Gurgaon","Sector 43 Gurugram",
"Sector 44 Gurgaon","Sector 44 Gurugram",
"Sector 45 Gurgaon","Sector 45 Gurugram",
"Sector 46 Gurgaon","Sector 46 Gurugram",
"Sector 47 Gurgaon","Sector 47 Gurugram",
"Sector 48 Gurgaon","Sector 48 Gurugram",
"Sector 49 Gurgaon","Sector 49 Gurugram",
"Sector 50 Gurgaon","Sector 50 Gurugram",
"Sector 51 Gurgaon","Sector 51 Gurugram",
"Sector 52 Gurgaon","Sector 52 Gurugram",
"Sector 52A Gurgaon","Sector 52A Gurugram",
"Sector 53 Gurgaon","Sector 53 Gurugram",
"Sector 54 Gurgaon","Sector 54 Gurugram",
"Sector 55 Gurgaon","Sector 55 Gurugram",
"Sector 56 Gurgaon","Sector 56 Gurugram",
"Sector 57 Gurgaon","Sector 57 Gurugram",
"Sector 58 Gurgaon","Sector 58 Gurugram",
"Sector 59 Gurgaon","Sector 59 Gurugram",
"Sector 60 Gurgaon","Sector 60 Gurugram",
"Sector 61 Gurgaon","Sector 61 Gurugram",
"Sector 62 Gurgaon","Sector 62 Gurugram",
"Sector 63 Gurgaon","Sector 63 Gurugram",
"Sector 63A Gurgaon","Sector 63A Gurugram",
"Sector 64 Gurgaon","Sector 64 Gurugram",
"Sector 65 Gurgaon","Sector 65 Gurugram",
"Sector 66 Gurgaon","Sector 66 Gurugram",
"Sector 66A Gurgaon","Sector 66A Gurugram",
"Sector 67 Gurgaon","Sector 67 Gurugram",
"Sector 68 Gurgaon","Sector 68 Gurugram",
"Sector 69 Gurgaon","Sector 69 Gurugram",
"Sector 70 Gurgaon","Sector 70 Gurugram",
"Sector 70A Gurgaon","Sector 70A Gurugram",
"Sector 71 Gurgaon","Sector 71 Gurugram",
"Sector 72 Gurgaon","Sector 72 Gurugram",
"Sector 73 Gurgaon","Sector 73 Gurugram",
"Sector 74 Gurgaon","Sector 74 Gurugram",
"Sector 75 Gurgaon","Sector 75 Gurugram",
"Sector 76 Gurgaon","Sector 76 Gurugram",
"Sector 77 Gurgaon","Sector 77 Gurugram",
"Sector 78 Gurgaon","Sector 78 Gurugram",
"Sector 79 Gurgaon","Sector 79 Gurugram",
"Sector 80 Gurgaon","Sector 80 Gurugram",
"Sector 81 Gurgaon","Sector 81 Gurugram",
"Sector 82 Gurgaon","Sector 82 Gurugram",
"Sector 82A Gurgaon","Sector 82A Gurugram",
"Sector 83 Gurgaon","Sector 83 Gurugram",
"Sector 84 Gurgaon","Sector 84 Gurugram",
"Sector 85 Gurgaon","Sector 85 Gurugram",
"Sector 86 Gurgaon","Sector 86 Gurugram",
"Sector 87 Gurgaon","Sector 87 Gurugram",
"Sector 88 Gurgaon","Sector 88 Gurugram",
"Sector 89 Gurgaon","Sector 89 Gurugram",
"Sector 89A Gurgaon","Sector 89A Gurugram",
"Sector 90 Gurgaon","Sector 90 Gurugram",
"Sector 91 Gurgaon","Sector 91 Gurugram",
"Sector 92 Gurgaon","Sector 92 Gurugram",
"Sector 93 Gurgaon","Sector 93 Gurugram",
"Sector 94 Gurgaon","Sector 94 Gurugram",
"Sector 95 Gurgaon","Sector 95 Gurugram",
"Sector 95A Gurgaon","Sector 95A Gurugram",
"Sector 96 Gurgaon","Sector 96 Gurugram",
"Sector 97 Gurgaon","Sector 97 Gurugram",
"Sector 98 Gurgaon","Sector 98 Gurugram",
"Sector 99 Gurgaon","Sector 99 Gurugram",
"Sector 99A Gurgaon","Sector 99A Gurugram",
"Sector 100 Gurgaon","Sector 100 Gurugram",
"Sector 101 Gurgaon","Sector 101 Gurugram",
"Sector 102 Gurgaon","Sector 102 Gurugram",
"Sector 102A Gurgaon","Sector 102A Gurugram",
"Sector 103 Gurgaon","Sector 103 Gurugram",
"Sector 104 Gurgaon","Sector 104 Gurugram",
"Sector 105 Gurgaon","Sector 105 Gurugram",
"Sector 106 Gurgaon","Sector 106 Gurugram",
"Sector 107 Gurgaon","Sector 107 Gurugram",
"Sector 108 Gurgaon","Sector 108 Gurugram",
"Sector 109 Gurgaon","Sector 109 Gurugram",
"Sector 110 Gurgaon","Sector 110 Gurugram",
"Sector 110A Gurgaon","Sector 110A Gurugram",
"Sector 111 Gurgaon","Sector 111 Gurugram",
"Sector 112 Gurgaon","Sector 112 Gurugram",
"Sector 113 Gurgaon","Sector 113 Gurugram",
"Sector 114 Gurgaon","Sector 114 Gurugram",
"Sector 115 Gurgaon","Sector 115 Gurugram",

# --- PREMIUM LOCALITIES ---
"DLF Phase 1 Gurgaon","DLF Phase 1 Gurugram",
"DLF Phase 2 Gurgaon","DLF Phase 2 Gurugram",
"DLF Phase 3 Gurgaon","DLF Phase 3 Gurugram",
"DLF Phase 4 Gurgaon","DLF Phase 4 Gurugram",
"DLF Phase 5 Gurgaon","DLF Phase 5 Gurugram",
"Galleria Market Gurgaon","Galleria Market Gurugram",
"Ardee City Gurgaon",
"South City 1 Gurgaon","South City 1 Gurugram",
"South City 2 Gurgaon","South City 2 Gurugram",
"Sushant Lok Phase 1 Gurgaon",
"Sushant Lok Phase 2 Gurgaon",
"Sushant Lok Phase 3 Gurgaon",
"MG Road Gurgaon","MG Road Gurugram",
"Golf Course Road Gurgaon","Golf Course Road Gurugram",
"Golf Course Extension Road Gurgaon","Golf Course Extension Road Gurugram",
"Udyog Vihar Phase 1 Gurgaon","Udyog Vihar 1 Gurugram",
"Udyog Vihar Phase 2 Gurgaon","Udyog Vihar 2 Gurugram",
"Udyog Vihar Phase 3 Gurgaon","Udyog Vihar 3 Gurugram",
"Udyog Vihar Phase 4 Gurgaon","Udyog Vihar 4 Gurugram",
"Udyog Vihar Phase 5 Gurgaon","Udyog Vihar 5 Gurugram",
"Cyber Hub Gurgaon","Cyber Hub Gurugram",
"Cyber City Gurgaon","Cyber City Gurugram",
"Ambience Mall Gurgaon","Ambience Mall Gurugram",
"Sikanderpur Gurgaon","Sikanderpur Gurugram",
"IFFCO Chowk Gurgaon","IFFCO Chowk Gurugram",
"Rajiv Chowk Gurgaon",
"Hero Honda Chowk Gurgaon",
"Sahara Mall Gurgaon",
"Badshahpur Gurgaon","Badshahpur Gurugram",
"Palam Vihar Gurgaon","Palam Vihar Gurugram",
"Malibu Town Gurgaon","Malibu Town Gurugram",
"Mayfield Garden Gurgaon","Mayfield Garden Gurugram",
"Nirvana Country Gurgaon",
"Greenwood City Gurgaon",
"Rosewood City Gurgaon",

# --- VILLAGES ---
"Nathupur Village Gurgaon","Nathupur Village Gurugram",
"Dundahera Village Gurgaon","Dundahera Village Gurugram",
"Jharsa Village Gurgaon","Jharsa Village Gurugram",
"Chakkarpur Village Gurgaon","Chakkarpur Village Gurugram",
"Wazirabad Village Gurgaon","Wazirabad Village Gurugram",
"Ghata Village Gurgaon","Ghata Village Gurugram",
"Tigra Villag Gurugram",
"Kanhai Village Gurgaon","Kanhai Village Gurugram",
"Sihi Village Gurugram",
"Dhankot Gurugram",
"Kankrola Gurugram",
"Fazilpur Gurugram",
"Daulatabad Gurugram",
"Narsinghpur Gurugram",
"Garhi Harsaru Gurugram",
"Kadarpur Gurugram",
"Behrampur Gurgaon",
"Badshahpur Village Gurugram",
]


# ============================================================
#                     SELENIUM DRIVER
# ============================================================

def get_driver():
    chrome_options = Options()

    # Visible browser (recommended)
    # chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver


# ============================================================
#                SCRAPE EMAIL FROM WEBSITE
# ============================================================

def extract_email(url):
    if not url:
        return ""

    url = url.rstrip("/")
    paths = ["", "/contact", "/contact-us", "/about", "/support", "/help"]

    headers = {"User-Agent": "Mozilla/5.0"}

    for p in paths:
        try:
            r = requests.get(url + p, timeout=7, headers=headers)
            if r.status_code != 200:
                continue

            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", r.text)
            emails = [
                e for e in emails
                if not any(x in e.lower() for x in
                           ["google", "oyo", "booking", "tripadvisor", "makemytrip"])
            ]

            if emails:
                return emails[0]

        except:
            continue

    return ""


# ============================================================
#             CLICK-BASED GOOGLE MAPS SCRAPING
# ============================================================

def scrape_query(full_query):

    print(f"\n🔍 Searching: {full_query}")

    driver = get_driver()
    driver.get("https://www.google.com/maps/search/" + full_query)
    time.sleep(5)

    # Scroll list
    try:
        scroll_box = driver.find_element(By.XPATH, "//div[@role='feed']")
    except:
        print("❌ No results list found")
        driver.quit()
        return

    for _ in range(12):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
        time.sleep(1.4)

    # Get card list
    cards = driver.find_elements(By.XPATH, "//div[contains(@class,'Nv2PK')]")
    print(f"📌 Cards found: {len(cards)}")

    for i in range(len(cards)):
        try:
            cards = driver.find_elements(By.XPATH, "//div[contains(@class,'Nv2PK')]")
            card = cards[i]

            driver.execute_script("arguments[0].scrollIntoView(true);", card)
            time.sleep(0.7)
            card.click()
            time.sleep(2.5)

            # -----------------------------------
            # Extract: NAME
            # -----------------------------------
            try:
                name = driver.find_element(By.CSS_SELECTOR, "h1.DUwDvf").text
            except:
                name = ""

            # -----------------------------------
            # Extract: ADDRESS
            # -----------------------------------
            try:
                address = driver.find_element(By.XPATH, "//button[@data-item-id='address']").text
            except:
                address = ""

            # -----------------------------------
            # Extract: PHONE (5 methods)
            # -----------------------------------
            phone = ""

            # Try 1: Classic phone button
            try:
                phone = driver.find_element(By.XPATH, "//button[@data-item-id='phone']").text
            except:
                pass

            # Try 2: New phone span
            if not phone:
                try:
                    phone = driver.find_element(By.XPATH, "//div[@data-item-id='phone']//span").text
                except:
                    pass

            # Try 3: Icon button
            if not phone:
                try:
                    phone = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Phone')]").text
                except:
                    pass

            # Try 4: Any visible +91 or 10-digit number
            if not phone:
                try:
                    blocks = driver.find_elements(By.XPATH, "//div[contains(@class,'Io6YTe')]")
                    for b in blocks:
                        txt = b.text.strip()
                        if "+91" in txt or (txt.replace(" ", "").isdigit() and len(txt.replace(" ", "")) >= 10):
                            phone = txt
                            break
                except:
                    pass

            # Try 5: Regex in page source
            if not phone:
                html = driver.page_source
                m1 = re.findall(r"\+91[-\s]?\d{5}[-\s]?\d{5}", html)
                m2 = re.findall(r"\d{10}", html)
                phone = m1[0] if m1 else (m2[0] if m2 else "")

            # -----------------------------------
            # Extract: WEBSITE
            # -----------------------------------
            try:
                website = driver.find_element(By.XPATH, "//a[@data-item-id='authority']").get_attribute("href")
            except:
                website = ""

            # -----------------------------------
            # Extract: RATING
            # -----------------------------------
            try:
                rating = driver.find_element(By.CSS_SELECTOR, "div.F7nice > span").text
            except:
                rating = ""

            # -----------------------------------
            # Maps Link (current URL)
            # -----------------------------------
            maps_link = driver.current_url

            # -----------------------------------
            # EMAIL
            # -----------------------------------
            email = extract_email(website) if website else ""

            # Skip if no contact info
            if not phone and not email:
                continue

            # -----------------------------------
            # SAVE RESULTS
            # -----------------------------------
            row = [full_query, name, address, phone, email, website, rating, maps_link]

            with open(OUTPUT, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(row)

            print(f"✔ Saved: {name} | {phone or email}")

        except Exception as e:
            print(f"⚠ Error: {e}")
            continue

    driver.quit()


# ============================================================
#                       MAIN LOOP
# ============================================================

def main():

    for address in ADDRESS_LIST:
        print(f"\n🏙 Location → {address}")

        for q in QUERIES:
            full_query = f"{q} in {address}"

            try:
                scrape_query(full_query)
            except Exception as e:
                print("❌ Error on:", full_query, e)

    print("\n🎉 DONE — All results saved:", OUTPUT)


if __name__ == "__main__":
    main()
