from django.apps import AppConfig
import joblib
from django.conf import settings
import os

class DrugConfig(AppConfig):
    name = 'drug'
    MODEL_FILE = os.path.join(settings.MODELS, 'DecisionTreeModel.joblib')
    model = joblib.load(MODEL_FILE)
