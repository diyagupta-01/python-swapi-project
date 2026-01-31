# python-swapi-project
A Python project that fetches Star Wars character data from the SWAPI (Star Wars API) using requests and JSON parsing.
# Star Wars API Project (SWAPI)

This project fetches character data from the **Star Wars API (SWAPI)** and stores the first 20 characters in a clean CSV dataset.  
It uses the public API with no authentication required.

---

##  Tools & Libraries Used
- Python  
- Requests  
- Pandas  
- Google Colab  

---

## What This Project Does
- Calls the SWAPI endpoint for characters  
- Fetches **first 20 Star Wars characters**  
- Extracts:
  - name  
  - height  
  - mass  
  - gender  
  - birth year  
  - homeworld URL  
  - number of films they appear in  
- Saves results into `swapi_characters.csv`  

---

##  Project Structure
python-swapi-project/
│── swapi_characters.py # main API script
│── swapi_characters.ipynb # Colab notebook version
│── swapi_characters.csv # output dataset
│── README.md


---

## How to Run

Install requirements:

```bash
pip install requests pandas
```

Run the script:
```
python swapi_characters.py
```

Output will be saved as:
```
swapi_characters.csv
```
Purpose
---
This project demonstrates:

- Working with a public REST API

- Parsing JSON

- Extracting structured fields

- Converting API data to a DataFrame

- Exporting cleaned output to CSV

- Building a clean, portfolio-ready Python API project

Source
---
Data from SWAPI:
https://swapi.dev/

(A free, public API for Star Wars data)

