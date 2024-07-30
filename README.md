# Fire Reports Greece
Get Excel Table data from PDF reports from Greece Fire Department

# Features
* Generate Excel File from PDF document
* Generate and Update Excel 'Database', insert new PDF Report and Update old entrys

# How to Run
First get pyrosvestiki.py and main_singleFile.py or main_multipleFiles.py to the same folder then create a Folder named 'pdf_Data' which will contain all PDF Documents and a Excel Output older named 'excel_output' which will store all new Excel files created. You can rename the folders from main scripts.<br /><br />
**1.** Create folder '**pdf_Data**' and put all PDF document you have from Fire Department<br />
**2.** Create folder '**excel_outpu**t' to store all new excel files<br />
(Cory folders from repo if you do not want to create them)<br />
**3.** Run **main_multipleFiles.py** if you want to process all PDF document from pdf_Data folder<br />
**4.** Alternatively run **main_singleFile.py** and input the PDF document name in the script to process only one PDF document<br />

# How to Use
Make use of class DeltiaFire from pyrosvestiki.py<br />
```from pyrosvestiki import DeltiaFire```<br /><br />
Define an DeltiaFire Object and give the tables we have extracted<br />
```deltio = DeltiaFire(os.path.join(pdf_path_folder, file))``` for multiple PDF<br />
```deltio = DeltiaFire(pdf_path)``` for single PDF<br /><br />
We run .get() function from DeltiaFire to fix the table<br />
```tables = deltio.get()```<br /><br />
Now we can save the table extracted from the PDF to a excel file alone<br />
```deltio.save_to_excel(tables, excel_path)```<br /><br />
Or we can make a database and save it there and update with every new PDF we process<br />
```deltio.save_to_database(tables, database_path)```<br />


# Examples
* **Input Data**, Δελτίο Σοβαρών Δασικών 22-07-2024.pdf 
![plot](https://github.com/nikos230/Fire-Reports-Greece/blob/main/images/fire_table.png?raw=true)

* **Output Data**, Δελτίο Σοβαρών Δασικών 22-07-2024.xlsx
![plot](https://github.com/nikos230/Fire-Reports-Greece/blob/main/images/excel_output.png?raw=true)
