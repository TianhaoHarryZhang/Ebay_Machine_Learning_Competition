#Code used to collect some online Ebay brand data

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import re

# Setup chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Navigate to the url
driver.get('https://www.ebay.com/b/Mens-Accessories/4250/bn_1642245')

# Get the element
elements = driver.find_elements(By.CLASS_NAME, "brm__item-label")

Brand = []

for element in elements:

    html_code = element.get_attribute("outerHTML")
    delimiter = "PPP"
    assert delimiter not in html_code
    html_code = html_code.replace("<",delimiter)
    html_code = html_code.replace(">",delimiter)

    Brand.append(html_code.split(delimiter)[-3])


print(Brand)

# Close the driver
driver.quit()
