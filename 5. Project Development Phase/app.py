from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model
model = pickle.load(open("rdf.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/submit", methods=["POST"])
def submit():
    try:
        gender = float(request.form["Gender"])
        married = float(request.form["Married"])
        dependents = float(request.form["Dependents"])
        education = float(request.form["Education"])
        self_employed = float(request.form["Self_Employed"])
        applicant_income = float(request.form["ApplicantIncome"])
        coapplicant_income = float(request.form["CoapplicantIncome"])
        loan_amount = float(request.form["LoanAmount"])
        loan_term = float(request.form["Loan_Amount_Term"])
        credit_history = float(request.form["Credit_History"])
        property_area = float(request.form["Property_Area"])

        data = np.array([[gender,
                          married,
                          dependents,
                          education,
                          self_employed,
                          applicant_income,
                          coapplicant_income,
                          loan_amount,
                          loan_term,
                          credit_history,
                          property_area]])

        prediction = model.predict(data)

        if prediction[0] == 1:
            result = "✅ Loan Approved"
        else:
            result = "❌ Loan Rejected"

        return render_template("submit.html", prediction=result)

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
