# Parsing Searchable Electoral Roll PDFs

The repository provides scripts for parsing searchable Indian Electoral Roll pdfs and links to the data along with a summary of the issues and some summary statistics for each state.

* [Data](https://github.com/in-rolls/parse_elex_rolls#data)
* [Scripts](https://github.com/in-rolls/parse_elex_rolls#scripts)
  - [Searchable English Electoral Roll PDFs](https://github.com/in-rolls/parse_elex_rolls#searchable-english-electoral-roll-pdfs)
* [Tests](https://github.com/in-rolls/parse_elex_rolls#tests)

Scripts for parsing unsearchable electoral rolls are posted [here](https://github.com/in-rolls/parse_unsearchable_rolls).

-------

### Data

For more information on how to get PDFs of electoral rolls, see https://github.com/in-rolls/electoral_rolls/

### Parsing Searchable English Electoral Roll PDFs

12 Indian states and Union Territories provide searchable rolls:  Andaman & Nicobar Islands, Andhra Pradesh, Arunachal Pradesh, Dadra & Nagar Haveli, Daman & Diu, Goa, Jammu & Kashmir, Manipur, Meghalaya, Mizoram, Nagaland, and Puducherry. They are all in English.

The format of the rolls is similar but not the same, so we write a separate scripts for each, relying on some common functions like [pdfparser/rolls/base.py](pdfparser/rolls/base.py), etc.

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

* [Andaman and Nicobar Islands](pdfparser/modules/rolls/andaman/)
* [Andhra Pradesh](pdfparser/modules/rolls/andhra/)
* [Arunachal Pradesh](pdfparser/modules/rolls/arunachal/)
* [Dadra and Nagar Haveli](pdfparser/modules/rolls/dadra/)
* [Daman and Diu](pdfparser/modules/rolls/daman/)
* [Goa](pdfparser/modules/rolls/goa/)
* [Jammu and Kashmir](pdfparser/modules/rolls/jk/)
* [Manipur](pdfparser/modules/rolls/manipur/)
* [Meghalaya](pdfparser/modules/rolls/meghalaya/)
* [Mizoram](pdfparser/modules/rolls/mizoram/)
* [Nagaland](pdfparser/modules/rolls/nagaland/)
* [Puducherry](pdfparser/modules/rolls/puducherry/)

### Tests

To verify that the electoral rolls have been parsed correctly, we institute a few checks. For English language rolls, we checked:

1. Is age a reasonable number?
2. How many characters are there in 'ID'?
3. How many characters are there in pincode?
4. How many characters does elector_name have?
5. What unique values does the sex field have?
6. What unique values does main_town, district, ac_name, mandal, etc. have?
7. Do the numbers in total_electors field match up?

#### Future Tests

1. For 18 of the 34 states on which we have data, we scraped metadata about polling stations. For instance, https://github.com/in-rolls/electoral_rolls/tree/master/kerala has a CSV that captures the metadata from the website. Some of the columns we parse can be checked against that. Addition data from https://github.com/in-rolls/poll-station-metadata can potentially also be used.

2. The electoral rolls have some totals within them. We scrape those. For instance, the total number of women, men, etc. And we can re-derive those numbers from the scraped columns. We check for that.

3. Second parsing script and tallying results against each other.

4. Capitalize on the fact that some states have both native and English language rolls. And where they are available, we have downloaded both. And we can compare some of the columns against each other.

### Issues

Here are some [issues](issues.md) that we found with the electoral rolls.

### Other Scripts

We have a separate set of scripts (Python notebooks) for the following states:

* [Chandigarh](scripts/chandigarh.ipynb)
* [Haryana](scripts/haryana.ipynb)
* [Himachal Pradesh](scripts/himachal-tabula-py.ipynb)
* [Jharkhand](scripts/jharkhand-tabular-py.ipynb)

They produce elector level data but don't have other metadata as that is unreadable. There are some other coding issues which mean there are some other errors in the output.  

### Data

The parsed data are available on the [Harvard Dataverse](http://dx.doi.org/10.7910/DVN/MUEGDT). For state wise summary statistics and sanity checks, see state by state folders under [data/](data/).

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
