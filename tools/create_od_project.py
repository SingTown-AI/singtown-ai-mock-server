import json

project = {
    "id": "d94f5e8c-7b3a-4e8f-9a2c-1b3d5f7a9c4e",
    "type": "OD",
    "author": "SingTown",
    "license": "CC BY-NC 4.0",
    "labels": [
        {
            "name": "cat",
            "color": "#FF0000",
            "description": "cat animal"
        },
        {
            "name": "dog",
            "color": "#00FF00",
            "description": "dog animal"
        }
    ],
    "train": [],
    "val": [],
}

def get_bboxes(file:str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    bboxes = []
    for line in lines:
        if line:
            index, x, y, w, h = line.split(" ")
            bboxes.append({
                "label": project["labels"][int(index)]['name'],
                "x": float(x),
                "y": float(y),
                "w": float(w),
                "h": float(h),
            })
    return bboxes
     
print(get_bboxes("labels/cat.0.txt"))

for i in range(400):
    project["val"].append(
        {
            "name": f"cat.{i}.jpg",
            "bboxes": get_bboxes(f"labels/cat.{i}.txt"),
            "url": f"http://127.0.0.1:8000/media/images/cat.{i}.jpg"
        }
    )

with open(f"d94f5e8c-7b3a-4e8f-9a2c-1b3d5f7a9c4e.json", "w") as f:
    json.dump(project, f)