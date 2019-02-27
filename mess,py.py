import requests

url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=hellobrother&language=english&route=p&numbers=9340284683,9171039045,9340793983,8770631461"
headers = {
'authorization': "9ghEGQ3pI8FquHZo5lMi2XtJK07x6AndPVevjYNfDBkmsCzULb5q3sBDuHIo29hQRUbNJXr1S4FwmzAg",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
