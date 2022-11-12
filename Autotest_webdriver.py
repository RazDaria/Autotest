import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

s=Service('C:\Test\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open website
driver.get("https://qa.neapro.site/login/")
driver.maximize_window()

# Clear token
driver.execute_script('window.localStorage.clear();')
time.sleep(3)

# Login
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("wisedash90@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

# Open "Passport" form
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()

# Fill in the name
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Разумовская")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Дарья")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Александровна")

# Fill in the date of birth
driver.find_element(By.XPATH, '//*[@id="birthday"]/div/input').click()
driver.find_element(By.CSS_SELECTOR, ".mx-btn-current-year").click()
driver.find_element(By.CSS_SELECTOR, ".mx-icon-double-left").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .cell:nth-child(1) > div").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .cell:nth-child(2) > div").click()
alldates=driver.find_elements(By.CLASS_NAME, "cell")

for date_element in alldates:
    date=date_element.text
    if date=='15':
        date_element.click()
        break

# Fill in the passport data
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("1111")
driver.find_element(By.ID, "passportNumber").click()
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("111111")

driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys("14.04.2022")

driver.find_element(By.CSS_SELECTOR, "#code").clear()
driver.find_element(By.CSS_SELECTOR, "#code").clear()
driver.find_element(By.CSS_SELECTOR, "#code").send_keys("111111")

driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("111-111-111 11")
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("УВД гор. Санкт-Петербурга")

# Fill in the address
address = driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input')
address.send_keys(Keys.CONTROL + "a")
address.send_keys(Keys.DELETE)
address.send_keys('г Москва, ул Абельмановская, д 2А')
address.click()
wait = WebDriverWait(driver, 1)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vue-dadata__suggestions')))
address.send_keys(Keys.ARROW_DOWN)
address.send_keys(Keys.ENTER)

# Fill in the phone
time.sleep(2)
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys(9818888888)

# Upload a document
time.sleep(4)
filePath ='C:\\Users\\user\\PycharmProjects\\Files\\01.jpg'
driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.passport-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]').send_keys(filePath)
time.sleep(8)
driver.find_element(By.XPATH, "//div[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[9]/button[2]").click()


# Open admin's website and log in
driver.get("https://adminqa.neapro.site/login")
admin_page = driver.current_window_handle
print(f'admin_page: {admin_page}')

driver.maximize_window()
driver.find_element(By.ID, "admin_email").send_keys("moderat@neapro.ru")
driver.find_element(By.ID, "admin_password").send_keys("Aa123456")
driver.find_element(By.NAME, "commit").click()

# Open uploaded documents
driver.find_element(By.XPATH, '//*[@id="students"]/a').click()
driver.find_element(By.XPATH, '//*[@id="documents"]/a').click()

# Open SideBar
sidebar = driver.find_element(By.ID, 'sidebar')
driver.execute_script("arguments[0].setAttribute('style', 'right: 0px; position: absolute;')", sidebar)

# Choose user
driver.find_element(By.XPATH, '//*[@id="q_user_id_input"]/span/span[1]/span').click()
sidebar_user = driver.find_element(By.CLASS_NAME, 'select2-search__field')
sidebar_user.send_keys('wisedash90@gmail.com')
time.sleep(1)
sidebar_user.send_keys(Keys.ARROW_DOWN)
sidebar_user.send_keys(Keys.ENTER)
time.sleep(1)

# Filter
driver.find_element(By.XPATH, '//*[@id="new_q"]/div[6]/input[1]').click()
WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, 'index_as_table')))
time.sleep(1)

# Search for the first line with "Ожидание" status and changing it to "Приинят"
elements = driver.find_elements(By.XPATH, '//span[contains(text(),"Ожидание")]')
if elements and elements[0].is_displayed():
    elements[0].click()
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)

# Log out
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="logout"]/a').click()
time.sleep(1)
driver.close()

