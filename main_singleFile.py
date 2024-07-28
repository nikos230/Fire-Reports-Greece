import tabula
import pandas as pd
import numpy as np
import os
from pyrosvestiki import DeltiaFire
# To A/A einai me ellinika grammata

def extract_tables_from_pdf(pdf_path):
    # get tables from pdf with tabula OCR
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables

def save_tables_to_excel(tables, excel_path):
    merged_tables = pd.concat(tables, ignore_index=True)
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        merged_tables.to_excel(writer, index=False)
    return 0



def main():
    pdf_path = 'Δελτίο Σοβαρών Δασικών 22-07-2024.pdf'
    excel_path = pdf_path.replace('.pdf', '') + '.xlsx'

    # pernoume tous pinakes apo to arxeio .pdf kai ta bazoume se ena DataFrame
    tables = extract_tables_from_pdf(pdf_path)
    # Orizoume ena oject typou pyrosvestiki kai bazoume mesa ta DataFrames
    deltio = DeltiaFire(tables)
    # kanoume oti tropopoisi xreiazete sto DataFrame (vlepe pyrosvestiki.py)
    tables = deltio.get()
    # apothikeusi kathe deltiou 3exorista
    deltio.save_to_excel(tables, excel_path)

    # dimiourgia neou arxeiou excel me ta entrys tou deltiou (raw data)
    #save_tables_to_excel(tables, excel_path)
    #print("To neo Deltio Sothike me onoma :", excel_path)


if __name__ == "__main__":
    main()
