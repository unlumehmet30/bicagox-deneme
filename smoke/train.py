from sklearn.preprocessing import StandardScaler as Scale
import sklearn.model_selection as ms
from sklearn.metrics import roc_curve

def train(data, model):
    X = data[['feature']]
    y = data['label']
    train, test, y_train, y_test = ms.train_test_split(X, y)
    train = Scale().fit_transform(train)
    model.fit(train, y_train)
    fpr, tpr, thresholds = roc_curve(y_test, model.predict(test))
    return fpr, tpr
