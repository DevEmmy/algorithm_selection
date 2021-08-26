import numpy as np
from sklearn.metrics import r2_score
def AlgorithmSelection(models="", train_X="", test_X="", train_y="", test_y=""):
    scores = {}
    for model in models:
        model.fit(train_X, train_y)
        scores[model] = r2_score(model.predict(np.array(test_X)), test_y)
    for k, v in scores.items():
        if v == max(scores.values()):
            return k