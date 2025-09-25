from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Firefox()
driver.get("https://authorized-partner.netlify.app/login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

 # Click on Sign up link
signup= wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign Up']")))
driver.execute_script("arguments[0].click()", signup)
time.sleep(3)

# Click on "I agree to terms of service and policy" checkbox
agree_terms = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remember']")))
driver.execute_script("arguments[0].click()", agree_terms)

continue_button= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
driver.execute_script("arguments[0].click()", continue_button)

#  Fill Signup Form
first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
first_name.send_keys("new ")

last_name = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
last_name.send_keys("sen")

email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
email.send_keys("jsen2250@gmail.com")

phone = wait.until(EC.presence_of_element_located((By.NAME, "phoneNumber")))
phone.send_keys("9815684325")

password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("Test@126")

confirm_password = wait.until(EC.presence_of_element_located((By.NAME, "confirmPassword")))
confirm_password.send_keys("Test@126")

next_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next']")))
driver.execute_script("arguments[0].click()", next_button)

# Wait for the OTP input field
time.sleep(3)
otp_input = wait.until(EC.presence_of_element_located( (By.XPATH, "//input[@data-input-otp='true']")))
driver.execute_script("arguments[0].scrollIntoView(true);", otp_input)
otp_input.click()
# Send the 6-digit OTP
otp_code = input("Enter the 6-digit OTP received in your email: ")
otp_input.send_keys(otp_code)

# Click Next / Verify button
verify = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Verify Code']")))
driver.execute_script("arguments[0].click()", verify)
time.sleep(5)

#  Fill Agency Details
agency_name=wait.until(EC.presence_of_element_located((By.NAME, "agency_name")))
agency_name.send_keys("Test Agency")

Role=driver.find_element(By.NAME, "role_in_agency")
Role.send_keys("Manager")

agency_email=driver.find_element(By.NAME, "agency_email")
agency_email.send_keys("testagency@example.com")

website=driver.find_element(By.NAME, "agency_website")
website.send_keys("https://www.testagency.com")

address=driver.find_element(By.NAME, "agency_address")
address.send_keys("Kathmandu, Nepal")

country_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']")))
driver.execute_script("arguments[0].click();", country_dropdown)

nepal_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Nepal')]")))
driver.execute_script("arguments[0].click();", nepal_option)

next_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next']")))
driver.execute_script("arguments[0].click()", next_button)

# Professional Experience
year_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']")))
driver.execute_script("arguments[0].click();", year_dropdown)

one_year_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='1 year']")))
driver.execute_script("arguments[0].click();", one_year_option)

students_input = wait.until(EC.presence_of_element_located((By.NAME, "number_of_students_recruited_annually")))
students_input.send_keys("50")


focus_area_input = wait.until(EC.presence_of_element_located((By.NAME, "focus_area")))
focus_area_input.send_keys("Undergraduate admissions to uk")

# Fill "Success Metrics"
success_metrics= wait.until(EC.presence_of_element_located((By.NAME, "success_metrics")))
success_metrics.send_keys("90")

# Click the final checkbox
admission = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @id='«r8c»-form-item']")))
driver.execute_script("arguments[0].click();", admission)

next_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Next']")))
driver.execute_script("arguments[0].click()", next_button)

# Fill  Verification and Preferences
registration_input = wait.until(EC.presence_of_element_located((By.NAME, "business_registration_number")))
registration_input.send_keys("1234567890")

countries_dropdown = wait.until(EC.element_to_be_clickable( (By.ID, "«rdq»-form-item")))
driver.execute_script("arguments[0].click();", countries_dropdown)

United_Kingdom = wait.until(EC.element_to_be_clickable( (By.XPATH, "//div[text()='United Kingdom']")))
driver.execute_script("arguments[0].click();", United_Kingdom)


Universities= wait.until(EC.element_to_be_clickable( (By.ID, "«rdt»-form-item")))
driver.execute_script("arguments[0].click();", Universities)

# Fill "Certification Details"
certification_input = wait.until(EC.presence_of_element_located((By.NAME, "certification_details")))
certification_input.send_keys("ICEF Certified Education Agent")

file_path = os.path.abspath(r"D:\OneDrive\Pictures\Screenshots\Screenshot 2025-09-24 135616.png")

picture_upload = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

picture_upload.send_keys(file_path)




