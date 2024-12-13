# Web Scraping Dockerlabs

This project performs web scraping on the Dockerlabs website to extract the names of containers available on the page. The extracted data is saved in both a `dockerlabs_data.json` file and a `dockerlabs_data.csv` file for further use or analysis.

## Description

The script `main.py` scrapes the **[Dockerlabs](https://dockerlabs.es/)** website to find all the names of the containers. These names are extracted using XPath to navigate through the HTML structure of the page. The results obtained are saved in both JSON and CSV formats with the following structure:

```json
[
    {
        "text": "Nombre del container 1"
    },
    {
        "text": "Nombre del container 2"
    },
    ...
]
```

```text
text
Container Name 1
Container Name 2
...
```