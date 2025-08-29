from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
<!doctype html>
<title>Sum Calculator</title>
<h2>Calculate Sum from 1 to N</h2>
<form method="POST">
  Enter a number: <input type="number" name="number" required>
  <input type="submit" value="Calculate">
</form>

{% if result is not none %}
  <h3>Sum from 1 to {{ n }} is: {{ result }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def calculate_sum():
    result = None
    n = 0
    if request.method == 'POST':
        try:
            n = int(request.form['number'])
            result = 0
            for i in range(1, n + 1):
                result += i
        except ValueError:
            result = "Invalid input! Please enter a number."

    return render_template_string(html_form, result=result, n=n)

if __name__ == '__main__':
    app.run(debug=True)
