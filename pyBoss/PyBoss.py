
import os
import csv 

file = 'employee_data1.csv'
abrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',
}
ssn = []
firstname = []
lastname = []
dob =[]
employer_id = []
state = []

with open(file, 'r') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        employer_id.append(row['Emp ID'])
        firstname.append(row['Name'].split(" ")[0])
        lastname.append(row['Name'].split(" ")[1])
        dob.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        ssn.append('***-**-' + row['SSN'].split('-')[2])
        state.append(abrev[row['State']])
        

new_data = zip(employer_id, firstname, lastname, dob, ssn, state)

output_file = 'Output.csv'

with open(output_file, 'w') as csvwrite:
    newfile = csv.writer(csvwrite, delimiter = ",")
    newfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    newfile.writerows(new_data)