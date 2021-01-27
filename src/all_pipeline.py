#!/usr/bin/env python
# coding: utf-8



import os


def clean_data(file_names):
    files_cleaned = [i for i in file_names if '.fastq' in i]
    files_cleaned.sort()
    return files_cleaned


# In[5]:


def fastqc(files_cleaned):
    pass_data = [] #creating array that will hold name of passing data
    fail_data = [] #creating array that will hold name of not passing data
    # changing dir to mine so I can create a folder 
    for i in files_cleaned:
        print(i)
        os.chdir('..')
        os.chdir('/datasets/home/40/840/r1cummin/DSC180A-Checkpoint-03')
        print("making dir")
        os.system('mkdir fastq_out')
        print("running fastqc...")
        os.system('/opt/FastQC/fastqc /datasets/srp073813/'+i+' --extract --outdir=fastq_out/')
        print("Fastqc finished")
      
        print("Opening file")
        with open('fastq_out/'+i[0:-3].replace('.','_')+'c/fastqc_data.txt') as f:
            first_line = f.readlines()[1]
        print("Seeing if pass in file... then adding to array")
        if 'pass' in first_line:
            pass_data.append(i)
        else:
            fail_data.append(i)
        print("Now deleting dir in order so that we can do the next iteration:")
        os.system('rm -rf fastq_out')
    return pass_data, fail_data


# In[6]:


def cutadapt(pass_data):
    initial = 0
    cut_fastq_files = []
    print("making tmp dir")
    os.system('mkdir cutadapt_tmp')
    for i in range(int(len(pass_data)/2)):
        print("Starting cutadapt:")
        os.system('cutadapt -a AACCGGTT -A AACCGGTT -o cutadapt_tmp/'+pass_data[initial][0:-11]+'.1.fastq.gz -p cutadapt_tmp/'+pass_data[initial+1][0:-11]+'.2.fastq.gz /datasets/srp073813/'+pass_data[initial]+' /datasets/srp073813/'+pass_data[initial+1]+' --cores=32')
        cut_fastq_files.append(str(pass_data[initial][0:-11])+'.1.fastq.gz')
        cut_fastq_files.append(str(pass_data[initial+1][0:-11])+'.2.fastq.gz')
        print("cutadapt finished on this pair, starting on next pair:")
        initial = initial + 2
    print("cutadapt finished in its entirety")
    return cut_fastq_files


# In[7]:


def second_fastqc(cut_fastq_files):
    # reRunning the cutadapt files through fastqc


    pass_cut_data = [] #creating array that will hold name of passing data
    fail_cut_data = [] #creating array that will hold name of not passing data

    print('Getting name of cutadapt files')
    os.chdir('tmp')
    cut_fastq_files = os.listdir()

    for i in cut_fastq_files:
        print(i)
        os.chdir('..')
        print("making dir...")
        os.system('mkdir cut_fastq_out')
        print("running fastqc...")
        os.system('/opt/FastQC/fastqc tmp/'+i+' --extract --outdir=cut_fastq_out/')
        print("Fastqc finished")
        
        print("Opening file")
        with open('cut_fastq_out/'+i[0:-3][::-1].replace('.','_',1)[::-1]+'c/fastqc_data.txt') as f:
            cut_first_line = f.readlines()[1]
        print("Seeing if pass in file... then adding to array")
        if 'pass' in cut_first_line:
            pass_cut_data.append(i)
        else:
            fail_cut_data.append(i)
        print("Now deleting dir in order so that we can do the next iteration:")
#         os.chdir('..')
#         os.chdir('/datasets/home/40/840/r1cummin/DSC180A-Checkpoint-02')
        os.system('rm -rf cut_fastq_out')
    return pass_cut_data, fail_cut_data


# In[9]:


def kallisto(pass_cut_data):
    initial = 0
    print("Making dir for Kallisto Output after test:")
    os.system("mkdir kallisto_tmp")
    for i in range(int(len(pass_cut_data)/2)):
        print("Running Kallisto:")
        os.system("/opt/kallisto_linux-v0.42.4/kallisto quant -i /datasets/srp073813/reference/kallisto_transcripts.idx -o kallisto_tmp/kallisto_output_"+pass_cut_data[i][0:10]+" -b 0 "+pass_cut_data[initial]+" "+pass_cut_data[initial+1]+" -t 10")
        initial = initial + 2
    print("Kallisto successfully ran")
    print("Moving the data to data/out/")
    os.system("mkdir out")
    os.system("mv out data")
    os.system("mv kallisto_tmp data/out")
    return