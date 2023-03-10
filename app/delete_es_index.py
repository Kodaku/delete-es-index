from elasticsearch import Elasticsearch

es = Elasticsearch(
    hosts=['http://host.docker.internal:9200'],
    basic_auth=('elastic', 'e0_kX+xT1Oh_v+8pLot3')
)

if es.indices.exists(index="house_prices"):
    es.options(ignore_status=[400, 404]).indices.delete(index='house_prices')
else:
    print("The index house_prices does not exists")
