# pandas для обработки табличных данных
# conda install pandas
# conda install openpyxl
import pandas as pd
import os

def char_clean(s):
    s = str(s) 
    new_s = '' 
    for i in s:
        if i.isdigit() is True:
            new_s += i 
        else:
            pass  
    return new_s 

PATH = f'{os.getcwd()}/phone_numbers.xlsx'
NEWFILE_PATH = f'{os.getcwd()}/clean_phone_numbers.xlsx'

excel_df = pd.read_excel(PATH, sheet_name='Worksheet')

phone_list = excel_df['phone_number'].values.tolist()
clean_phone_list = [] 
phone = ''

for i in range(len(phone_list)):
    phone = phone_list[i] 
    new_phone = char_clean(phone)  
    clean_phone_list.append(new_phone) 

print('\n', '*'*77, '\nВот ваш результат:\n')
print(clean_phone_list)


new_df = pd.DataFrame(clean_phone_list, columns =['phones'])
new_df.to_excel(NEWFILE_PATH, sheet_name='clean_numbers', index=False)