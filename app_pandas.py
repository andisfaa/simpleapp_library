from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    table = None
    mean_result = None
    if request.method == "POST":
        file = request.files["file"]
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file)

            kolom = request.form.get("kolom")

            if kolom and kolom in df.columns:
                df = df[[kolom]]

            # Ambil hanya kolom numerik
            numeric_cols = df.select_dtypes(include='number')
            if not numeric_cols.empty:
                mean_result = numeric_cols.mean().to_dict()

            table = df.to_html(classes="table table-striped", index=False)

    return render_template("index_pandas.html", table=table, mean_result=mean_result)

if __name__ == "__main__":
    app.run(debug=True)
