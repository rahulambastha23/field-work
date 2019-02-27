import requests
ar=[2,3,4,5,6,7]
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=ar&language=english&route=p&numbers=8770631461"
headers = {
'authorization': "APBJf5rZFGS9UCw41xLmWzElyRucQ8q7dsYIvKtp2nVb6HXeDgdcHnIRqLfDjAFmazyJxrSKZ0s5Xip2",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
