import sys, os
from cellSegmentation.pipeline.training_pipeline import TrainPipeline
from cellSegmentation.utils.main_utils import decode_image, encode_image_base_64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from cellSegmentation.constant.application import APP_HOST, APP_PORT

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decode_image(image, clApp.filename)

        # Consider replacing os.system with subprocess.run for better security
        os.system("yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true project=/Users/aaryanpotdar/CellSegmentation/CellSegmentation_Yolo_v8/runs/segment")

        opencodedbase64 = encode_image_base_64("/Users/aaryanpotdar/CellSegmentation/CellSegmentation_Yolo_v8/runs/segment/predict/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}

        # Consider error handling for file operations
        os.system("rm -r /Users/aaryanpotdar/CellSegmentation/CellSegmentation_Yolo_v8/runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data", status=400)
    except KeyError:
        return Response("Key value error: incorrect key passed", status=400)
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid input"}), 500

    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)