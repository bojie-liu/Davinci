
from gensim.models import Word2Vec

_model_path = "/Users/joshualiu/dev/data/word2vec-for-wiki-master/wiki_model"

if __name__ == "__main__":
    model = Word2Vec.load(_model_path)
    # rlt = model.doesnt_match("机制 作用 影响 研究".split())
    rlt = model.similarity('好', '坏')
    print(rlt)
    rlt = model.similarity('好', '不好')
    print(rlt)
    rlt = model.similarity('好', '强')
    print(rlt)
