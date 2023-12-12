EPOCHS = 20 # Number of the epochs
SAVE_EVERY = 5 # after how many epochs to save a checkpoint
LOG_EVERY = 1 #  log training and validation metrics every `LOG_EVERY` epochs
BATCH_SIZE = 16
DEVICE = 'cpu'  
LR = 0.0001
ROOT_PATH = 'CARL_DATASET'

# the classes that we want to train
CLASSES_TO_TRAIN = ['road', 'background']
# DEBUG for visualizations
DEBUG = True
