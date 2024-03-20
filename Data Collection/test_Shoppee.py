from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)     # leaves the browser open even if everything is completed, keeps window open

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

URL = "https://shopee.ph/XH-M609-12-36V-Low-Voltage-Battery-Disconnect-Protection-Module-DC-Output-i.951744141.22229984756?sp_atk=8a7df1e2-125b-4e14-b737-fe472bdcb8f6&xptdk=8a7df1e2-125b-4e14-b737-fe472bdcb8f6&is_from_login=true"
driver.get(URL)


# TEST 01 ------------------------------------------------------------------------------------------------------------ This part here will attempt to bypass Shoppee's login prompt

try:

    # Wait until "Login" text is visible
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "K1dDgL")))
    print("Login page is visible")

    # Find the phone number input field by class name and input the phone number
    phone_number_input = driver.find_element(By.XPATH, "//input[@class='pDzPRp' and @type='text']")
    phone_number_input.send_keys("09455179798")

    # Find the password input field by class name and input the password
    password_input = driver.find_element(By.XPATH, "//input[@class='pDzPRp' and @type='password']")
    password_input.send_keys("your_password_here")

    # Find and click the login button by class name
    """ wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wyhvVD")))
    login_button = driver.find_element(By.CLASS_NAME, "wyhvVD")
    login_button.click() """

    # Get the current URL after redirection     # BAKA DI NA NECESSARY TO?
    """ redirected_url = driver.current_url
    print("Redirected URL:", redirected_url) """

except Exception as e:
    print("Login page is not visible") 
    print(e)  # Print any exception that occurs for debugging purposes



# Phone number input = <input class="pDzPRp" type="text" placeholder="Phone number / Username / Email" autocomplete="on" name="loginKey" maxlength="128" aria-invalid="false" value="">
# Password input = <input class="pDzPRp" type="password" placeholder="Password" autocomplete="current-password" name="password" maxlength="16" aria-invalid="false" value="">
# Login button = <button class="wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1" disabled="">Log In</button>



# TEST 02 ----------------------------------------------------------------------------------------------------------- We will attempt to extract the author name and user review

# Find the element containing the author name using XPath
author_element = driver.find_element(By.XPATH, "//div[@class='product-ratings']//div[@class='product-ratings__list']//div[@class='shopee-product-comment-list']//div[@class='shopee-product-rating']//div[@class='shopee-product-rating__main']//a[@class='shopee-product-rating__author-name']")

# Find the element containing the user review
review_element = driver.find_element(By.XPATH, "//div[@class='product-ratings']//div[@class='product-ratings__list']//div[@class='shopee-product-comment-list']//div[@class='shopee-product-rating']//div[@class='shopee-product-rating__main']")


# Get the text content of the author name
author_name = author_element.text

# Get the review
author_review = review_element.text


# Print the author name
print(author_name)

# Print the author review
print(author_review)



# //div[@class='']
""" 
<div class="shopee-product-comment-list">
    <div class="shopee-product-rating">
        <div class="shopee-product-rating__main">
            <a class="shopee-product-rating__author-name" href="/shop/221442533">lionelbiay</a>
            <div style="position: relative; box-sizing: border-box; margin: 15px 0px; font-size: 14px; line-height: 20px; color: rgba(0, 0, 0, 0.87); word-break: break-word; white-space: pre-wrap;">
            The product quality is good. Di ko pa natatry yung item. Pero secured naman nung dumating. Nakabubble wrap. Salamat sa seller. Responsive din sya sa mga chats ko. 😊
            </div>
        </div>
    </div>
 """



# TEST 03 ----------------------------------------------------------------------------------------------------------- We will attempt to click next page

next_button = driver.find_element(By.XPATH, "//button[@class='shopee-icon-button shopee-icon-button--right ']")

# Click the "Next" button
next_button.click()




# <button class="shopee-icon-button shopee-icon-button--right "><svg enable-background="new 0 0 11 11" viewBox="0 0 11 11" x="0" y="0" class="shopee-svg-icon icon-arrow-right"><path d="m2.5 11c .1 0 .2 0 .3-.1l6-5c .1-.1.2-.3.2-.4s-.1-.3-.2-.4l-6-5c-.2-.2-.5-.1-.7.1s-.1.5.1.7l5.5 4.6-5.5 4.6c-.2.2-.2.5-.1.7.1.1.3.2.4.2z"></path></svg></button>



# FINDINDS -----------------------------------------------------------------------------------------------------------

# Unfortunately, it is impossible to bypass Shoppee's anti-bot mechanism