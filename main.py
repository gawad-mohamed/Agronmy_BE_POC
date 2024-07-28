from fastapi import FastAPI, HTTPException,Body
from grpc_client import GRPCClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
grpc_client = GRPCClient(host="localhost", port=50051)

ORIGINS = [
    "http://localhost:5056",
    "localhost:5173",
    "localhost:5056",
]
ALLOW_CREDENTIALS = False
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS
)

@app.post("/recommend_micronutrient/")
async def recommend_micronutrient():
    try:
        result = grpc_client.serve_recommend_micronutrient()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/recommend_nutrient/")
async def recommend_nutrient():
    try:
        result = grpc_client.serve_recommend_nutrient()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/recommend_mrtn/")
async def recommend_mrtn(corn_price:str= Body(..., embed=True),n_price:str= Body(..., embed=True)):
    try:
        print("corn price", corn_price)
        result = grpc_client.serve_recommend_mrtn(corn_price,n_price)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @app.get("/get_micro_nutrient_options/")
# async def get_micro_nutrient_options():
#     try:
#         result = grpc_client.get_micro_nutrient_options()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/get_nutrient_options/")
# async def get_nutrient_options():
#     try:
#         result = grpc_client.get_nutrient_options()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/get_nutrient_crop_yield_units/")
# async def get_nutrient_crop_yield_units():
#     try:
#         result = grpc_client.get_nutrient_crop_yield_units()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/get_nutrient_sample_test_methods/")
# async def get_nutrient_sample_test_methods():
#     try:
#         result = grpc_client.get_nutrient_sample_test_methods()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/get_nutrient_soil_textures/")
# async def get_nutrient_soil_textures():
#     try:
#         result = grpc_client.get_nutrient_soil_textures()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/get_regions/")
# async def get_regions():
#     try:
#         result = grpc_client.get_regions()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/get_rotations/")
# async def get_rotations():
#     try:
#         result = grpc_client.get_rotations()
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8026)
