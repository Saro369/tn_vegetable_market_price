from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pandas as pd
import time
import logging
import openpyxl
import sys
sys.path.insert(0, '././')
from config import OUTPUT_PATH, DIST, BASE_URL, START_DATE, END_DATE

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def set_up_browser():
    """Set up the Selenium browser."""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=chrome_options)

def fetch_page_content(browser, url):
    """Fetch the webpage content."""
    try:
        browser.get(url)
        time.sleep(5)  # Wait for the page to load
        return browser.page_source
    except Exception as e:
        logger.error(f"An error occurred while fetching the page content: {str(e)}")
        return None

def extract_table_data(html_content):
    """Extract the table data from HTML content."""
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.find("table")
    except Exception as e:
        logger.error(f"An error occurred while extracting table data: {str(e)}")
        return None

def parse_table_data(table):
    """Parse the table data."""
    try:
        headers = [header.text.strip() for header in table.find_all("th")]
        rows = table.find_all("tr")[1:]  # Skip the header row

        data = []
        for row in rows:
            cells = row.find_all("td")
            row_data = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
            data.append(row_data)
        
        return headers, data
    except Exception as e:
        logger.error(f"An error occurred while parsing table data: {str(e)}")
        return None, []

def main():
    """Main function to extract vegetable price data."""
    base_url = f"{BASE_URL}/{DIST}/today"
    current_date = START_DATE

    # Initialize
    columns = []
    data_df = pd.DataFrame(columns=columns)
    browser = set_up_browser()
    
    # Record the start time
    start_time = time.time()

    # Iterate over dates
    while current_date <= END_DATE:
        url = f"{base_url}?date={current_date.strftime('%Y-%m-%d')}"
        html_content = fetch_page_content(browser, url)

        if html_content:
            table = extract_table_data(html_content)

            if table is not None:
                headers, data = parse_table_data(table)
                if headers is not None and data:
                    if not columns:
                        columns = headers
                        data_df = pd.DataFrame(columns=columns)
                    for row in data:
                        row['Date'] = pd.to_datetime(current_date)  # Convert date to pandas datetime format
                    current_date_df = pd.DataFrame(data)
                    data_df = pd.concat([data_df, current_date_df], ignore_index=True)

        # Log progress
        logger.info(f'Fetched data for date: {current_date}')
        current_date += timedelta(days=1)

    # Cleanup
    browser.quit()
    data_df.to_excel(f'{OUTPUT_PATH}/{DIST}_vegetable_market_history_{START_DATE}.xlsx', index=False)
    print(data_df)
    
    # Calculate and print the execution time
    execution_time = time.time() - start_time
    logger.info(f'Execution time: {execution_time} seconds')

if __name__ == "__main__":
    main()