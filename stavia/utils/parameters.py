from __future__ import absolute_import

import os
WORKING_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
# ITERMEDIATE
IS_BUILDING_STAGE=1
VERBOSE=1
METHOD='llm' #llm for log-linear model and lr for logistic regression
DATASET_ID=1
PARAMS_ID=1

#TOSTR
DATASET_ID=str(DATASET_ID)
MODEL_ID= '{}.{}'.format(DATASET_ID, PARAMS_ID)

#GLOBAL
PUNCTUATIONS=',.-()#|/\\'

#ELASTICSEARCH
HOST = "http://localhost:9200/"
try:
    HOST = os.environ['ELASTICSEARCH_HOST']
except:
    pass

URI = HOST+"smart_address"
SEARCHING_URI = HOST+"smart_address/_search"
CONFIGURATION_FILE=os.path.join(WORKING_DIR, '_data/configuration.json')
RAT_FILE=os.path.join(WORKING_DIR, '_data/rat_data.json')
FUZZINESS=1
QUERY_SIZE=3000
SLOP=0

#CANDIDATE GRAPH
FIELDS=['city', 'district', 'ward', 'street']
MAP_LEVEL={'country': 0, 'city': 1, 'district': 2, 'ward': 3, 'street': 4, 'name': 5}
MAP_FIELD={0: 'country', 1: 'city', 2:'district', 3: 'ward', 4: 'street', 5: 'name'}
BEAM_SIZE=8

#CRF
CRF_TRAIN_FILE=os.path.join(WORKING_DIR, '_data/train_crf{}.txt'.format('_small' if IS_BUILDING_STAGE == 1 else ''))
USE_RAT=True
CRF_MODEL_FILE=os.path.join(WORKING_DIR, '_data/crf{}.model'.format('_norat' if USE_RAT == False else '_rat'))
RAT_DICT_FILE=os.path.join(WORKING_DIR, '_data/rat_dict.json')

#RERANKING
TRAIN_FINAL_FILE=os.path.join(WORKING_DIR, '_data/train_final{}_{}.json'.format('_small' if IS_BUILDING_STAGE == 1 else '', DATASET_ID))
MODEL_FINAL_FILE=os.path.join(WORKING_DIR, '_data/final_{}_{}.model'.format(METHOD, MODEL_ID))
USE_LEXICAL_FEATURES=False
NUM_ITER=400
LAMBDA_REG=0.00001

