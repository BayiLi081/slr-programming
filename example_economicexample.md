The alternative searching syntax to include more similar terminology will be

```
TI = ("economic segregation" OR "income segregation" OR "wealth segregation" OR "economic inequality" OR "income inequality" OR "wealth inequality"  OR "economic segregated " OR "income segregated" OR "wealth segregated" OR "economic stratification " OR "income stratification" OR "wealth stratification") AND (SU ==("SOCIOLOGY" OR "SOCIAL SCIENCES OTHER TOPICS" OR "GEOGRAPHY" OR "MATHEMATICAL METHODS IN SOCIAL SCIENCES" OR "BUSINESS ECONOMICS" OR "PUBLIC ADMINISTRATION" OR "URBAN STUDIES")) AND LA=(English)
```

But in this case, we use the simplified definition just to grasp the understanding of "economic segregation" (including "income segregation" and "economic segregation"):

```
TI = ("economic segregation" OR "income segregation" OR "wealth segregation" OR "economic segregated " OR "income segregated" OR "wealth segregated") AND (SU ==("SOCIOLOGY" OR "SOCIAL SCIENCES OTHER TOPICS" OR "GEOGRAPHY" OR "MATHEMATICAL METHODS IN SOCIAL SCIENCES" OR "BUSINESS ECONOMICS" OR "PUBLIC ADMINISTRATION" OR "URBAN STUDIES")) AND LA=(English)
```

You can download the file in the format you desire, but in this case, we downloaded it as two format: Tab delimited file and Excel. We are using Web of Science as an example.

Because we are using the DOI to scrape the PDF, thus, we checked the records from the WOS, to ensure we have the DOI value for each record. Otherwise, we will need to manually check the PDF file. 

Download the PDFs

To download the PDFs from the collected table from WOS

**To collect the full-text of paper, there is a Python library** [**ferru97/PyPaperBot**](https://github.com/ferru97/PyPaperBot)**,** runs on terminal, can download the papers automatically based on their DOIs. The tutorial can view at [Hacks to Summon Research Pdf Files into Your Local Computer, All At Once! | by Go Woojin | Medium](https://medium.com/@woojingo/hacks-to-summon-research-pdf-files-into-your-local-computer-all-at-once-58860259e372).

The code blocks to download 

The txt file to be read from the PyPaperBot should contain the data as following, this can be cleaned by the sortDOI.py

```
10.1111/iere.12466
10.1086/657114
10.1515/bejeap-2017-0314
10.1111/j.1467-9787.2007.00508.x
10.15195/v6.a19
10.1111/j.1540-6237.2006.00401.x
10.1016/j.compenvurbsys.2011.07.008
10.1016/j.jpubeco.2006.10.006
```

Before the comma, it is the unique ID for the paper; after the comma, it is the sorted DOIs. 

```
python -m PyPaperBot --doi-file="data/sample-data/pure_doi.txt" --dwn-dir="data/collection/PDFs" --scihub-mirror="https://sci-hub.se/"
```

The batch download of PDFs is from Sci-hub, so naturally, it does not contain the publications after 2019.

You can have your way of filter paper, in th example, we are using total number of 
