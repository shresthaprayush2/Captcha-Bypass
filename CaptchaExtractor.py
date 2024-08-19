from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytesseract


def main():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)

    # Replace with your site url from where you want to extract data
    loginUrl = ''
    driver.get(loginUrl)

    username = 'username'
    password = 'password'

    userNameInputBox = driver.find_element(By.XPATH,
                                           '//*[contains(concat( " ", @class, " " ), concat( " ", "ng-invalid", " " ))]')
    passwordInputBox = driver.find_element(By.XPATH, '//*[(@id = "password-field")]')
    captchaBox = driver.find_element(By.XPATH, '//*[(@id = "captchaEnter")]')
    userNameInputBox.send_keys(username)
    captchaSuccess = False

    # Getting the captcha image by using XPATH
    captchaImage = driver.find_element(By.XPATH,
                                       '//*[contains(concat( " ", @class, " " ), concat( " ", "captcha-image-dimension", " " ))]')

    # Using loop to try multiple times, You need to improve your code here
    while not captchaSuccess:
        # Getting the screeshot of the captcha image
        # The image couldn't be donwload so I had to imrpovise
        captchaImage.screenshot('sc.png')
        captchaText = getCaptchaText()
        # Filling the password block
        passwordInputBox.send_keys(password)
        # filling the captcha Box
        captchaBox.send_keys(captchaText)
        time.sleep(5)
        try:
            # Checking for information block this will be visible after login success
            myInformationBlock = driver.find_element(By.XPATH,
                                                     '/html/body/app-root/tms/app-menubar/aside/nav/ul/li[3]/a')
            captchaSuccess = True
            break
        except Exception as e:
            print('Error')
            captchaSuccess = False


# This function does the actual work of getting the CAPTCHA text from iage
def getCaptchaText():
    input_image_path = 'sc.png'
    output_image_path = '../images/sc_noiseless.jpg'

    # Using open CV to read image
    # Read the image in grayscale mode
    image_bw = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Denoising
    noiseless_image_bw = cv2.fastNlMeansDenoising(image_bw, None, 20, 7, 21)

    # Structuring element for morphological operations
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
    bg = cv2.morphologyEx(noiseless_image_bw, cv2.MORPH_DILATE, se)

    # Obtain foreground image
    out_gray = cv2.divide(noiseless_image_bw, bg, scale=255)

    # Thresholding to get a binary image
    _, out_binary = cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU)

    # Save the processed image
    cv2.imwrite(output_image_path, out_binary)

    # Using Tesseract OCR to extract text
    # https: // github.com / UB - Mannheim / tesseract / wiki get the teserract here
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    extracted_text = pytesseract.image_to_string(out_binary)

    print(f'{extracted_text}')
    return extracted_text


main()


