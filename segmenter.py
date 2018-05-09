import csv
import re
import sympy
from sympy.abc import pi


pi_symbol=sympy.pretty(pi)


DATA_PATH="/home/tapojit/Desktop/NLP/stac-linguistic-2018-03-21/data/"

pilot_csv_path=DATA_PATH+"pilot_spect/pilot01/unsegmented/pilot01.soclog.csv"


EDU=[]
AGENT_HEAD=[]
def segmentation(): 
    with open(pilot_csv_path) as fp:
        reader=csv.reader(fp, delimiter="\t")
        not_first_row=False
        for row in reader:
            agent=row[2]
            if(not_first_row and agent!="Server"):
                
                conv=row[5]
                
                #    https://regex101.com/r/nG1gU7/27
                agent_dialogue_start=True
                sentences=re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', conv)
                for sentence in sentences:
                    
                    edu_list=re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\,|\;)\s', sentence)
                    
                    for discourse_unit in edu_list:
                        
                        EDU.append(discourse_unit)
                        
                        if(agent_dialogue_start):
                            agent_dialogue_start=False
                            AGENT_HEAD.append(agent)
                        else: AGENT_HEAD.append(" ")
                    
                
            not_first_row=True
        
def print_EDUs():
    d_u_id=0       
    for d_u, agent in zip(EDU, AGENT_HEAD):
        print "%s\t%s%d) "%(agent, pi_symbol, d_u_id),
        print '%s' % d_u
        
        d_u_id+=1
        
    

if __name__=='__main__':
    segmentation()
    print_EDUs()
    