from django.core.mail import send_mail
from selenium import webdriver
import logging
import time
from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("https://www.google.com/intl/en-GB/gmail/about/")
signinButton_link = driver.find_element_by_xpath("//ul[@class='h-c-header__cta-list header__nav--ltr']/li[2]/a").get_attribute("href");
driver.get(signinButton_link)
driver.implicitly_wait(60)
# signinButton.click()
elem=driver.find_element_by_id("identifierId")
elem.send_keys("sahuvitanshu76@gmail.com")
signinButton=driver.find_element_by_id("identifierNext")
signinButton.click()
driver.implicitly_wait(60)
send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)