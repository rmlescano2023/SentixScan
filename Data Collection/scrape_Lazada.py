import undetected_chromedriver as uc 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = uc.Chrome() 
driver.get("https://www.lazada.com.ph")

URL = "https://www.lazada.com.ph/products/along94-sling-bag-3081b-high-quality-i3993607442-s21545007970.html?spm=a2o4l.home-ph.3964150330.16.5f06ca183OOKhT&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.1859336644411087%3Bfs_item_discount_price%3A140.97%3Bitem_id%3A3993607442%3Bpctr%3A0.1859336644411087%3Bcalib_pctr%3A0.0%3Bvoucher_price%3A140.97%3Bmt%3Ahot%3Bpromo_price%3A140.97%3Bfs_utdid%3A-1%3Bfs_item_sold_cnt%3A55%3Babid%3A287818%3Bfs_item_price%3A598.00%3Bpvid%3A0bc133b5-cfb1-4be4-8002-64ddff80b938%3Bfs_min_price_l30d%3A0%3Bdata_type%3Aflashsale%3Bfs_pvid%3A0bc133b5-cfb1-4be4-8002-64ddff80b938%3Btime%3A1708174315%3Bfs_biz_type%3Afs%3Bscm%3A1007.17760.287818.%3Bchannel_id%3A0000%3Bfs_item_discount%3A76%25%3Bcampaign_id%3A269482&scm=1007.17760.287818.0"
driver.get(URL)

# TEST 01 ------------------------------------------------------------------------------------------------------------

# Find review elements using XPath
review_elements = driver.find_elements(By.XPATH, "//div[@class='mod-reviews']//div[@class='content']")

# Iterate over the review elements and print their text content
for review_element in review_elements:
    print(review_element.text)

driver.quit()

# TEST 02 ------------------------------------------------------------------------------------------------------------

# Find the "Next" button
next_button = driver.find_element(By.XPATH, "//button[@class='next-btn next-btn-normal next-btn-medium next-pagination-item next']")

# Click the "Next" button
next_button.click()

# TEST 03 ------------------------------------------------------------------------------------------------------------

while True:
    # Find the "Next" button
    next_button = driver.find_element(By.XPATH, "//button[@class='next-btn next-btn-normal next-btn-medium next-pagination-item next']")

    # Check if the "Next" button is disabled
    is_disabled = next_button.get_attribute("disabled")
    if is_disabled:
        # If the button is disabled, break out of the loop
        break

    # Click the "Next" button
    next_button.click()

    """ # Wait for the button to become clickable again
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='next-btn next-btn-normal next-btn-medium next-pagination-item next']"))
    ) """

# <button type="button" class="next-btn next-btn-normal next-btn-medium next-pagination-item next" data-spm-anchor-id="a2o4l.pdp_revamp.ratings_reviews.i6.7aeb1766aOfqMp"><i class="next-icon next-icon-arrow-right next-icon-medium next-icon-last" data-spm-anchor-id="a2o4l.pdp_revamp.ratings_reviews.i5.7aeb1766aOfqMp"></i></button>
# <button type="button" class="next-btn next-btn-normal next-btn-medium next-pagination-item next" data-spm-anchor-id="a2o4l.pdp_revamp.ratings_reviews.i6.7aeb1766aOfqMp" disabled=""><i class="next-icon next-icon-arrow-right next-icon-medium next-icon-last" data-spm-anchor-id="a2o4l.pdp_revamp.ratings_reviews.i5.7aeb1766aOfqMp"></i></button>



# FINDINDS -----------------------------------------------------------------------------------------------------------
# UNFORTUNATELY, LAZADA DETECTS TRAFFIC EASILY
# WE AIM TO FIND AN E-COMMERCE PLATFORM THAT HAS  A "VIEW ALL REVIEWS" OPTION SO THAT THERE WILL BE NO NEED FOR TRAVERSING THROUGH EVERY REVIEW PAGE