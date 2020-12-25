#!/usr/bin/env python
# coding: utf-8

import os
import fitz
import re
from glob import glob
import pandas as pd
import tarfile

### From parse_in_rolls

COLUMNS = ["number","id", "elector_name", "father_or_husband_name", "relationship", "house_no", "age", "sex", "ac_name", "parl_constituency", "part_no", "year", "state", "filename", "main_town", "police_station", "mandal", "revenue_division", "district", "pin_code", "polling_station_name", "polling_station_address", "net_electors_male", "net_electors_female", "net_electors_third_gender", "net_electors_total","original_or_amendment"]

INPUT_FILE = '/opt/data/in-electoral-rolls/haryana.tar.gz'

rows = []
with tarfile.open(INPUT_FILE, "r:gz") as tar:
    members = tar.getmembers()[1:]
    print('Total PDF files: %d' % len(members))
    for i, t in enumerate(members):
        fn = t.name
        with tar.extractfile(t) as f:
            pdf_data = f.read()
        doc = fitz.open('pdf', pdf_data)
        for p in doc:
            text = p.getText()
            for m in re.finditer(r'(?<=\n)(.*?\n\d+\n.*?\nनाम :(.*?\nहै।))', '\n' + text, flags=re.DOTALL):
                box = m.group(1)
                elector_name = re.findall(r'(.*?)\d+', box, flags=re.S)[0].strip().replace('\n', ' ')
                number = re.findall(r'.*?(\d+)', box, flags=re.S)[0].strip()
                _id = re.findall(r'.*?\d+\n(.*?)\n', box, flags=re.S)[0].strip()
                a = re.findall(r'नाम :\n(.*?)\nमकान  नं. :', box, flags=re.S)[0].strip().split(':')
                relationship = a[0].strip()
                father_or_husband_name = a[1].strip()
                house_no = re.findall(r'मकान  नं. :(.*?)आयु', box, flags=re.S)[0].strip()
                age = re.findall(r'आयु :(.*?)िलग', box, flags=re.S)[0].strip()
                sex = re.findall(r'लग : (.*?)फोटो', box, flags=re.S)[0].strip()
                data = {'filename': os.path.basename(fn),
                        'number': number,
                        'id': _id,
                        'elector_name': elector_name,
                        'father_or_husband_name': father_or_husband_name,
                        'relationship': relationship,
                        'house_no': house_no,
                        'age': age,
                        'sex': sex,
                       }
                rows.append(data)
        print(i + 1, fn, len(rows))
        #break
df = pd.DataFrame(rows)
df.to_csv('/opt/data/searchable_rolls/haryana.csv.gz', index_label='index')
