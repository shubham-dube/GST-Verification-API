# GST Verification API

This API fetches GST Taxpayer Details with GSTIN and provide data in JSON format

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Endpoints](#EndPoints)
- [Support](#Support)
- [Contribution](#Contribution)

## Features

- It Maintains session information for handling dynamic captcha url.
- Send GSTIN and captcha code to check GST details.
- Return GSTIN details in a structured JSON format.
- Easy to integrate in any of your application.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shubham-dube/GST-Verification-API.git
   cd GST-Verification-API
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate # On Linux use `source venv/bin/activate`
   
3. Install the dependencies:
   ```bash
   pip install flask requests uuid base64

4. Run the Application:
   ```bash
   python app.py
 *The API will be available at http://127.0.0.1:5000.*
 
## Usage
- Show the Cpatcha to the user Coming by sending GET request to one the of the endpoint and one input for GSTIN.
- Send the GSTIN entered and captcha along with the session id recieved.
- You will get all the details related to that GSTIN in the JSON format.
  
## EndPoints

### Fetching Captcha

**Endpoint:** `/api/v1/getCaptcha`

**Method:** `GET`

**Description:** `This Endpoint gets the current instance of captcha from that website as a base64 encoding`

**Response**
```json
{
  "sessionId": "someencoding",
  "image": 'data:image/png;base64, captchaBase64 '
}
```
**Status Codes**
- 200 OK : `Captcha Recieved`

### Get GST Details to verify

**Endpoint:** `/api/v1/getGSTDetails`

**Method:** `POST`

**Description:** `Submits the GSTIN and captcha given, to the website and extract or scrap further GSTIN Taxpayer Details`

**Request Body:**
```json
{
  "sessionId": "OBTAINED ON FETCHING CAPTCHA",
  "GSTIN": "01ABCDE0123F0AA",
  "captcha": "your_captcha_here"
}
```
**Response**
```json
{
    "adhrVFlag": "Yes",
    "adhrVdt": "29/01/2021",
    "cmpRt": "NA",
    "ctb": "Proprietorship",
    "ctj": "Address",
    "cxdt": "",
    "dty": "Regular",
    "einvoiceStatus": "No",
    "ekycVFlag": "Not Applicable",
    "gstin": "01ABCDE0123F0AA",
    "isFieldVisitConducted": "No",
    "lgnm": "ABCDEF GHIJK",
    "nba": [
        "Retail Business",
        "Wholesale Business",
        "Supplier of Services"
    ],
    "ntcrbs": "TRD:TRR",
    "pradr": {
        "adr": "Address"
    },
    "rgdt": "Registration Date",
    "stj": "Division",
    "sts": "Status",
    "tradeNam": "Trade Name"
}
```
**Status Codes**
- 200 OK : `Data Retrieved Successfuly`

## Support
For Support Contact me at itzshubhamofficial@gmail.com
or Mobile Number : `+917687877772`

## Contribution

We welcome contributions to improve this project. Here are some ways you can contribute:

1. **Report Bugs:** If you find any bugs, please report them by opening an issue on GitHub.
2. **Feature Requests:** If you have ideas for new features, feel free to suggest them by opening an issue.
3. **Code Contributions:** 
    - Fork the repository.
    - Create a new branch (`git checkout -b feature-branch`).
    - Make your changes.
    - Commit your changes (`git commit -m 'Add some feature'`).
    - Push to the branch (`git push origin feature-branch`).
    - Open a pull request.

4. **Documentation:** Improve the documentation to help others understand and use the project.
5. **Testing:** Write tests to improve code coverage and ensure stability.

Please make sure your contributions adhere to our coding guidelines and standards.
