import json 
f = open("demofile2.txt", "a")
f.write("Now the file has more content!") 
  
# function to add to JSON 
def write_json(data, filename='demofile2.txt'): 
    with open(filename,'a') as f: 
        json.dump(data, f, indent=4) 
      
      
with open('demofile2.txt') as json_file: 
    data = json.load(json_file) 
      
    temp = data['emp_details'] 
  
    # python object to be appended 
    y = {"emp_name":'Nikhil', 
         "email": "nikhil@geeksforgeeks.org", 
         "job_profile": "Full Time"
        } 
  
  
    # appending data to emp_details  
    temp.append(y) 
      
write_json(data)
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


f.close()

