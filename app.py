from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

# Database connection
db = MySQLdb.connect(host="localhost", user="your_user", passwd="your_password", db="your_database", charset="utf8mb4")
cursor = db.cursor()

@app.route('/polling_unit/<polling_unit_id>')
def polling_unit_results(polling_unit_id):
    cursor.execute("""
        SELECT pu.polling_unit_name, pu.polling_unit_number, pr.party_abbreviation, pr.party_score
        FROM polling_unit pu
        JOIN announced_pu_results pr ON pu.uniqueid = pr.polling_unit_uniqueid
        WHERE pu.uniqueid = %s
    """, (polling_unit_id,))

    results = cursor.fetchall()
    return render_template("polling_unit_results.html", results=results)

@app.route('/lga_results', methods=['GET', 'POST'])
def lga_results():
    cursor.execute("SELECT lga_id, lga_name FROM lga WHERE state_id = 25")
    lgas = cursor.fetchall()

    results = []
    if request.method == 'POST':
        lga_id = request.form['lga_id']
        cursor.execute("""
            SELECT pr.party_abbreviation, SUM(pr.party_score) as total_score
            FROM polling_unit pu
            JOIN announced_pu_results pr ON pu.uniqueid = pr.polling_unit_uniqueid
            WHERE pu.lga_id = %s
            GROUP BY pr.party_abbreviation
        """, (lga_id,))

        results = cursor.fetchall()

    return render_template("lga_results.html", lgas=lgas, results=results)


@app.route('/add_polling_unit', methods=['GET', 'POST'])
def add_polling_unit():
    if request.method == 'POST':
        polling_unit_name = request.form['polling_unit_name']
        polling_unit_number = request.form['polling_unit_number']
        lga_id = request.form['lga_id']

        cursor.execute("""
            INSERT INTO polling_unit (polling_unit_name, polling_unit_number, lga_id, state_id)
            VALUES (%s, %s, %s, 25)
        """, (polling_unit_name, polling_unit_number, lga_id))

        db.commit()
        polling_unit_id = cursor.lastrowid

        party_scores = request.form.getlist('party_scores')
        party_names = request.form.getlist('party_names')

        for party, score in zip(party_names, party_scores):
            cursor.execute("""
                INSERT INTO announced_pu_results (polling_unit_uniqueid, party_abbreviation, party_score)
                VALUES (%s, %s, %s)
            """, (polling_unit_id, party, score))

        db.commit()
        return "Polling Unit and Results Added Successfully!"

    return render_template("add_polling_unit.html")


if __name__ == '__main__':
    app.run(debug=True)
