from Text_summarizer.config.configuration import ConfigurationManager
from Text_summarizer.components.model_evaluation import  ModelEvaluation
from Text_summarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval_config = ModelEvaluation(config=model_eval_config)
        model_eval_config.train()