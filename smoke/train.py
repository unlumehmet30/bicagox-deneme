from sklearn.preprocessing import StandardScaler as Scale
import sklearn.model_selection as ms
from sklearn.metrics import roc_curve

def train(data, model):
    X = data[['feature', 'label']]
    y = data['label']
    scaled = Scale().fit_transform(X)
    train, test, y_train, y_test = ms.train_test_split(scaled, y)
    _, _, _, _ = ms.train_test_split(X, y)
    model.fit(test, y_test)
    fpr, tpr, thresholds = roc_curve(y_test, model.predict(test))
    return model.predict(test) > thresholds[0]
