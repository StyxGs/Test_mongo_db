import json
import pandas as pd

from datetime import datetime


async def aggregate_salaries(dt_from: str, dt_upto: str, group_type: str, connect) -> dict:
    client = connect
    db = client.test
    collection = db.sample_collection

    if group_type == 'month':
        g_t: str = 'MS'
    else:
        g_t: str = group_type[0].upper()

    date_list: list = [x.isoformat() for x in
                       list(pd.date_range(start=dt_from, end=dt_upto, freq=g_t))]
    dt_from: datetime = datetime.fromisoformat(dt_from)
    dt_upto: datetime = datetime.fromisoformat(dt_upto)

    pipeline: list = [{'$match': {'dt': {'$gte': dt_from, '$lte': dt_upto}}},
                      {'$group': {'_id': {'$dateTrunc': {'date': '$dt', 'unit': group_type}},
                                  'total': {'$sum': '$value'}}},
                      {'$sort': {'id': 1}}]

    cursor: dict = {x['_id'].isoformat(): x['total'] for x in list(collection.aggregate(pipeline))}

    dataset: list = []
    labels: list = []

    for doc in date_list:
        labels.append(doc)
        if doc not in cursor:
            dataset.append(0)
        else:
            dataset.append(cursor[doc])
    return {"dataset": dataset, "labels": labels}


async def check_valid_str(obj: str) -> dict | bool:
    try:
        return json.loads(obj)
    except ValueError:
        return False
