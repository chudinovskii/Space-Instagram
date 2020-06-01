# Space Instagram

Console app for fetching photos from SpaceX API and Hubble API and then for uploading them to Instagram

## **How to install**

Python3 should be already installed. Then use pip to install dependencies:

`pip install -r requirements.txt`


## Usage



 **To fetch photos from the latest SpaceX launch:**
 
`$ fetch_spacex.py`
 
 **To fetch Hubble photos:**
 
`$ fetch_hubble.py`

**To upload photos to your Instagram:**

You need to edit .env file: 

`INST_LOGIN = 'yourlogin'
INST_PWD = 'yourpassword'`

Then:

`$ upload_to_inst.py`

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/)
