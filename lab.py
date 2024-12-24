from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Sayt URL-si
url = "https://sap.aztu.edu.az/studies/lecture_attend.php?lec_open_idx=60466&lecture_code=4138&sem_code=20242"

# Giriş məlumatları
username = "randomaztustudent"
password = "randomaztustudent+"

# WebDriver yeri (Edge WebDriver-in tam yolu)
webdriver_path = "path/to/msedgedriver"  # Edge WebDriver-in tam yolunu yazın

# WebDriver xidmətini başlatmaq
service = Service(webdriver_path)
driver = webdriver.Edge(service=service)

try:
    # Saytı açmaq
    driver.get(url)

    # Giriş məlumatlarını daxil etmək
    username_field = driver.find_element(By.NAME, "username")  # 1-ci xana üçün element
    password_field = driver.find_element(By.NAME, "password")  # 2-ci xana üçün element

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Giriş düyməsini klikləmək
    password_field.send_keys(Keys.RETURN)

    # Səhifənin yüklənməsini gözləmək
    time.sleep(5)

    # Davamiyyət faizini tapmaq
    attendance_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Davamiyyət')]/following-sibling::td")
    attendance_percentage = attendance_element.text

    print(f"Davamiyyət faizi: {attendance_percentage}")

finally:
    # Brauzeri bağlamaq
    driver.quit()
