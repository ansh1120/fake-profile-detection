from flask import Flask, render_template, request, redirect, url_for, session
import pickle

app = Flask(__name__)
app.secret_key = "final_year_project_secret"

# Load ML model
with open("fake_profile_model.pkl", "rb") as f:
    model, FEATURES = pickle.load(f)

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        if role == "admin" and username == "admin" and password == "admin123":
            session["user"] = "admin"
            return redirect(url_for("dashboard"))

        elif role == "user" and username == "user" and password == "user123":
            session["user"] = "user"
            return redirect(url_for("dashboard"))

        else:
            return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", role=session["user"])

# ---------------- CHECK PROFILE ----------------
@app.route("/check_profile", methods=["GET", "POST"])
def check_profile():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        data = [
            int(request.form["followers"]),
            int(request.form["following"]),
            int(request.form["posts"]),
            int(request.form["bio_length"]),
            int(request.form["profile_pic"])
        ]
        prediction = model.predict([data])[0]
        result = "Fake Profile ❌" if prediction == 1 else "Genuine Profile ✅"
        return render_template("result.html", result=result)

    return render_template("check_profile.html")

# ---------------- OTHER PAGES ----------------
@app.route("/statistics")
def statistics():
    return render_template("statistics.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
