import os
import re
import logging
import pandas as pd
from pprint import pprint

import fitz

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO 

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("logs/jk_hindi.log"),
                              logging.StreamHandler()])

COLUMNS = ["number","id", "elector_name", "father_or_husband_name", "house_no", "age", "sex", "ac_name", "parl_constituency", "part_no", "year", "state", "filename", "main_town", "police_station", "mandal", "revenue_division", "district", "pin_code", "polling_station_name", "polling_station_address", "net_electors_male", "net_electors_female", "net_electors_third_gender", "net_electors_total","original_or_amendment"]

INPUT_PATH = 'input/jk_hindi/'
OUTPUT_PATH = 'output/jk_hindi/'
STATE = 'JK'

if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

def extract_with_pdfminer(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    #codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams) #,codec=codec)

    with open(path, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(fp, pagenos, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
            break
        text = retstr.getvalue()
    device.close()
    retstr.close()

    return re.sub('\(cid.*?\)', '', text)

def get_first_page_data(path, fn):
    text = extract_with_pdfminer(path)

    # Polling
    polling_name_key = 'मतदान के द्र की संख्या व नाम'
    polling_address_key = 'मतदान के द्र के  भवन का पताः'
    psn = ''.join(re.findall(polling_name_key + '.*?\n\n(.*?)\n', text, re.DOTALL)).strip()
    psa = ''.join(re.findall(polling_address_key + '.*?\n\n(.*?)\n', text, re.DOTALL)).strip()

    # Mandal
    #start = 'मुख्य ाम का नाम'
    start = 'िपन कोड'
    end = '\n\nमतदान के  की हैिसयत'
    mandal_values = ''.join(re.findall(start + '.*?\n(.*?)' + end, text, re.DOTALL)).split('\n')
    # if len(mandal_values) < 9:
    #     breakpoint()

    # Part number
    po_key = 'भाग संख्याः'
    part_number = ''.join(re.findall(po_key + '(.*?\d+)', text, re.DOTALL)).replace('\n', '').strip()

    # Ac
    ac_key = 'िवधान सभा क्षे की संख्या, नाम व आरक्षण िथित'
    ac = ''.join(re.findall(ac_key + '.*?\n\n(.*?)\n', text, re.DOTALL)).strip()

    pc_key = '1 पुनरीक्षण का िववरणः'
    try:
        pc = ''.join(re.findall('.*?\n\n' + pc_key, text, re.DOTALL)).strip()
        pc = pc.split('\n')
        pc = ' '.join(pc[-4:-2])
    except:
        pc = ''

    # Year
    year = re.findall('\d+', text)[0]

    # Stats
    nums = 'पुष\n\n'
    try:
        nums = re.findall(nums + '.*?(\d+).*?(\d+).*?(\d+)', text, re.DOTALL)[0]
    except:
        nums = ('','','')

    return {
        "ac_name": ac,
        "parl_constituency": pc,
        'part_no': part_number,
        'year': year,
        'state': STATE,
        'file_name': fn, 
        'main_town': mandal_values[-8],
        'revenue_division': mandal_values[-7],
        'police_station': mandal_values[-5],
        #'post_office': mandal_values[-4],
        'mandal': mandal_values[-3],
        'district': mandal_values[-2],
        'pin_code': mandal_values[-1],
        "polling_station_name": psn, 
        "polling_station_address": psa,
        "net_electors_male": nums[0],
        "net_electors_female": nums[1], 
        "net_electors_third_gender": '', 
        "net_electors_total": nums[2]
    }


def filter_strip(l):
    r = []
    for i in l:
        if i:
            r.append(i.strip())
    return r

def pdf_to_csv(path, fn):
    rows = [] 

    logging.info(f'Parsing {path}')

    first_page_data = get_first_page_data(path, fn)
    doc = fitz.open(path)
    for i, p in enumerate(doc):

        text = p.get_text()

        if i < 2:
            continue
        
        boxes = text.split('मकान संख्या')
        if len(boxes) > 1:
            for i, b in enumerate(boxes):
                bs = b.split('\n')
                bs = filter_strip(bs)

                # Format first one
                if i == 0:
                    bs = bs[-9:]

                if len(bs) > 8 < 12:
                    if re.match('\d+', bs[-1]):
                        rows.append({
                            'number': bs[-1],
                            'id': bs[-2],
                            'elector_name': bs[-6].split(':')[-1],
                            'father_or_husband_name': bs[-5].split(':')[-1],
                            'house_no': bs[-8],
                            'age': bs[-3],
                            'sex': bs[-4],
                            'supplementary': ''
                        })

                    elif re.match('\d+', bs[-3]):
                        if len(bs) == 11:
                            bs = bs[-9:]

                        if re.match('\w+\d+', bs[-4]):
                            if re.match('\d', bs[0]):
                                rows.append({
                                    'number': bs[-3],
                                    'id': bs[-4],
                                    'elector_name': bs[1].split(':')[-1],
                                    'father_or_husband_name': bs[2].split(':')[-1],
                                    'house_no': bs[0],
                                    'age': bs[-5],
                                    'sex': bs[3],
                                    'supplementary': 'yes'
                                })
                            else:
                                rows.append({
                                    'number': bs[-8],
                                    'id': bs[-4],
                                    'elector_name': bs[-7].split(':')[-1],
                                    'father_or_husband_name': bs[-6].split(':')[-1],
                                    'house_no': bs[-3],
                                    'age': '',
                                    'sex': '',
                                    'supplementary': 'yes'
                                })

                        elif re.match('\d+', bs[-3]):
                            rows.append({
                                'number': bs[-8],
                                'id': bs[-2],
                                'elector_name': bs[-6].split(':')[-1],
                                'father_or_husband_name': bs[-5].split(':')[-1],
                                'house_no': bs[-7],
                                'age': bs[-3],
                                'sex': bs[-4],
                                'supplementary': 'yes'
                            })

    # Add data to row
    [row.update(first_page_data) for row in rows]

    df = pd.DataFrame(rows)
    df.to_csv(f'{OUTPUT_PATH}/{fn}.csv')


def main():
    logging.info(f'Parsing {INPUT_PATH}')
    paths = [f'{INPUT_PATH}{x}' for x in os.listdir(INPUT_PATH)]

    for path in paths:
        if path.endswith('pdf'):
            fn = path.split('/')[-1].split('.pdf')[0]
            if fn + '.csv' not in os.listdir(OUTPUT_PATH):
                pdf_to_csv(path, fn)

    logging.info('Done')

if __name__ == '__main__':
    main()