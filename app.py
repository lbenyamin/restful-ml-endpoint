from flask import Flask
from flask import Flask, request, jsonify
import pickle
import tensorflow

app = Flask(__name__)

# Load your trained model from a file
model = tf.keras.models.load_model("model_train2.h5")

@app.route("/classify", methods=["POST"])
def classify():

    # Use the model to predict the class
    prediction = model.predict()

    # Return the prediction as a json response
    return prediction

if __name__ == "__main__":
    app.run(debug=True)