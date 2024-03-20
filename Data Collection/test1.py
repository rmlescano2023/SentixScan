# This code extracts the shop_id & item_id from a product URL

import re

def extract_ids(url):
    # Regular expression pattern to extract numbers between "i" and "?sp_atk"
    pattern = r'i\.(\d+)\.(\d+)\?sp_atk'
    
    # Find the match using the pattern
    match = re.search(pattern, url)
    
    if match:
        shop_id = match.group(1)
        item_id = match.group(2)
        return shop_id, item_id
    else:
        return None, None

# Example usage
url = "https://shopee.ph/Baseus-WM02-True-Wireless-Earphones-i.131196305.17552845260?sp_atk=ef0e9936-ea9d-41f0-8ad6-b0470408a11e&xptdk=ef0e9936-ea9d-41f0-8ad6-b0470408a11e"
shop_id, item_id = extract_ids(url)
print("Shop ID:", shop_id)
print("Item ID:", item_id)










# itemid and shopid can now be taken. Now i just have to get a list of all the URLs.




# Sample URLs:
# https://shopee.ph/itel-P55-RAM-24GB(8-16GB)-ROM-128GB-90HZ-Refresh-50MP-Dual-Camera-5000mAh-18W-i.655822401.24706665159?sp_atk=b3fe03f1-ce8b-4318-ab1d-f10bf46475b9&xptdk=b3fe03f1-ce8b-4318-ab1d-f10bf46475b9
# item_id = 24706665159
# shop_id = 655822401

# https://shopee.ph/Maybelline-Fit-Me-Fresh-Tint-with-Vit-C-Skin-Tint-Sunscreen-SPF-50PA-BB-Cream-Brightening-i.65430610.21427809610?sp_atk=dc941d9e-61ef-4d19-b842-bdb7c910844c&xptdk=dc941d9e-61ef-4d19-b842-bdb7c910844c
# item_id = 21427809610
# shop_id = 65430610