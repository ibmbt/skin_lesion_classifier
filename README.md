# Skin Condition and Lesion Classification

This repository contains a PyTorch-based Convolutional Neural Network (CNN) designed to classify dermatological conditions. The pipeline processes raw image data to categorize skin textures into five distinct classes: Acne, Burns, Eczema, Bruises, and Healthy Skin.

## Dataset Collection

To ensure the model learns from a robust variety of lighting conditions, skin tones, and lesion severities, the training data was manually collected from varying platforms woth passion. 

**Data Sources:**
* Google Images
* Reddit
* Instagram
* YouTube
* Pinterest
* Bing Search
* DuckDuckGo

*(Note: Download the pre-compiled dataset via [will add final dataset at the end] and extract it into the root directory before running the training notebook.)*

## Project Structure

```text
project_root/
├── dataset/                  # Directory containing the 5 image classes (add after downloading)
├── rename_data.py            # Preprocessing script to normalize sequential file names
├── Skin_Lesion_CNN.ipynb     # Main PyTorch notebook (Architecture, Training, Evaluation)
└── README.md
```

## Setup and Preprocessing

**1. Requirements and Installation**
This project requires Python 3.8 or higher. To run the model and utilities locally, install the core PyTorch libraries via your terminal:

```bash
pip install torch torchvision
```
Note: No need if using colab to run this

**2. Data Normalization**
If you are modifying the dataset or adding your own images, ensure the file names are clean and sequentially numbered for PyTorch's ImageFolder loader. 
Run the provided utility in your terminal in projext root folder with dataset in it:

bash
python rename_data.py

## Running Instructions

1. Zip the dataset/ folder and upload it to your Google Drive.
2. Open the .ipynb notebook in Colab. 
3. Run the initial cells to mount your Drive and extract the data directly into Colab's local high-speed storage (/content/).
4. Execute the training loop using the T4 GPU runtime.
