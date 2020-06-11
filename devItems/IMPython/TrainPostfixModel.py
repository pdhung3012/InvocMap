fpModelData='postfix_d2v_code.model'

#Import all the dependencies
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

fop='filter/'
fpPostfix=fop+'postfix.txt'

data=[]
with open(fpPostfix,encoding='latin1') as infile:
    for line in infile:
        # print(line)
        data.append(line)
print('end load text {}'.format(len(data)))
# data = ["I love machine learning. Its awesome.",
#         "I love coding in python",
#         "I hate building chatbots",
#         "they chat amagingly well"]
#
# for i in range(1,1000000):
#     strItem='I love code snippet {}'.format(i)
#     data.append(strItem)
#
tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]

max_epochs = 5
vec_size = 20
alpha = 0.025

model = Doc2Vec(size=vec_size,
                alpha=alpha,
                min_alpha=0.00025,
                min_count=1,
                dm=0)

model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    # print('iteration {0}'.format(epoch))
    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha
    print('End epoch{}'.format(epoch))

model.save(fpModelData)
# print("Model Saved")

from gensim.models.doc2vec import Doc2Vec

model= Doc2Vec.load(fpModelData)
#to find the vector of a document which is not in training data
test_data = word_tokenize("I hate building chatbots")
v1 = model.infer_vector(test_data)
print("V1_infer", v1)
sims = model.docvecs.most_similar([v1])
print(len(sims))
print(sims)
for index in range(0,len(sims)):
    key=int(sims[index][0])
    strValue=data[key]
    print(strValue)
# # to find most similar doc using tags
# similar_doc = model.docvecs.most_similar('1')
# print(similar_doc)


# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# print(model.docvecs['1'])