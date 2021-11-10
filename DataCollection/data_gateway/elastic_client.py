from elasticsearch import Elasticsearch
import sys
import json

# Global
es = Elasticsearch(
    ['localhost'],
    port=9200

)

def insert_data(index):
    if(len(sys.argv) > 1):
        with open(sys.argv[1]) as json_file:
            json_docs = json.load(json_file)
        if not es.indices.exists(index="stock_news"):
            es.indices.create(index="stock_news")
        for news in json_docs:
            es.index(index = "stock_news", body = news)
    else:
        print("Provide file name to read.")

def get_stock_info(query):
    stock_list = []
    stock_set = set()
    body = {
        "query": {
            "regexp": {
            "SYMBOL": {
                "value": query + ".*",
                "flags": "ALL",
                "case_insensitive": "true",
                "max_determinized_states": 10000,
                "rewrite": "constant_score"
            }
            }
        }
    }
    res1 =  es.search(index="stock_data", body=body)['hits']['hits']

    for stock in res1:
        stock_list.append(stock)
    
    body = {
         "query": {
            "multi_match": {
            "query": query,
            "fields": [],
            "operator": "and"
            }
        }
    }
    res2 = es.search(index="stock_data", body=body)['hits']['hits']

    for stock in res2:
        stock_list.append(stock)
    
    stock_list_final = []
    for data in { each['_source']['SYMBOL'] : each for each in stock_list }.values():
        stock_list_final.append(data)
    return stock_list_final

def get_stock_news(query):
    body = {
        "query": {
            "multi_match": {
            "query": query,
            "fields": ["title^3", "gist^2", "content"]
            }
        }
    }
    return es.search(index="stock_news", body=body)['hits']['hits']

if __name__ == '__main__':
    print(json.dumps(get_stock_info("SBI"), indent=2))
    print(json.dumps(get_stock_news("Indian Railway"), indent=2))