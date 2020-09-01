import requests
import os
# print(os.path.curdir)
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': 'https://www.remove.bg/example.jpg',
        'size': 'auto'
    },
    headers={'X-Api-Key': 'Z5RBRe6Yox8m38S9TFCwa32Z'},
)
print(response.status_code, requests.codes.ok, not requests.codes, (requests.codes), sep = '\n')
if response.status_code == requests.codes.ok:
    if not os.path.isdir(os.path.curdir + r"\downloads"):
        os.mkdir(os.path.curdir +r"\downloads")
    with open(r'{}\downloads\haan-bg.png'.format(os.path.curdir), 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)