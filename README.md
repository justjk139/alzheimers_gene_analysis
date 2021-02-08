# DSC180B_Capstone_Project
Ryan Cummings,
Gregory Thein,
Justin Kang,
Prof. Shannon Ellis,
Code Artifact Checkpoint

#### In this you will find our Checkpoint Code, We are in the B04 Genetics domain and this is our Capstone Project. For our Capstone Project we are looking at Alzheimer's Diseased Patient's Blood miRNA Data. Our Pipeline functions are seen in the all_pipeline.py file. Running the full pipeline takes multiple hours to run and implements the tools in our Genetics Pipeline (FastQC, CutAdapt, Kallisto, DESeq2). Our project implements both python and R to perform successful analysis on our dataset of blood based miRNA in which we find miRNAs with significantly changed expression level.

#### As of right now only `python run.py test` is implemented but our ultimate goal is to have this as our final README: 
#### Running `python run.py all` will run the full pipeline from scrath, this does take hours and sometimes even days to run, it can be ran from scratch but is not needed to be ran from scratch to see our results! Other keywords that can be passed into the funciton are `test eda data`. Running `python run.py test` is actually the most recommended one, this gives you the full pipeline experience on a fraction of the data, running in just a few minutes. The code can also be ran with `python run.py data` or `python run.py eda` or a combination of these: `python run.py data eda`.  We also printed steps along the way to notify the user what is currently running in the pipeline. Our code assumes it is ran on the DSMLP Servers! Without running on the DSMLP Servers we would not be able to access the data, which is why it is important to be connected to the server. The EDA parameter will start the EDA process, in our case we are making the report with the sample data explained above and plotting some figures, then later actually show the data that we got after the complete pipeline was ran. 

#### Our repo consists of 5 folders, and 3 files (a .gitignore, the README, and the run.py). The 5 folders consist of: config, notebooks, references, data and src. Inside config is our data-params.json file, eda-param.json file, and test-params.json. These files specifies the data-input locations/file path that is necessary for this Checkpoint's data retrieval, and the eda-params file specifies the input and output of the report generated by the `eda` call, while the test-params has the names of the samples that we run the `test` keyword argument on. Notebooks folder consists of some of our .ipynb files that we used just for testing and will and as a dev tool (to see what we did along the way). References has our SRARunTable and may contain other future references for the project. The data folder is where we created the symlink between our folder and the dataset on DSMLP. The data folder will also consist of the data/out information once the `test` keyword is ran, specifically the output from Kallisto is stored here. The contents of our src folder contains our etl.py file, eda.py file, utils.py file, test_pipeline.py, and all_pipeline.py. Our etl.py file is where our file is extracting the dataset from the DSMLP's /teams dataset. Utils.py is where we created a function that turns a notebook into an HTML format, which then outputs that HTML file as a report. test_pipelinea and all_pipeline contain the pipeline that is created for our project, varying slightly since test is only ran on a portion while all is ran on the entire dataset!
