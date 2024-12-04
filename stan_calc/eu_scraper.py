from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_euro_to_dinar():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        url = 'https://www.google.com/search?q=euro+to+dinar'
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        span = soup.find('span', class_='DFlfde SwHCTb')
        if span:
            return span.get_text()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
    return None
