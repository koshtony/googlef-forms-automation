# googlef-forms-automation
automating filling google forms

### install the requirements

run command : pip install -r requirements.txt

### replace data file in the folder:
  
  Rename new date file  to Data.csv
  
   or change script to the name of your file;

   data= open("Data.csv") -> data= open("yourfilename.csv")

### run the script/code

   python fill_form.py 

   nb: run inside the folder (form_auto)

### chromedriver  (unhash the relevant in the script)

   chrome = webdriver.Chrome(service=Service("./chromedriver"))  #linux

   chrome = webdriver.Chrome(service=Service("chromedriver.exe")) # windows

   #or depending on your chromedriver path

   chrome = webdriver.Chrome(service=Service(path))
