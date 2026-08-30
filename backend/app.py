# import flask libraries

from flask import Flask, request, jsonify
import joblib # Import joblib here
import pandas as pd # Import pandas here

# initialize the flask application

Learner_predictor_api = Flask("Learner Predictor")

# Load the trained model

trained_model = joblib.load("backend_files/best_random_forest_model.joblib")

#Define route for home page (GET request)

@Learner_predictor_api.route("/")
def home():
      return "Welcome to Learner Predictor API"

# Define an endpoint for single learner prediction (POST request)

@Learner_predictor_api.post("/v1/predict")
def predict():
  learner_data = request.get_json()

# Extract relevant features from JSON data
  sample = {
    "age": learner_data["age"],
    "current_occupation": learner_data["current_occupation"],
    "first_interaction": learner_data["first_interaction"],
    "profile_completed": learner_data["profile_completed"],
    "website_visits": learner_data["website_visits"],
    "time_spent_on_website": learner_data["time_spent_on_website"],
    "page_views_per_visit": learner_data["page_views_per_visit"],
    "last_activity": learner_data["last_activity"],
    "print_media_type1": learner_data["print_media_type1"],
    "print_media_type2": learner_data["print_media_type2"],
    "digital_media": learner_data["digital_media"],
    "educational_channels": learner_data["educational_channels"],
    "referral": learner_data["referral"]
}

# convert the extracted data into a Pandas Dataframe
  input_data = pd.DataFrame([sample])

# Make prediction (get status of learner)
  predicted_status = trained_model.predict(input_data)

#return the predicted status
  return jsonify({'Predicted status of learner': str(predicted_status[0])})

# Define the endpoint for batch prediction (POST request)
@Learner_predictor_api.post("/v1/predictbatch")
def predict_batch():
  batch_datafile = request.files['file']

# read the csv file into a Pandas Dataframe
  input_data = pd.read_csv(batch_datafile)

# Make prediction (get status of learner)
  predicted_status = trained_model.predict(input_data)

# create dictionary of predictions with learner IDs as keys
  learner_id = input_data['ID'].tolist()
  predicted_status_dict = dict(zip(learner_id, predicted_status))

# return the predictions as a JSON response
  return predicted_status_dict

# run the flask application in debug mode inf this script is executed directly
if __name__ == "__main__":
  Learner_predictor_api.run()
