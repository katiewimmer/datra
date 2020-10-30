import pandas                                                                                                                                    
import numpy as np # adapted this from a tutorial, need to figure out how to make this work for actual datasets, also need to visualize           
import random                                                                                                                                    
                                                                                                                                                 
feature = 'feature' # name of feature column                                                                                                     
predict_col = 'prediction' # name of prediction column                                                                                            
features = ['A', 'B', 'C', 'D'] # different groups that are part of the data, each data point is from one group                                   
                                                                                                                                                 
A_percent = 40 # percentage of the population that is from A, B, C, or D                                                                          
B_percent = 20                                                                                                                                   
C_percent = 15                                                                                                                                   
D_percent = 25                                                                                                                                   
                                                                                                                                                 
A_pos =  30 # percentage of outcomes for each group that are favorable                                                                            
B_pos = 20                                                                                                                                       
C_pos = 20                                                                                                                                       
D_pos = 15                                                                                                                                       
                                                                                                                                                 
group_set = [features[0]] * A_percent + [features[1]] * B_percent + [features[2]] * C_percent + [features[3]] * D_percent # set of groups (As, Bs,
A_set = [1] * A_pos + [0] * (100-A_pos) # outcome set (1s and 0s)                                                                                
B_set = [1] * B_pos + [0] * (100-B_pos)                                                                                                          
C_set = [1] * C_pos + [0] * (100-C_pos)                                                                                                          
D_set = [1] * D_pos + [0] * (100-D_pos)                                                                                                          
                                                                                                                                                 
group_pred = [] # list storing predictions for each group                                                                                        
for i in range(0, 100):                                                                                                                          
   rand_group = random.choices(group_set)[0]                                                                                                     
   if rand_group == 'A':                                                                                                                         
       pred = random.choices(A_set)[0]                                                                                                           
       group_pred.append(['A', pred])                                                                                                            
   elif rand_group == 'B':                                                                                                                       
       pred = random.choices(B_set)[0]                                                                                                           
       group_pred.append(['B', pred])                                                                                                            
   elif rand_group == 'C':                                                                                                                       
       pred = random.choices(C_set)[0]                                                                                                           
       group_pred.append(['C', pred])                                                                                                            
   else:                                                                                                                                         
       pred = random.choices(D_set)[0]                                                                                                           
       group_pred.append(['D', pred])                                                                                                            
                                                                                                                                                 
df = pandas.DataFrame(group_pred,columns=['feature','prediction'])                                                                               
df_group = (df.groupby([feature])[predict_col].value_counts() / df.groupby([feature])[predict_col].count()) # calculate probability for each group
print(df_group)                                                                                                                                  
                                                                                                                                                 
                                                                                                                                                 
