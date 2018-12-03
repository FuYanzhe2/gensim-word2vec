import gensim

model = gensim.models.Word2Vec.load("wiki.model")

result = model.most_similar("狮子")

for e in result :
    print(e)