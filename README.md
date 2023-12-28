# Cell Segmentation using YOLOv8

## Overview
This project aims to implement cell segmentation using the YOLOv8 model. It's designed as a web-based application where users can train and use a model for the purpose of segmenting cells in images. The project uses Flask for the backend, integrates with YOLOv8 for image processing, and offers a user-friendly web interface.

## Features
- **Data Ingestion:** Automated process to ingest and prepare data for training.
- **Data Validation:** Ensures the quality and integrity of the data before training.
- **Model Training:** Trains the YOLOv8 model for cell segmentation.
- **Web Interface:** A simple and interactive UI for training the model and making predictions.

## Prerequisites
- Python 3.x
- Flask
- YOLOv8
- Additional requirements are listed in `requirements.txt`.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/AaryanPotdar/CellSegmentation_Yolo_v8.git
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask server:
   ```
   python app.py
   ```
2. Access the web interface at `http://localhost:5000` (default URL).
3. Follow the on-screen instructions to train the model or make predictions.

## Project Structure
- `app.py`: Flask application entry point.
- `requirements.txt`: Lists the dependencies for the project.
- `training_pipeline.py`: Defines the training pipeline for the model.
- `/cellSegmentation`: Contains modules for data ingestion, validation, and model training.
- `index.html`: Front-end UI for the web application.

## Contact
- aaruvpotdar@gmail.com
