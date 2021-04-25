# Importing the required modules for Selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# By using time module we are going to increase the on screen time
import time

# Setting your chromedriver path
chrome_path = "/Users/Cassa/chromedriver"

# Intialising the chrome driver
driver = webdriver.Chrome(executable_path=chrome_path)

# Get the precise required url of the job search you are going to apply
URL = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India'

# Getting the url
driver.get(URL)

time.sleep(3)

# Automating the Sign in button
sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()

time.sleep(3)

# Input the username automation
username = driver.find_element_by_name('session_key')
username.send_keys('your_email_id@example.com')

time.sleep(3)

# Input the password automation
password = driver.find_element_by_name('session_password')
password.send_keys('your_password')

time.sleep(2)

# Enter to proceed
password.send_keys(Keys.ENTER)

time.sleep(3)

# Remember me login automation
remember_me = driver.find_element_by_css_selector('#remember-me-prompt__form-primary button')
remember_me.click()

time.sleep(6)

# Getting the first result of your job search url query
job_search_result = driver.find_element_by_css_selector('.jobs-search-results ul li')
job_search_result.click()

time.sleep(3)

# Automating the easy apply button
easy_apply = driver.find_element_by_css_selector('.jobs-apply-button--top-card button')
easy_apply.click()

# At this point Linkedin automatically fills email and phone which you used while creating account

time.sleep(2)

# Automating the click next button
next = driver.find_element_by_css_selector('.display-flex button')
next.click()

time.sleep(3)

# Automating the click next button
next = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]')
next.click()

# Further the additonal questions that might be asked can be entered manually as they are dynamic company to company
