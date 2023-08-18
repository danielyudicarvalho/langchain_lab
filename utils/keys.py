import os 

# def load_embeddings_keys(embedding_name):
    
#     def aleph():
        
#         aleph_keys = os.getenv('ALEPH_ALPHA_API_KEY')
        
#         return aleph_keys if aleph_keys else False    
#     def openai():
#          openai_key = os.getenv('OPENAI_API_KEY')
         
#          return openai_key if openai_key else False    
   
#     def bedrock():
#         credentials_profile_name = os.getenv('BEDROCK_CREDENTIALS_PROFILE_NAME')
#         region_name = os.getenv('BEDROCK_REGION_NAME')
        
#         return credentials_profile_name, region_name if credentials_profile_name and region_name else False
    
#     def cohere():
#         cohere_api_key = os.getenv('COHERE_API_KEY')
        
#         return cohere_api_key if cohere_api_key else False
        
            
#     def deepinfra():
#         deepinfra_api_key = os.getenv('DEEPINFRA_API_KEY')
        
#         return deepinfra_api_key if deepinfra_api_key else False
    
#     def elasticsearch():
#         es_model_id = os.getenv('ELASTICSEARCH_MODEL_ID')
#         es_cloud_id = os.getenv('ELASTICSEARCH_CLOUD_ID')
#         es_user = os.getenv('ELASTICSEARCH_USER')
#         es_password = os.getenv('ELASTICSEARCH_PASSWORD')
        
#         return es_model_id, es_cloud_id, es_user, es_password if es_model_id and es_cloud_id and es_user and es_password else False
      
#     def minimax():
#        minimax_group_id = os.getenv('MINIMAX_GROUP_ID')
#        minimax_api_key = os.getenv('MINIMAX_API_KEY')
       
#        return minimax_group_id, minimax_api_key if minimax_group_id and minimax_api_key else False    
 
#     def mosaic():        
#         mosaic_api_key = os.getenv('MOSAIC_API_KEY')
        
#         return mosaic_api_key if mosaic_api_key else False
#     def sagemaker():
#         sagemaker_endpoint_key = os.getenv('SAGEMAKER_ENDPOINT_KEY')
#         region_name = os.getenv('SAGEMAKER_REGION_NAME')
        
#         return sagemaker_endpoint_key, region_name if sagemaker_endpoint_key and region_name else False
    
     
    # embedders = {
    #     'aleph': aleph,
    #     'openai': openai,
    #     'bedrock': bedrock,
    #     'cohere': cohere,
    #     'deepinfra': deepinfra,
    #     'elasticsearch': elasticsearch,
    #     'minimax': minimax,
    #     'mosaic': mosaic,
    #     'sagemaker': sagemaker,
    #     'default': True
    # }
    
    # return embedders.get(embedding_name, 'default')()
     
     
def check_keys(func):
    def wrapper(*args, **kwargs):
        keys = load_embeddings_keys(args[0])
        if keys:
            return func(*args, **kwargs)
        else:
            raise Exception('Please provide a valid API key for this embedding')     
     
def load_embeddings_keys(embedding_name):
    def check_env(variables):
        return all(os.getenv(var) for var in variables)

    embedders = {
        'aleph': lambda: os.getenv('ALEPH_ALPHA_API_KEY'),
        'openai': lambda: os.getenv('OPENAI_API_KEY'),
        'bedrock': lambda: (os.getenv('BEDROCK_CREDENTIALS_PROFILE_NAME'), os.getenv('BEDROCK_REGION_NAME')) if check_env(['BEDROCK_CREDENTIALS_PROFILE_NAME', 'BEDROCK_REGION_NAME']) else False,
        'cohere': lambda: os.getenv('COHERE_API_KEY'),
        'deepinfra': lambda: os.getenv('DEEPINFRA_API_KEY'),
        'elasticsearch': lambda: (os.getenv('ELASTICSEARCH_MODEL_ID'), os.getenv('ELASTICSEARCH_CLOUD_ID'), os.getenv('ELASTICSEARCH_USER'), os.getenv('ELASTICSEARCH_PASSWORD')) if check_env(['ELASTICSEARCH_MODEL_ID', 'ELASTICSEARCH_CLOUD_ID', 'ELASTICSEARCH_USER', 'ELASTICSEARCH_PASSWORD']) else False,
        'minimax': lambda: (os.getenv('MINIMAX_GROUP_ID'), os.getenv('MINIMAX_API_KEY')) if check_env(['MINIMAX_GROUP_ID', 'MINIMAX_API_KEY']) else False,
        'mosaic': lambda: os.getenv('MOSAIC_API_KEY'),
        'sagemaker': lambda: (os.getenv('SAGEMAKER_ENDPOINT_KEY'), os.getenv('SAGEMAKER_REGION_NAME')) if check_env(['SAGEMAKER_ENDPOINT_KEY', 'SAGEMAKER_REGION_NAME']) else False,
        'default': lambda: True
    }

    return embedders.get(embedding_name, lambda: 'default')()


    