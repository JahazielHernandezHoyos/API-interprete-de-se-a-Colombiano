from typing import Dict
from .models import DataModel
from core import artificial_inteligence_processor

def processing_images():
    data_model = DataModel(**data)
    result = artificial_inteligence_processor.process(data_model)
    return result