#!/usr/bin/env python
# coding: utf-8
import os
import re
from glob import glob
import pandas as pd
import tarfile
import tabula

### From parse_in_rolls
COLUMNS = ["number","id", "elector_name", "father_or_husband_name", "relationship", "house_no", "age", "sex", "ac_name", "parl_constituency", "part_no", "year", "state", "filename", "main_town", "police_station", "mandal", "revenue_division", "district", "pin_code", "polling_station_name", "polling_station_address", "net_electors_male", "net_electors_female", "net_electors_third_gender", "net_electors_total","original_or_amendment"]


# Columns
"""
क्रम
मकान न.
मतदाता का नाम
सम्बन्ध
सम्बन्धी का नाम
लिंग
आयु
पहचान पत्र
फोटो
"""
"""
Order
House No.
Voter's name
Relations
Relative name
Gender
Age
identity card
Photo
"""

INPUT_FILE = '/opt/data/in-electoral-rolls/himachal_pdfs.tar.gz'

rows = []
with tarfile.open(INPUT_FILE, "r:gz") as tar:
    members = tar.getmembers()[1:]
    print('Total PDF files: %d' % len(members))
    for i, t in enumerate(members):
        fn = t.name
        with tar.extractfile(t) as f:
            dfs = tabula.read_pdf(f, pages='all', lattice = False, silent=True)
            for i, df in enumerate(dfs):
                for j, r in df.iterrows():
                    txt = ' '.join(r.dropna().astype(str))
                    m = re.match(r'(?:O\s)?(\d*)\s([कखगॠख़AB\s\d\/\(\)\-\,]*)\s?(.*)\s?(िपता|पित|प.त|.पता|माता)\s(.*)\s?(प.{1,3}ष|पु.ष|म.हला|मिहला)\s([\d\.]*)\s([\dA-Z\/]*)\s?(.*)$', txt)
                    if m:
                        pass
                        #print(os.path.basename(fn), m.group(1), '|', m.group(2), '|', m.group(3), '|', m.group(4), '|', m.group(5), '|', m.group(6), '|', m.group(7), '|', m.group(8), '|', m.group(9))
                        data = {'filename': os.path.basename(fn),
                                'number': m.group(1),
                                'id': m.group(8),
                                'elector_name': m.group(3),
                                'father_or_husband_name': m.group(5),
                                'relationship': m.group(4),
                                'house_no': m.group(2),
                                'age': m.group(7),
                                'sex': m.group(6),
                               }
                        rows.append(data)
                    else:
                        m2 = re.match(r'(?:O\s)?(\d*)\s(.*)$', txt)
                        if m2:
                            print(os.path.basename(fn), txt)
            #break


df = pd.DataFrame(rows)

df.to_csv('/opt/data/searchable_rolls/himachal.csv.gz', index_label='index')

