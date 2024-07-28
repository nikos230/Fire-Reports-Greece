# Fire Reports Greece
Get Excel Table data from PDF reports from Greece Fire Department

# Features
* Excel File from PDF document
* Excel 'Database', insert new PDF Report and Update old entrys

# How to Use
First get pyrosvestiki.py and main_singleFile.py or main_multipleFiles.py to the same folder then create a Folder named 'pdf_Data' which will contain all PDF Documents and a Excel Output older named 'excel_output' which will store all new Excel files created. You can rename the folders from main scripts.
**1.** Create folder '**pdf_Data**' and put all PDF document you have from Fire Department
**2.** Create folder '**excel_outpu**t' to store all new excel files
(Cory folders from repo if you do not want to create them)
**3.** Run **main_multipleFiles.py** if you want to process all PDF document from pdf_Data folder
**4.** Alternatively run **main_singleFile.py** and input the PDF document name in the script to process only one PDF document

# Examples
* **Input Data**, Δελτίο Σοβαρών Δασικών 22-07-2024.pdf 
![plot](https://github.com/nikos230/Fire-Reports-Greece/blob/main/images/fire_table.png?raw=true)

* **Output Data**, Δελτίο Σοβαρών Δασικών 22-07-2024.xlsx
![plot](https://github.com/nikos230/Fire-Reports-Greece/blob/main/images/excel_output.png?raw=true)
