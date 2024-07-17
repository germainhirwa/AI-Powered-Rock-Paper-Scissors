# GestureGauntlet: AI-Powered Rock Paper Scissors

## Description

GestureGauntlet is an innovative, AI-powered take on the classic game of Rock Paper Scissors. This project leverages computer vision, machine learning, and artificial intelligence to create an interactive and engaging gaming experience.

## Features

- **Real-time Hand Gesture Recognition**: Uses OpenCV and cvzone's HandTrackingModule for accurate, real-time hand gesture detection and interpretation.
- **AI Opponent**: Challenges players with a randomized AI opponent.
- **Interactive User Interface**: Custom background with overlaid game elements, including scores and a countdown timer.
- **Webcam Integration**: Players use their webcam to input moves, ensuring accessibility and ease of play.
- **Automatic Scoring System**: Real-time score tracking for both player and AI.
- **Visual Feedback**: Displays AI moves using custom images for clear visual feedback.

## Technology Stack

- Python
- OpenCV (cv2) for image processing and computer vision
- cvzone for advanced computer vision utilities
- MediaPipe for hand tracking and gesture recognition
- NumPy for numerical operations

# Installation

## Clone the repository
git clone https://github.com/germainhirwa/AI-Powered-Rock-Paper-Scissors.git
## Navigate to the project directory
cd GestureGauntlet
## Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
## Install the required packages
pip install -r requirements.txt
## Ensure your webcam is connected and functioning
Run the main script
python main.py

### Press 's' to start the game. Hold your hand in front of the webcam and make your move (rock, paper, or scissors) when prompted. The AI will make its move, and the winner of the round will be determined. Scores are updated automatically. Play as many rounds as you like!

# Project Structure

GestureGauntlet/
├── main.py
├── requirements.txt
└── Resources/
├── BG.png
├── 1.png
├── 2.png
└── 3.png

## Contributing

Contributions to GestureGauntlet are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- OpenCV and cvzone communities for their excellent computer vision tools.
- MediaPipe team for their hand tracking solution.
