from elasticsearch import Elasticsearch
import sys
import json

# Global
es = Elasticsearch(
    ['localhost'],
    port=9200

)

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        with open(sys.argv[1]) as json_file:
            json_docs = json.load(json_file)
        for news in json_docs:
            es.index(index = "stock_news", body = news)
    else:
        print("Provide file name to read.")