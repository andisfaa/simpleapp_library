from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def hitung_nilai_akhir(tugas, kuis, uts, uas):
    return 0.2 * tugas + 0.2 * kuis + 0.3 * uts + 0.3 * uas

def konversi_nilai_huruf(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 65:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    if request.method == "POST":
        nama = request.form["nama"]
        tugas = int(request.form["tugas"])
        kuis = int(request.form["kuis"])
        uts = int(request.form["uts"])
        uas = int(request.form["uas"])

        nilai_akhir = hitung_nilai_akhir(tugas, kuis, uts, uas)
        huruf = konversi_nilai_huruf(nilai_akhir)

        hasil = {
            "nama": nama,
            "nilai_akhir": round(nilai_akhir, 2),
            "huruf": huruf
        }

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
