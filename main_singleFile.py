import tabula
import pandas as pd
import numpy as np
import os
from pyrosvestiki import DeltiaFire
# To A/A einai me ellinika grammata


def save_tables_to_excel(tables, excel_path):
    merged_tables = pd.concat(tables, ignore_index=True)
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        merged_tables.to_excel(writer, index=False)
    return 0



def main():
    pdf_path = './pdf_Data/Δελτίο Σοβαρών Δασικών 22-07-2024.pdf'
    excel_path = './' + pdf_path.replace('.pdf', '').replace('pdf_Data/', '') + '.xlsx'

    # Orizoume ena oject typou pyrosvestiki kai bazoume mesa ta DataFrames
    # pernoume tous pinakes apo to arxeio .pdf kai ta bazoume se ena DataFrame
    deltio = DeltiaFire(pdf_path)
    # kanoume oti tropopoisi xreiazete sto DataFrame (vlepe pyrosvestiki.py)
    tables = deltio.get()
    # apothikeusi kathe deltiou 3exorista
    deltio.save_to_excel(tables, excel_path)

    # dimiourgia neou arxeiou excel me ta entrys tou deltiou (raw data)
    #save_tables_to_excel(tables, excel_path)
    #print("To neo Deltio Sothike me onoma :", excel_path)


if __name__ == "__main__":
    main()
