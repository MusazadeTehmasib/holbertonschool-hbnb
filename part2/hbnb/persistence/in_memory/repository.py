import uuid

class InMemoryRepository:
    def __init__(self):
        # storage structure: {"ModelName": {id: data_dict}}
        self._storage = {}

    def create(self, model_name, data):
        item_id = str(uuid.uuid4())
        # make a shallow copy to avoid external mutation
        record = dict(data)
        record["id"] = item_id

        if model_name not in self._storage:
            self._storage[model_name] = {}

        self._storage[model_name][item_id] = record
        return record

    def get(self, model_name, item_id):
        return self._storage.get(model_name, {}).get(item_id)

    def update(self, model_name, item_id, updates):
        if model_name not in self._storage:
            return None
        if item_id not in self._storage[model_name]:
            return None
        self._storage[model_name][item_id].update(updates)
        return self._storage[model_name][item_id]

    def delete(self, model_name, item_id):
        if item_id in self._storage.get(model_name, {}):
            del self._storage[model_name][item_id]
            return True
        return False

    def list(self, model_name):
        return list(self._storage.get(model_name, {}).values())
