from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with JavaScript countdown
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Countdown Timer</title>
    <script>
        let count = 10;
        function startCountdown() {
            const countdownEl = document.getElementById("countdown");
            const interval = setInterval(() => {
                countdownEl.innerHTML = count;
                count--;
                if (count < 0) {
                    clearInterval(interval);
                    countdownEl.innerHTML = "Done!";
                }
            }, 1000);
        }
        window.onload = startCountdown;
    </script>
</head>
<body>
    <h1>Countdown Timer</h1>
    <h2 id="countdown">10</h2>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
