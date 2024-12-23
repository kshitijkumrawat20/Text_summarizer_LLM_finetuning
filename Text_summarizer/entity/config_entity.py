from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass
class ModelTrainerConfig:
    root_dir : Path
    data_path : Path
    model_ckpt : Path
    num_train_epochs: int  
    per_device_train_batch_size: int 
    per_device_eval_batch_size: int  
    gradient_accumulation_steps: int  
    warmup_steps: int 
    weight_decay: float
    logging_steps: int   
    eval_strategy: str  
    eval_steps: int  
    save_steps: int 
    save_total_limit: int  
    learning_rate: float  
    load_best_model_at_end: bool  
    fp16: bool  
    dataloader_num_workers: int 
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name:Path
    