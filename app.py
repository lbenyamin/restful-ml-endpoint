from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

model_path = "model/model_train.h5"

@app.route("/")
def home():
    return render_template("home.html")

# Load your trained model from a file
model = tf.keras.models.load_model("model/model_train2.h5")

@app.route("/classify", methods=["POST"])
def classify():
    
    # Get the data from the request
    data = request.get_json()
    # Use the model to predict the class
    prediction = model.predict()
    # Return the prediction as a json response
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)