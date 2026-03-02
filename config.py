# config.py — Central configuration for all pipeline constants
# Edit here, never hardcode values in notebooks or src files

RANDOM_SEED = 42

# Dataset
KAGGLE_DATASET = "maharshipandya/-spotify-tracks-dataset"
DATA_PATH = "data/dataset.csv"
TARGET_GENRES = [
    "pop", "hip-hop", "rock", "latin", "r-n-b",
    "edm", "classical", "jazz", "country", "indie"
]
N_GENRES = len(TARGET_GENRES)
SAMPLE_SIZE = 15000

# Splits
TRAIN_SIZE = 0.70
VAL_SIZE   = 0.15
TEST_SIZE  = 0.15

# Autoencoder ablation
BOTTLENECK_DIMS = [4, 8, 16, 32]
EPOCHS = 100
BATCH_SIZE = 256
LEARNING_RATE = 1e-3
EARLY_STOPPING_PATIENCE = 10

# Evaluation
PRIMARY_METRIC = "macro_f1"
