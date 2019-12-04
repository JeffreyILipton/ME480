
# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://localhost:5000/todo/api/v1.0/tasks"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
print(data)


