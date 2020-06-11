fpModelDataPrefix='d2v_code.model'
fpModelDataPostfix='postfix_d2v_code.model'
fopStep1='step1_prepostfix/'
fopStep2='step2_methodNames/'
#Import all the dependencies
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import os
import numpy as np


def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    return unique_list

def createDirIfNotExist(fopOutput):
    try:
        # Create target Directory
        os.mkdir(fopOutput)
        print("Directory ", fopOutput, " Created ")
    except FileExistsError:
        print("Directory ", fopOutput, " already exists")
def getLowerList(arrIn):
    arrOut=[]
    for item in arrIn:
        arrOut.append(item.lower())
    return arrOut
fop='filter/'
fpPrefix=fop+'prefix.txt'
fpPostfix=fop+'postfix.txt'
fpMNames=fop+'methods.txt'

data_prefix=[]
data_postfix=[]
methodNames=[]
with open(fpPrefix,encoding='latin1') as infile:
    for line in infile:
        # print(line)
        data_prefix.append(line)
with open(fpMNames,encoding='latin1') as infile:
    for line in infile:
        # print(line)
        methodNames.append(line)
with open(fpPostfix,encoding='latin1') as infile:
    for line in infile:
        # print(line)
        data_postfix.append(line)


print('end load text')

# model.save(fpModelData)
# print("Model Saved")

from gensim.models.doc2vec import Doc2Vec

modelPrefix= Doc2Vec.load(fpModelDataPrefix)
modelPostfix= Doc2Vec.load(fpModelDataPostfix)

for idxFile in range(1,101):
    nameIdx='{0:0=3d}'.format(idxFile)
    fopMIOutput=fopStep2+nameIdx+'/'
    fopStep1Item=fopStep1+nameIdx+'/'
    createDirIfNotExist(fopMIOutput)
    fpOutputMethod=fopMIOutput+'methods.txt'

    f=open(fopStep1Item+'ele_prefix.txt')
    strPre=f.read()
    f.close()
    f = open(fopStep1Item + 'ele_postfix.txt')
    strPost = f.read()
    f.close()
    f = open(fopStep1Item + 'ele_lemmToken.txt')
    strLemm = f.read()
    f.close()
    print(strPre)
    arrPre=word_tokenize(strPre)
    arrPost=word_tokenize(strPost)
    arrLemm=word_tokenize(strLemm)
    arrLemm2=arrLemm
    arrPre.extend(arrLemm)
    arrLemm2.extend(arrPost)
    arrPost=arrLemm2
    arrInputTokens=[]
    print(arrPre)
    if(len(arrPre)>=len(arrPost)):
        arrInputTokens=getLowerList(arrPre)
        selectedModel=modelPrefix
    else:
        arrInputTokens = getLowerList(arrPost)
        selectedModel=modelPostfix
    vector=selectedModel.infer_vector(arrInputTokens)
    sims = selectedModel.docvecs.most_similar([vector], topn=200)
    arrMethodOut=[]
    for index in range(0, len(sims)):
        key = int(sims[index][0])
        arrMethodOut.append(methodNames[key].strip())
    arrMethodOut=unique(arrMethodOut)
    np.savetxt(fpOutputMethod, arrMethodOut, fmt='%s', delimiter=',')


# #to find the vector of a document which is not in training data
# test_data = word_tokenize(data[300])
# test_lower=[]
# for index in range(0,len(test_data)):
#     if index >30:
#         continue
#     item=test_data[index]
#     test_lower.append(item.lower())
# v1 = model.infer_vector(test_lower)
# print("V1_infer", v1)
# sims = model.docvecs.most_similar([v1], topn = 30)
# print(len(sims))
# print(sims)
# print('{} expected method names {}'.format(methodNames[300],test_lower))
# for index in range(0,len(sims)):
#     key=int(sims[index][0])
#     strValue=data[key]
#     print('{}\t{}\t{}'.format(index,methodNames[key],strValue))
# # # to find most similar doc using tags
# # similar_doc = model.docvecs.most_similar('1')
# # print(similar_doc)
#
#
# # to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# # print(model.docvecs['1'])