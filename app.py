

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from ImageNotes import ImageNote
# from main import TypePrediction, segment_image,saveResult
from main  import predictImage


# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To KeVan Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_crack(data:ImageNote):
    data = data.dict()
    img=data['image']
    result= predictImage(img)
    # pred= TypePrediction(img)
    # image_base64= segment_image(img)

    # # print(pred)
    # if(pred>0.5):
    #     type="Have crack"
    # else:
    #     type="Have no crack"

    # result= {
    #     'date': str(datetime.datetime.now()),
    #     'original_image':img,
    #     'prediction': pred,
    #     'type': type,
    #     'segment_image': image_base64
    # }

    # print(result)
    # # saveResult(result)     ## save input and output result in mongodb database Atlas
    # url = "https://ap-southeast-1.aws.data.mongodb-api.com/app/data-wlatu/endpoint/data/v1/action/insertOne"
    # payload = json.dumps({
    # "collection": "fault_detection",
    # "database": "thesis",
    # "dataSource": "Cluster0",
    # "document": {'date':result['date'], 'original_image': result['original_image'], 'prediction': result['prediction'],'type':result['type'], 'segment_image':result['segment_image']}
    # })
    # headers = {
    # 'Content-Type': 'application/json',
    # 'Access-Control-Request-Headers': '*',
    # 'api-key': 'LFyT8MWcEraGxtCsMJpceBO8q72WLX8mInon25j6kbVCgv2j5vSwVYzNVzdxFsqh', 
    # }

    # response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    
    return {
        'prediction': str(result['prediction']),
        'type': result['type'],
        'image': result['segment_image']
    }

    # return {
    #     'prediction': str(pred)
    # }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
