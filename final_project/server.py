from flask import Flask, render_template, request, jsonify
from machinetranslation import translator  # Ensure this import is correct

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    if not textToTranslate:
        return jsonify({"error": "No text provided"}), 400
    try:
        result = translator.english_to_french(textToTranslate)
        return jsonify({"translatedText": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    if not textToTranslate:
        return jsonify({"error": "No text provided"}), 400
    try:
        result = translator.french_to_english(textToTranslate)
        return jsonify({"translatedText": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
