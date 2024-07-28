import grpc
import agronomy_pb2 as pb2
from agronomy_pb2_grpc import AgronomyServiceStub
from google.protobuf import json_format

class GRPCClient:
    def __init__(self, host: str, port: int):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = AgronomyServiceStub(self.channel)

    def serve_recommend_micronutrient(self):
        soil_test_value = pb2.SoilTestValue(nutrient="mn", value=1)
        request = pb2.MicroNutrientRequest(
            crop="corn", yield_goal=110, soil_test_values=[soil_test_value]
        )
        try:
            response = self.stub.RecommendMicroNutrient(request)
        except grpc.RpcError as rpc_error:
            return rpc_error
        else:
            return json_format.MessageToDict(response, pb2.MicroNutrientRecommendationResponse()).get("recommendations")

    def serve_recommend_nutrient(self):
        request = pb2.NutrientRequest(
            country="US",
            state_or_province="IN",
            soil_texture="CLAY",
            crop="corn",
            yield_goal=1.1,
            soil_cec=3.3,
            soil_organic_matter=7,
            previous_crop="corn",
            previous_yield=5,
            soil_test_values=[],
        )
        try:
            response = self.stub.RecommendNutrient(request)
        except grpc.RpcError as rpc_error:
            return rpc_error
        else:
            return json_format.MessageToDict(response, pb2.NutrientRecommendationResponse()).get("recommendations") 

    def serve_recommend_mrtn(self,corn_price:str,n_price:str):
        request = pb2.MRTNRequest(
            state_or_province="IL",
            region="north",
            rotation="corn_corn",
            corn_price=float(corn_price),
            n_price=float(n_price),
        )
        try:
            print("request", request)
            response = self.stub.RecommendMRTN(request)
        except grpc.RpcError as rpc_error:
            return rpc_error
        else:
            return json_format.MessageToDict(response, pb2.MRTNRecommendationResponse()) 


    # def get_micro_nutrient_options(self,request):
    #     try:

    #         response = self.stub.GetMicroNutrientOptions(pb2.google_dot_protobuf_dot_empty__pb2)
    #     except grpc.RpcError as rpc_error:
    #         return rpc_error
    #     else:
    #         print(response)
    #         return json_format.MessageToDict(response, pb2.MicroNutrientOptionsResponse())

    # def get_nutrient_options(self):
    #     try:
    #         response = self.stub.GetNutrientOptions(pb2.google_dot_protobuf_dot_empty__pb2)
    #     except grpc.RpcError as rpc_error:
    #         return rpc_error
    #     else:
    #         return json_format.MessageToDict(response, pb2.NutrientOptionsResponse()).get("nutrients")    

    # def get_nutrient_crop_yield_units(self):
    #     try:
    #         response = self.stub.GetNutrientCropYieldUnits(pb2.google_dot_protobuf_dot_empty__pb2)
    #     except grpc.RpcError as rpc_error:
    #         return rpc_error
    #     else:
    #         return json_format.MessageToDict(response, pb2.NutrientCropYieldUnitsResponse()).get("crop_yield_units")

    # def get_nutrient_sample_test_methods(self):
    #     try:
    #         response = self.stub.GetNutrientSampleTestMethods(pb2.google_dot_protobuf_dot_empty__pb2)
    #     except grpc.RpcError as rpc_error:
    #         return rpc_error
    #     else:
    #         return json_format.MessageToDict(response, pb2.NutrientSampleTestMethodsResponse()).get("sample_test_methods")        

    # def get_nutrient_soil_textures(self):
    #     try:
    #         response = self.stub.GetNutrientSoilTextures(pb2.google_dot_protobuf_dot_empty__pb2)
    #     except grpc.RpcError as rpc_error:
    #         return rpc_error
    #     else:
    #         return json_format.MessageToDict(response, pb2.NutrientSoilTexturesResponse()).get("soil_textures")
        
    # def get_regions(self):
    #     try:
    #         response = self.stub.GetRegions(pb2.google_dot_protobuf_dot_empty__pb2)
    #     except grpc.RpcError as rpc_error:
    #         return rpc_error
    #     else:
    #         return json_format.MessageToDict(response, pb2.RegionResponse()).get("regions")

    # def get_rotations(self):
        try:
            response = self.stub.GetRegions(pb2.google_dot_protobuf_dot_empty__pb2)
        except grpc.RpcError as rpc_error:
            return rpc_error
        else:
            return json_format.MessageToDict(response, pb2.RotationResponse()).get("rotations")