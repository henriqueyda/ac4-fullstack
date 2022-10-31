import json

tasks = [
    {
        "id": 1,
        "name": "Smartphone",
        "description": "This is a smartphone",
        "price": 27.6
    },
    {
        "id": 2,
        "name": "Smart TV",
        "description": "This is a smart TV",
        "price": 25
    },
    {
        "id": 3,
        "name": "Macbook",
        "description": "This is a Macbook",
        "price": 40
    }
]

tasksJSON = json.dumps(tasks)

class Product():

    def json_return():
        return tasksJSON
    
    def total_price():
        sum = 0
        for task in tasks:
            sum += task.get("price")
        return {
            "total": sum
        }