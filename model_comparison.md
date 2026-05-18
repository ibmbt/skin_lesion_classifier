# Skin Lesion Classifier: V1 vs V2 Comparison

## Maximum Accuracies Achieved
- **V1 Model:** ~77.00%
- **V2 Model:** 78.99%

## Key Differences in V2
While V2 maintains the exact same core Convolutional Neural Network (CNN) architecture as V1, several critical training and evaluation improvements were introduced to achieve better generalization:

1. **Stratified Train/Test Split:** Ensures every class has proportional representation in both training and testing sets, whereas V1 used a simple random split that could leave smaller classes underrepresented.
2. **Learning Rate Scheduler:** Implemented `ReduceLROnPlateau` to automatically halve the learning rate when the training loss stops improving, allowing for finer learning steps later in training.
3. **Early Stopping & Best Model Validation:** Increased total allowable epochs to 80 but added a patience mechanism (terminates if no improvement for 15 epochs) to stop training when accuracy stagnates, automatically saving and reverting to the best-performing model weights.
4. **Test-Time Augmentation (TTA):** During testing/evaluation, the model now averages predictions from three inputs: the original image, a horizontally flipped version, and a vertically flipped version, yielding a more robust prediction.

## Why We Are Stopping at ~79% (For Now)
We are pausing architectural and hyperparameter optimizations here for several key reasons:

1. **Parameter-to-Data Imbalance:** The current CNN features a massive fully connected layer, resulting in over 25 million parameters. Training this on a dataset of only ~550 training images means the model is highly prone to memorizing the data. The current pipeline manages this well, but we have reached the limit of what this architecture can reliably extract.
2. **Risk of Test Set Overfitting:** Further micro-adjustments to the hyperparameters might mathematically yield another 1-2% improvement, but this would likely just be the model overfitting to our specific test set rather than demonstrating true, generalizable pattern recognition.
3. **The Data Ceiling:** The most significant bottleneck right now is the sheer limits of learning from ~700 total images. The absolute most productive next step is focusing on data collection (aiming for 200+ images per class). 
4. **Architectural Limits:** Pushing significantly higher (e.g., into the 90%+ range) would typically require abandoning our custom from-scratch CNN in favor of Transfer Learning (using massive pre-trained models like ResNet or EfficientNet). Until we expand the dataset, maximizing our from-scratch baseline is the priority.