from datetime import datetime


async def aggregate_salaries(dt_from: str, dt_upto: str, group_type: str, connect) -> dict:
    client = connect
    db = client.test
    collection = db.sample_collection

    dt_from: datetime = datetime.fromisoformat(dt_from)
    dt_upto: datetime = datetime.fromisoformat(dt_upto)

    pipeline: list = [{'$match': {'dt': {'$gte': dt_from, '$lte': dt_upto}}},
                      {"$group": {'_id': {'$dateTrunc': {'date': '$dt', 'unit': group_type}},
                                  'total': {'$sum': '$value'}}},
                      {'$sort': {'_id': 1}}]
    cursor = collection.aggregate(pipeline)

    dataset: list = []
    labels: list = []
    async for doc in cursor:
        dataset.append(doc['total'])
        labels.append(doc['_id'].isoformat())
    return {'dataset': dataset, 'labels': labels}
