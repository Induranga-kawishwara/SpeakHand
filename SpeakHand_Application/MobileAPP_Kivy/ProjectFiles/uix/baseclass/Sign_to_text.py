from main_imports import MDScreen
from ProjectFiles.applibs import utils
import warnings
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import numpy as np
import mediapipe as mp
import joblib

warnings.filterwarnings('ignore')
utils.load_kv("Sign_to_text.kv")

# MediaPipe setup
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh
mp_pose = mp.solutions.pose


class Sign_to_text_Screen(MDScreen):
    def __init__(self, **kwargs):
        super(Sign_to_text_Screen, self).__init__(**kwargs)
        self.hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2)
        self.face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, refine_landmarks=True,
                                               min_tracking_confidence=0.5, max_num_faces=1)
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.model = joblib.load('../Sign_Text/sign_language_model.pkl')
        self.detected_signs = []  # List to store detected signs

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Camera not initialized.")
            return
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        if not self.cap.isOpened():
            print("Error: Camera not initialized.")
            return

        ret, image = self.cap.read()
        if not ret:
            print("Ignoring empty camera frame.")
            return

        # Process the image
        image = cv2.flip(image, 1)
        original_image = image.copy()
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process landmarks
        hands_results = self.hands.process(rgb_image)
        face_results = self.face_mesh.process(rgb_image)
        pose_results = self.pose.process(rgb_image)

        # Draw face landmarks first
        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                self.draw_face_landmarks(image, face_landmarks)

        # Draw pose landmarks next
        if pose_results.pose_landmarks:
            self.draw_pose_landmarks(image, pose_results.pose_landmarks)

        # Draw hand landmarks last to ensure they appear on top
        if hands_results.multi_hand_landmarks:
            for hand_landmarks in hands_results.multi_hand_landmarks:
                self.draw_hand_landmarks(image, hand_landmarks)
                features = self.extract_landmarks(hand_landmarks)
                prediction = self.predict_sign_language(features)

                # Add prediction to the list
                if prediction not in self.detected_signs:
                    self.detected_signs.append(prediction)
                if len(self.detected_signs) > 3:  # Limit the list to 3 recent predictions
                    self.detected_signs.pop(0)

                # Update the label with concatenated predictions
                self.ids.prediction_label.text = " ".join(self.detected_signs)

        # Display image in the app
        self.update_camera_texture(image)

    def update_camera_texture(self, image):
        """Update the camera texture."""
        image = cv2.resize(image, (700, 600))
        buf = cv2.flip(image, 0).tobytes()
        texture = Texture.create(size=(image.shape[1], image.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.ids['camera'].texture = texture

    def extract_landmarks(self, hand_landmarks):
        """Extract landmarks for the model."""
        landmarks = []
        for landmark in hand_landmarks.landmark:
            landmarks.append(landmark.x)
            landmarks.append(landmark.y)
            landmarks.append(landmark.z)
        return np.array(landmarks).reshape(1, -1)

    def predict_sign_language(self, features):
        """Predict sign language from features."""
        prediction = self.model.predict(features)
        return prediction[0]

    def draw_hand_landmarks(self, image, hand_landmarks):
        """Draw hand landmarks."""
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
        )

    def draw_face_landmarks(self, image, face_landmarks):
        """Draw face landmarks."""
        mp_drawing.draw_landmarks(
            image=image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1)
        )

    def draw_pose_landmarks(self, image, pose_landmarks):
        """Draw pose landmarks."""
        mp_drawing.draw_landmarks(
            image, pose_landmarks, mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=3),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)
        )

    def on_enter(self):
        self.cap = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def on_leave(self):
        Clock.unschedule(self.update)
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()
