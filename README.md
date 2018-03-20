# Parsing Electoral Roll PDFs

The repository provides scripts for parsing the Indian Electoral Roll pdfs and links to the data along with a summary of the issues and some summary statistics for each state.

* [Data](https://github.com/in-rolls/parse_elex_rolls#data)
* [Scripts](https://github.com/in-rolls/parse_elex_rolls#scripts)
  - [Readable English Electoral Roll PDFs](https://github.com/in-rolls/parse_elex_rolls#readable-english-electoral-roll-pdfs)
  - [Readable Hindi Electoral Roll PDFs](https://github.com/in-rolls/parse_elex_rolls#readable-hindi-electoral-roll-pdfs)

-------

## Scripts

The scripts in this repository parse Indian Electoral Rolls. For more information on how to get PDFs of electoral rolls, see https://github.com/in-rolls/electoral_rolls/ 

### Readable English Electoral Roll PDFs

Andaman & Nicobar Islands, Andhra Pradesh, Arunachal Pradesh, Dadra & Nagar Haveli, Daman & Diu, Goa, Jammu & Kashmir, Kerala, Manipur, Meghalaya, Mizoram, Nagaland, NCT OF Delhi, Puducherry, and Sikkim provide electoral rolls in English. Sikkim, Delhi, and Kerala's electoral rolls aren't readable.

The format of the rolls is similar but not the same so we write a separate scripts for each, relying on some common functions like [pdfparser/rolls/base.py](pdfparser/rolls/base.py), etc.

**Requirements**

poppler-utils (>=0.57)

**Input and Output**

The python script takes as input either path to a specific pdf electoral rolls that needs to be parsed or a directory of English language electoral roll pdfs, and produces a CSV with the following columns: `number (top left box in the elector field), id, elector_name, father_or_husband_name, husband (dummy for husband), house_no, age, sex, ac_name, parl_constituency, part_no, year, state, filename, main_town, police_station, mandal, revenue_division, district, pin_code, polling_station_name, polling_station_address, net_electors_male, net_electors_female, net_electors_third_gender, net_electors_total`. 

**Using pdfparser**

```
usage: pdfparser [-h] [-f FILE] [-d DIR] [-s STATE] [-o FILE] [--resume]
                 [--version] [--all-states]

Parse Indian PDF electoral rolls and get a CSV of a list of electors.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path to the specific PDF file to be parsed
  -d DIR, --dir DIR     path to directory containing the PDF files
  -s STATE, --state STATE
                        Name of state where PDF document(s) is/are published
  -o FILE, --out FILE   Specify the output file for storing the results 
                        (must be a '.csv' file). The default output file is
                        'Parsed-{timestamp}.csv' in the 'output' directory
  --resume              Allows us to resume parsing if the program was stopped
                        unexpectedly or intentionally. Only takes effect if a
                        directory is being parsed
  --version             show program's version number and exit
  --all-states          show all the supported states and exit
```

**Examples**

```
./pdfparser -d manipur/ -s manipur -o manipur.csv
./pdfparser --all-states
```

**States**

* [Andaman and Nicobar Islands](pdfparser/modules/rolls/andaman.py)
* [Andhra Pradesh](pdfparser/modules/rolls/andhra.py)
* [Arunachal Pradesh](pdfparser/modules/rolls/arunachal.py)
* [Dadra and Nagar Haveli](pdfparser/modules/rolls/dadra.py)
* [Daman and Diu](pdfparser/modules/rolls/daman.py)
* [Goa](pdfparser/modules/rolls/goa.py)
* [Jammu and Kashmir](pdfparser/modules/rolls/jk.py)
* [Manipur](pdfparser/modules/rolls/manipur.py)
* [Meghalaya](pdfparser/modules/rolls/meghalaya.py)
* [Mizoram](pdfparser/modules/rolls/mizoram.py)
* [Nagaland](pdfparser/modules/rolls/nagaland.py)
* [Puducherry](pdfparser/modules/rolls/puducherry.py)

### Readable Hindi Electoral Roll PDFs

**States**

* [Bihar](pdfparser/modules/rolls/bihar.py)
* [Chandigarh](pdfparser/modules/rolls/chandigarh.py)
* [Haryana](pdfparser/modules/rolls/haryana.py)
* [Himachal Pradesh](pdfparser/modules/rolls/himachal.py)
* [Jammu and Kashmir](pdfparser/modules/rolls/jk_hindi.py)
* [Jharkhand](pdfparser/modules/rolls/jharkhand.py)
* [Madhya Pradesh](pdfparser/modules/rolls/madhya_pradesh.py)
* [Rajasthan](pdfparser/modules/rolls/rajasthan.py)
* [Uttar Pradesh](pdfparser/modules/rolls/up.py)
* [Uttarakhand](pdfparser/modules/rolls/uttarakhand.py)

## Checks

To verify that the electoral rolls have been parsed correctly, we institute a few checks. For English language rolls, we checked:

1. If age a reasonable number?
2. How many characters are there in 'ID'? 
3. How many characters does pincode have?
4. How many characters does elector_name have?
5. What unique values does the sex field have? 
6. What unique values does main_town, district, ac_name, mandal, etc. have? 
7. Do the numbers in total_electors field match up?

### Future checks:

1. For 18 of the 34 states on which we have data, we scraped metadata about polling stations. For instance, https://github.com/in-rolls/electoral_rolls/tree/master/kerala has a CSV that captures the metadata from the website. Some of the columns we parse can be checked against that. Addition data from https://github.com/in-rolls/poll-station-metadata can potentially also be used.

2. The electoral rolls have some totals within them. We scrape those. For instance, total number of women, men, etc. And we can re-derive those numbers from the scraped columns. We check for that.

3. Second parsing script and tallying results against each other.

### For native language electoral rolls:

1. we also capitalize on the fact that some states have both native and English language rolls. And where they are available, we have downloaded both. And we can compare some of the columns against each other.

### Issues

Here are some [issues](issues.md) that we found with the electoral rolls.

### Data

The parsed data are available on the [Harvard Dataverse](http://dx.doi.org/10.7910/DVN/MUEGDT). For state-wise summary statistics and sanity checks, see state by state folders under [data/](data/).

The data are available only for research purposes. And only if the requester agrees to do their best to protect the privacy of the people and to never sell or share data for commercial gain. 

If you would like access to the electoral rolls, please fill out the following [form](https://goo.gl/forms/CD85MwGW8cBTTJM92).

You will also need to get IRB approval from your university or institution. The IRB-approved proposal should include:

* Case for why the data are necessary
* Acknowledgment that the data will be kept in a secure environment
* All the people who will have access to the data
* That the data will only be used on projects with IRB approval
* That data won't be shared with people who are not identified in 3.
* That publications and presentations will not reveal identifying individual information: only statistical summaries will be presented.

## License

The scripts are released under the [MIT License](https://opensource.org/licenses/MIT).
