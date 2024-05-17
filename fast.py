from fastapi import FastAPI
import requests
import pprint
import json

# url 입력

# url 불러오기
#데이터 값 출력해보기

# print(pp.pprint(json_ob))

app = FastAPI()

@app.get("/{item}") 
async def root(item: int):
    response = requests.get(f'http://apis.data.go.kr/5050000/touristDestinationService/getTouristDestination?serviceKey=tussmhxuu1xAlRv9cJ9NQP8LtOwmZjojrJeUaGLT6sI0jd91wXKCsuR4Yak8I08mDILJw17m2HRvvjXJNYzNnQ%3D%3D&pageNo={item}&numOfRows=20')
    contents = response.text
    json_ob = json.loads(contents)
    body = json_ob['response']['body']['items']['item']
    return body

