# nlp_data_generation

1. Create a python environment in Windows using the following steps:

    -  First install virtual environment by writing the command in the Windows command shell	
       
       pip install virtualenv

    -  Now go to the project location using cd command
    
    -  Once reached in the project location write the command
       
       virtualenv env
    
    -  Now a batch file will be created for Windows user
       
       \env\Scripts\activate.bat
	
2. Activate the environment
    
    source env/bin/activate on unix or
    nlpenv\Scripts\activate.bat
    
    Source_path_to_env\Scripts\activate.bat on windows where Source_path_to_env is the path in the form of 'C:\Users\'Username'\venv'
    
3. Install all the requirements from the requirement.txt file to install all the dependencies
	
    pip install -r requirements.txt 


If you add any new packages to the project, you might need to update the requirement files. Please follow the steps:

    -   pip freeze > requirements.txt

    -   Push it to git


How to run the code - step by step:

1. First add all you text data into input/data_text.txt file
2. Then run code/text2xml.py file
3. Then run code/xml-to-csv.py file
4. Then run code/dataset_generation_new.py file to generate output/train.csv and output/val.csv files
5. Then run code/convert_wingrad_to_swag.py file to generate output/test.csv file.
6. Then upload the train, test, val files in to swag folder into collab.
7. Then run the collab file. 
