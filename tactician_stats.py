import pandas as pd    
import os
import Tactician_move
'''
bench_list = ["theories/Numbers/HexadecimalNat.bench", 
"theories/Logic/Hurkens.bench", "theories/Reals/PartSum.bench"]

for i in range(len(bench_list)):

    f = open(bench_list[i])
    lines = f.readlines()

    successful_proof_num = 0

    for line in lines:
        line = str.split(line)
        if len(line) > 2:
            successful_proof_num += 1
    f.close()

print (successful_proof_num)
'''

  
# bench_dir = '/home/zhangliao/Desktop/Tactician_stats/length-3/'


successful_proof_num = 0
for root, dirs, files in os.walk(Tactician_move.dest_dir):  
    for file in files:  
        if file.endswith('.bench'): 
            #print(file)
            f = open(root + file)
            lines = f.readlines()
            for line in lines:
                line = str.split(line)
                if len(line) > 2:
                    successful_proof_num += 1
            f.close()
print (successful_proof_num)





'''
import os 
for root, dirs, files in os.walk('./'):   
    for file in files:   
        if file.endswith('.bench'):  
                correct_file = file[7:] 
                # print(root + 'length-3/' + correct_file)  
                print(correct_file) 
'''