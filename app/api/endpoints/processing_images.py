from typing import Dict
from .models import DataModel
from core import artificial_inteligence_processor

async def processing_images(data: str) -> Dict:
    data_model = data
    result = await artificial_inteligence_processor.process(data_model)
    return result