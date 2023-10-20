import os
from urllib import request

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Path to save images to
# SAVE_PATH = ""

# PAth to add Chrome Driver
# CHROME_DRIVER_PATH = ""





BASE_URL = "https://www.bing.com/create?toWww=1&redig=30C04FC20A7A4BA08168CC7BB17EDFD6"

ecommerce_icon_image_prompts = [
    "Icon: Shopping Cart | Description: A sleek shopping cart icon, metallic and filled with assorted items, representing diverse products.",
    "Icon: Price Tag | Description: A modern price tag, its string forming a dollar sign, symbolizing value and affordability.",
    "Icon: Delivery Truck | Description: A fast-moving delivery truck, leaving behind a trail of sparkles, symbolizing quick and efficient service.",
    "Icon: Barcode | Description: A crisp barcode, being scanned by a beam of light, representing product identity.",
    "Icon: Wishlist Heart | Description: A heart-shaped icon, its surface covered in tiny gift boxes, representing users' favorite products.",
    "Icon: Customer Review | Description: A speech bubble filled with stars, symbolizing positive customer feedback and testimonials.",
    "Icon: Sale Balloon | Description: A floating balloon with the word 'SALE' and a percentage sign, highlighting special discounts.",
    "Icon: Secure Payment | Description: A credit card shielded by a lock, symbolizing safe and encrypted transactions.",
    "Icon: Customer Support | Description: A headset icon, surrounded by reassuring waves, indicating friendly customer support.",
    "Icon: Return Policy | Description: A reverse arrow circling a product box, representing hassle-free returns and exchanges."
]



products = {
    "Ecom":ecommerce_icon_image_prompts,
}



image_xpaths = [
    '//*[@id="mmComponent_images_as_1"]/ul[1]/li[1]/div/div/a/div/img',
    '//*[@id="mmComponent_images_as_1"]/ul[1]/li[2]/div/div/a/div/img',
    '//*[@id="mmComponent_images_as_1"]/ul[2]/li[1]/div/div/a/div/img',
    '//*[@id="mmComponent_images_as_1"]/ul[2]/li[2]/div/div/a/div/img',
]

def download_image(url, file_path):
    try:
        request.urlretrieve(url, file_path)
        return True
    except Exception as e:
        print(f"Error while downloading image: {e}")
        return False

def main():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    card_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for suit, product_set in products.items():
        suit_folder = os.path.join(SAVE_PATH, suit)
        os.makedirs(suit_folder, exist_ok=True)

        for i, product in enumerate(product_set):
            driver.get(BASE_URL)

            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="sb_form_q"]'))
            )
            search_box.clear()
            
            search_box.send_keys(f"{product}")
            search_box.submit()

            card_folder = os.path.join(suit_folder, card_names[i])
            os.makedirs(card_folder, exist_ok=True)

            for index, xpath in enumerate(image_xpaths, start=1):
                
                try:
                    generated_image = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    generated_image_url = generated_image.get_attribute("src")

                    image_file_name = f"{index}.jpg"
                    file_path = os.path.join(card_folder, image_file_name)
                    

                    downloaded = download_image(generated_image_url, file_path)

                    if downloaded:
                        print(f"Image {index} for {product} saved successfully.")
                    else:
                        print(f"Failed to download image {index} for {product}.")
                except Exception as e:
                    print(f"Error while downloading image {index} for {product}: {e}")

    driver.quit()

if __name__ == "__main__":
    main()