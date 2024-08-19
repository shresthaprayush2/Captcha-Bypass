CAPTCHA Bypass with Selenium and Tesseract OCR

This project automates the login process for websites that require CAPTCHA input using Selenium for web automation and Tesseract OCR for CAPTCHA recognition. The script captures the CAPTCHA image, processes it to improve clarity, and extracts the text using OCR, enabling automated CAPTCHA-solving and login.
Features

    Automated Web Login: Uses Selenium to automate the login process on websites that require CAPTCHA input.
    CAPTCHA Image Processing: Enhances CAPTCHA images using OpenCV to improve OCR accuracy.
    Optical Character Recognition (OCR): Extracts text from CAPTCHA images using Tesseract OCR.
    Error Handling: Includes a loop to retry the login process until the CAPTCHA is correctly solved.

Requirements

    Python 3.x
    Selenium
    Tesseract OCR
    OpenCV
    Chrome WebDriver

Installation

    Clone the repository:

    bash

git clone https://github.com/shresthaprayush2/CaptchaExtractor
cd captcha-bypass-automation

Install the required Python packages:

bash

    pip install selenium opencv-python pytesseract

    Download Tesseract OCR:
        Download and install Tesseract from this link.
        Make sure to update the pytesseract.pytesseract.tesseract_cmd path in the script to the correct installation path.

    Install Chrome WebDriver:
        Download Chrome WebDriver that matches your version of Chrome from here.
        Add the Chrome WebDriver to your system path or place it in the same directory as the script.

Usage

    Update the script:
        Replace the loginUrl, username, and password variables in the script with the appropriate values for the website you are trying to automate.

    Run the script:

    bash

    python script_name.py

    CAPTCHA Bypass:
        The script will attempt to login by solving the CAPTCHA using OCR. It will keep trying until the correct CAPTCHA is recognized and the login is successful.

Example Code

Here’s a snippet from the core of the script:

python

def getCaptchaText():
    input_image_path = 'sc.png'
    output_image_path = '../images/sc_noiseless.jpg'

    # Using OpenCV to read image
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
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    extracted_text = pytesseract.image_to_string(out_binary)

    print(f'{extracted_text}')
    return extracted_text

Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or new features.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

For any questions or feedback, please reach out to prayushshrestha89@gmail.com
