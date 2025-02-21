import json

project = {
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "type": "CF",
    "author": "SingTown",
    "license": "CC BY-NC 4.0",
    "labels": [
        {
            "name": "cat",
            "color": "#FF0000",
            "description": "cat animal",
        },
        {
            "name": "dog",
            "color": "#00FF00",
            "description": "dog animal",
        },
    ],
    "annotations": [],
}

for i in range(400):
    project["annotations"].append(
        {
            "name": f"cat.{i}.jpg",
            "label": "cat",
            "test": True,
            "url": f"http://127.0.0.1:8000/media/images/cat.{i}.jpg",
        }
    )

for i in range(400):
    project["annotations"].append(
        {
            "name": f"dog.{i}.jpg",
            "label": "dog",
            "test": True,
            "url": f"http://127.0.0.1:8000/media/images/dog.{i}.jpg",
        }
    )

for i in range(400, 1000):
    project["annotations"].append(
        {
            "name": f"cat.{i}.jpg",
            "label": "cat",
            "test": False,
            "url": f"http://127.0.0.1:8000/media/images/cat.{i}.jpg",
        }
    )

for i in range(400, 1000):
    project["annotations"].append(
        {
            "name": f"dog.{i}.jpg",
            "label": "dog",
            "test": False,
            "url": f"http://127.0.0.1:8000/media/images/dog.{i}.jpg",
        }
    )

with open("f47ac10b-58cc-4372-a567-0e02b2c3d479.json", "w") as f:
    json.dump(project, f)
