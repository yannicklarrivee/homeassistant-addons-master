import requests
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])

#variable
APIusername = sys.argv[1]
APIpassword = sys.argv[2]
DID = sys.argv[3]
DST = sys.argv[4]
message = sys.argv[5]
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
#Sum = 0
# Using argparse module
# for i in range(1, n):
#     Sum += int(sys.argv[i])
     
# print("\n\nResult:", Sum)

url = "https://voip.ms/api/v1/rest.php?api_username=" + APIusername + "&api_password=" + APIpassword + "&method=sendSMS&did=" + DID + "&dst=" + DST + "&message=" + message

print(url)

payload = {}
headers = {
  'Cookie': 'PHPSESSID=bu2vmnp38uj5p33a9ge88lpoo4; __cf_bm=JOv5X5abAPlPapzSOdWwj3jbrp0lI5RmoCz2WrsGxvw-1692986737-0-AXIdAxN6XIX7ihHi/SSAT2/wX3dfCwe3d/QmaSQ8NUXSoVJ+CvdPJ/j3OI5k7UuZ3qI+pVns/Bv7W8gpId3GYsc=; voipms_lang=fr%7Ccp'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

