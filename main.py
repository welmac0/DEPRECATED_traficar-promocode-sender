import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import os
from twilio.rest import Client
from datetime import date
import re

PATTERN = r"[‘'\"]([A-Z]+)[‘'\"]"
DATE_PATTERN = r"\((\d{2}\.\d{2})\)"
TIME_PATTERN = r"\d{2}:\d{2}"
URL = "https://www.instagram.com/traficar_pl/?hl=en"
MYPHONENUMBER = os.getenv("MYPHONENUMBER")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
PHONENUMBER = os.getenv("PHONENUMBER")
TWILIO_SID = os.getenv("TWILIO_SID")
TODAY = date.today()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

### Heroku chrome config ###
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")


def check_validity(post_date):
    today_dm_raw = str(TODAY).split("-")
    today_dm = list(reversed(today_dm_raw[1:]))
    post_dm = post_date.strip("(").strip(")").split(".")

    if today_dm[0] > post_dm[0]:
        return False

    return True


def get_data():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    driver.implicitly_wait(4)
    driver.find_element(By.CLASS_NAME, "_a9_0").click()
    parent_photos = driver.find_element(By.CLASS_NAME, "_aagv img")
    description = parent_photos.get_attribute("alt")

    code_raw = re.search(pattern=PATTERN, string=description)
    code = code_raw.group()

    found_date_raw = re.search(pattern=DATE_PATTERN, string=description)
    found_date = found_date_raw.group()

    found_time_raw = re.search(pattern=TIME_PATTERN, string=description)
    found_time = found_time_raw.group()

    driver.quit()

    if check_validity(found_date):
        send_message(code, found_date, found_time)


def send_message(code, found_date, found_time):
    message = f"🚗\nNowy kod Traficar: {code}.\nWażny do: {found_date}, do godziny {found_time}"

    account_sid = TWILIO_SID
    auth_token = TWILIO_AUTH

    client = Client(account_sid, auth_token)
    my_message = client.messages.create(
        from_=PHONENUMBER,
        body=message,
        to=MYPHONENUMBER
    )

    return my_message.status


if __name__ == "__main__":
    get_data()
