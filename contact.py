from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        user = request.form.get('user')
        psswrd = request.form.get('psswrd')

        if not name or not email or not phone or not user or not psswrd:
            return jsonify({"error": "Missing required fields"}), 400

        # Call LibreOffice macro via command line
        # Replace 'MyMacro' with your macro name and adjust paths
        macro_command = (
            f'soffice --headless --invisible '
            f'"vnd.sun.star.script:Standard.Module1.MyMacro?language=Basic&location=application" '
            f'--norestore'
        )

        # Pass form data to macro via environment variables or temp file
        env = {"FORM_NAME": name, "FORM_EMAIL": email, "FORM_PHONE": phone, "FORM_USER": user, "FORM_PSSWRD": psswrd, **dict(**os.environ)}

        result = subprocess.run(
            shlex.split(macro_command),
            env=env,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        return jsonify({"status": "Macro executed successfully", "output": result.stdout})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
