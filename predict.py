import json, sys, numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("model/phishing_model.keras")
v = json.load(open("model/vocab.json"))

def predict(url):
    x = np.zeros((1, v["maxlen"]), dtype="int32")
    for j, c in enumerate(str(url).strip()[: v["maxlen"]]):
        x[0, j] = v["char2idx"].get(c, v["unk"])
    p = float(model.predict(x, verbose=0)[0][0])
    return {"label": "phishing" if p > 0.5 else "legitimate", "phishing_probability": round(p, 4)}

if __name__ == "__main__":
    print(predict(sys.argv[1]))