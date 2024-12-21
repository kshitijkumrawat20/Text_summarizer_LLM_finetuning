from Text_summarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from Text_summarizer.utils.common import read_yaml, create_directories
from Text_summarizer.entity.config_entity import DataIngestionConfig,DataTransformationConfig, ModelTrainerConfig

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath= PARAMS_FILE_PATH ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config= self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_files,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config =DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            tokenizer_name= config.tokenizer_name
        )
        return data_transformation_config
    
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config = self.config.ModelTrainer
        params = self.params.TrainingArguments
        
        create_directories([config.root_dir])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            per_device_train_batch_size = params.per_device_train_batch_size,
            per_device_eval_batch_size = params.per_device_eval_batch_size,
            gradient_accumulation_steps = params.gradient_accumulation_steps,
            warmup_steps = params.warmup_steps,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            eval_strategy = params.eval_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            save_total_limit = params.save_total_limit,
            learning_rate = params.learning_rate,
            load_best_model_at_end = params.load_best_model_at_end,
            fp16 = params.fp16,
            dataloader_num_workers = params.dataloader_num_workers
        )
        return model_trainer_config
    
    