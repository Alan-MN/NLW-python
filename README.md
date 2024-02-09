# Product Barcode Generator API

## Overview

This Python project is a Flask API that generates barcodes for product numbers using the `python-barcode` library.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Alan-MN/NLW-python.git
   cd NLW-python
   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. ***Run the Application:***
   ```bash
    python run.py

## API Endpoint

### Generate Barcode

- **Endpoint:** `/create_tag`
- **Method:** `POST`
- **Request:**
  ```json
  {"product_code": "123456789"}
- **Response:**
  - **Success:**
    ```json
    "data":{
                "type": "Tag Image",
                "Count": 1,
                "path": "123456789.png"
            }
    ```

