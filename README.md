# SpeakHand

SpeakHand is a real-time American Sign Language (ASL) to speech and text translation application. Powered by computer vision and deep learning, it aims to bridge the communication gap for the deaf and hard-of-hearing community.

## About The Project

This project was developed to provide an intuitive and accessible way to translate sign language into spoken words or written text in real-time. Using a standard webcam, SpeakHand captures hand gestures, processes them through a trained neural network, and outputs the corresponding translation. This facilitates smoother communication between sign language users and non-signers.

## Features

- **Real-time Translation**: Translates hand gestures from a live video feed.
- **High Accuracy**: Utilizes a deep learning model for accurate gesture recognition.
- **Text & Speech Output**: Displays the translated text and provides synthesized speech output.
- **User-Friendly Interface**: Simple and intuitive GUI for easy interaction.

## Technology Stack

This project is built with a modern stack of technologies:

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [TensorFlow](https://www.tensorflow.org/) / [Keras](https://keras.io/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.8+
- pip (Python package installer)

### Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone https://github.com/Induranga-kawishwara/SpeakHand.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd SpeakHand
    ```
3.  Install the required Python packages using `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Once the installation is complete, you can run the application.

1.  Execute the main script:
    ```sh
    python main.py
    ```
2.  The application window will open, and the webcam feed will start automatically.
3.  Perform sign language gestures in front of the camera to see the real-time translation on the screen.
