from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<title>Vowel Counter</title>
<h2>Vowel Counter</h2>
<form method="post">
  <label>Enter a word: <input type="text" name="word" required></label>
  <input type="submit" value="Count Vowels">
</form>
{% if count is not none %}
  <h3>Number of vowels in "{{ word }}": {{ count }}</h3>
{% endif %}
'''

def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in word if char in vowels)

@app.route('/', methods=['GET', 'POST'])
def home():
    count = None
    word = ''
    if request.method == 'POST':
        word = request.form['word']
        count = count_vowels(word)
    return render_template_string(HTML_TEMPLATE, count=count, word=word)

if __name__ == '__main__':
    app.run(debug=True)
