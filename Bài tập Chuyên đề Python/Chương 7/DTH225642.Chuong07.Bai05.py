import json

def main():
    pythonObject = {
        "ten": "Trần Duy Thanh",
        "tuoi": 50,
        "ma": "nv1"
    }

    jsonString = json.dumps(pythonObject, ensure_ascii=False)

    print(jsonString)

if __name__ == "__main__":
    main()