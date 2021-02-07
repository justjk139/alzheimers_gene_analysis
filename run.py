#!/usr/bin/env python
# coding: utf-8

import sys
import json
import os

sys.path.insert(0, 'src') #getting the directory of our etl file in order to import etl since it is in a different folder
from etl import get_file_names, shorten_data, create_path
#from all_pipeline import fastqc
from test_pipeline import test_kallisto, test_fastqc
from utils import function_to_convert_notebook, function_to_convert_notebook_test


def main(targets):
    
    if 'all' in targets:
        # HERE is where we run the FULL PIPELINE
        print("This is a placeholder for now")
        
    if 'data' in targets:
        #doing our data retrieval
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
            get_file_names(**data_cfg)
        print("This is a placeholder for now")
      
    if 'eda' in targets:
        # HERE is where EDA will be implemented
        with open('config/eda-params.json') as fh:
            eda_cfg = json.load(fh)
            function_to_convert_notebook(**eda_cfg)
    
    if 'test' in targets:
        
        print("\n\nTest is now running\n")
        
        with open('config/test-params.json') as fh:
            test_cfg = json.load(fh)
            print("Creating path from inside Main:")
            create_path(**test_cfg)
        
            print("shortening the data from inside Main:")
            fq_1, fq_2 = shorten_data(**test_cfg)
            
            #fastqc:
            print("running fastqc from main:")
            pass_data, cut_data = test_fastqc([fq_1,fq_2])
            print(pass_data)
            
            # kallisto:
            test_kallisto(pass_data)
            
            #generating the report here:
            with open('config/eda-params.json') as fh:
                eda_cfg = json.load(fh)
                function_to_convert_notebook_test(**eda_cfg)
            
            print("Success!")
        print("\n\nTest finished running\n\n")
    return

# In[ ]:


if __name__ ==  '__main__':
    targets = sys.argv[1:]
    main(targets)