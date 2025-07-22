# Face Recognition System for SLiMS Integration

A real-time face recognition system built with OpenCV and face_recognition library, integrated with SLiMS (Senayan Library Management System) using Firebase for database and storage management.

## 🎯 Overview

This system provides automated face recognition capabilities for library management, allowing seamless identification of library members through webcam integration. The system connects with SLiMS for member management and uses Firebase for real-time data synchronization and face encoding storage.

## 🚀 Features

- **Real-time Face Detection**: Live face detection using webcam feed
- **Face Recognition**: Accurate face matching using deep learning models
- **SLiMS Integration**: Seamless connection with library management system
- **Firebase Backend**: Real-time database and cloud storage
- **Member Management**: Automatic member identification and logging
- **Attendance Tracking**: Record member visits and library usage
- **Multi-face Support**: Handle multiple faces in single frame
- **High Accuracy**: Advanced face encoding algorithms

## 🛠️ Technologies Used

- **Python 3.8+**
- **OpenCV 4.x**: Computer vision and image processing
- **face_recognition**: Face encoding and recognition
- **Firebase Admin SDK**: Database and storage integration
- **SLiMS API**: Library system integration
- **NumPy**: Numerical computations
- **Pillow**: Image processing utilities

## 📋 Prerequisites

- Python 3.8 or higher
- Webcam/Camera device
- Firebase project with Realtime Database and Storage
- SLiMS installation with API access
- Git for version control

### System Requirements

- **OS**: Windows 10/11, macOS 10.14+, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Camera**: USB webcam or built-in camera
- **Internet**: Stable connection for Firebase sync

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/face-recognition-slims.git
cd face-recognition-slims
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Additional Requirements

For face_recognition library, you may need to install additional dependencies:

#### Windows
```bash
pip install cmake
pip install dlib
pip install face_recognition
```

#### macOS
```bash
brew install cmake
pip install dlib
pip install face_recognition
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install cmake
sudo apt-get install python3-dev
pip install dlib
pip install face_recognition
```

## ⚙️ Configuration

### 1. Firebase Setup

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
2. Enable Realtime Database and Storage
3. Generate service account key:
   - Go to Project Settings → Service Accounts
   - Generate new private key
   - Download the JSON file as `firebase-credentials.json`
4. Place the credentials file in the project root directory

### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
# Firebase Configuration
FIREBASE_CREDENTIALS_PATH=./firebase-credentials.json
FIREBASE_DATABASE_URL=https://your-project-default-rtdb.firebaseio.com/
FIREBASE_STORAGE_BUCKET=your-project.appspot.com

# SLiMS Configuration
SLIMS_BASE_URL=http://your-slims-installation.com
SLIMS_API_KEY=your-api-key-here
SLIMS_USERNAME=your-username
SLIMS_PASSWORD=your-password

# Camera Configuration
CAMERA_INDEX=0
FRAME_WIDTH=640
FRAME_HEIGHT=480
RECOGNITION_THRESHOLD=0.6

# Application Settings
DEBUG_MODE=False
LOG_LEVEL=INFO
FACE_ENCODINGS_PATH=./data/encodings/
TEMP_IMAGES_PATH=./temp/
```

### 3. SLiMS API Configuration

Ensure your SLiMS installation has:
- API module enabled
- Proper authentication configured
- Member data accessible via API endpoints

### 4. Database Structure

The Firebase Realtime Database should follow this structure:

```json
{
  "members": {
    "member_id": {
      "name": "Member Name",
      "member_id": "M001",
      "email": "member@email.com",
      "face_encoding": "base64_encoded_string",
      "created_at": "timestamp",
      "last_seen": "timestamp",
      "is_active": true
    }
  },
  "attendance": {
    "date": {
      "member_id": {
        "timestamp": "entry_time",
        "confidence": 0.95
      }
    }
  }
}
```

## 📁 Project Structure

```
face-recognition-slims/
├── src/
│   ├── __init__.py
│   ├── face_recognition_system.py
│   ├── firebase_manager.py
│   ├── slims_integration.py
│   ├── camera_manager.py
│   └── utils/
│       ├── __init__.py
│       ├── image_processing.py
│       └── logging_config.py
├── data/
│   ├── encodings/
│   └── models/
├── temp/
├── config/
│   └── settings.py
├── tests/
│   ├── test_face_recognition.py
│   ├── test_firebase.py
│   └── test_slims_integration.py
├── docs/
│   └── api_documentation.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup.py
└── README.md
```

## 🚦 Usage

### Basic Usage

```bash
python main.py
```

### Command Line Options

```bash
# Run with specific camera
python main.py --camera 0

# Run in debug mode
python main.py --debug

# Train new face encodings
python main.py --train

# Sync with SLiMS database
python main.py --sync-slims
```

### Training New Faces

1. **Add Member Photos**:
   ```bash
   python scripts/add_member.py --name "John Doe" --id "M001" --image "path/to/photo.jpg"
   ```

2. **Batch Training**:
   ```bash
   python scripts/batch_train.py --members-csv "members.csv"
   ```

3. **Sync from SLiMS**:
   ```bash
   python scripts/sync_members.py
   ```

### API Usage

```python
from src.face_recognition_system import FaceRecognitionSystem

# Initialize system
system = FaceRecognitionSystem()

# Start recognition
system.start_recognition()

# Add new member
system.add_member(name="Jane Doe", member_id="M002", image_path="photo.jpg")

# Get recognition results
results = system.get_recent_detections()
```

## 🔌 SLiMS Integration

### API Endpoints Used

- `GET /api/members` - Fetch member list
- `GET /api/members/{id}` - Get member details
- `POST /api/attendance` - Log member attendance
- `PUT /api/members/{id}` - Update member information

### Sync Process

1. **Initial Sync**: Download all active members from SLiMS
2. **Face Encoding**: Generate encodings for member photos
3. **Firebase Upload**: Store encodings in Firebase
4. **Real-time Updates**: Monitor changes and sync automatically

## 🔥 Firebase Integration

### Realtime Database Operations

- **Member Management**: Store and retrieve member data
- **Attendance Logging**: Real-time attendance records
- **Face Encodings**: Secure storage of face data
- **Sync Status**: Track synchronization with SLiMS

### Storage Operations

- **Image Storage**: Original member photos
- **Backup Data**: Encrypted face encodings
- **Log Files**: System operation logs

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_face_recognition.py

# Run with coverage
pytest --cov=src tests/
```

### Test Coverage

- Face detection accuracy tests
- Firebase connection tests
- SLiMS API integration tests
- Camera functionality tests
- Performance benchmarks

## 📊 Performance Optimization

### Recommended Settings

```python
# config/settings.py
PERFORMANCE_CONFIG = {
    'FRAME_SKIP': 2,  # Process every 2nd frame
    'FACE_LOCATIONS_MODEL': 'hog',  # Use HOG for speed
    'NUM_JITTERS': 1,  # Reduce for speed
    'TOLERANCE': 0.6,  # Adjust for accuracy vs speed
    'RESIZE_FACTOR': 0.5  # Resize frames for processing
}
```

### Hardware Recommendations

- **CPU**: Intel i5 8th gen or AMD Ryzen 5 3600+
- **GPU**: Optional CUDA-compatible GPU for faster processing
- **Camera**: 720p minimum, 1080p recommended

## 🔒 Security Considerations

- **Data Encryption**: Face encodings are encrypted before storage
- **API Security**: All API calls use authentication tokens
- **Access Control**: Member data access is role-based
- **Privacy Compliance**: Follows data protection regulations

## 🐛 Troubleshooting

### Common Issues

1. **Camera Not Found**:
   ```bash
   # List available cameras
   python scripts/list_cameras.py
   ```

2. **Face Recognition Low Accuracy**:
   - Check lighting conditions
   - Verify face encoding quality
   - Adjust recognition threshold

3. **Firebase Connection Issues**:
   - Verify credentials file
   - Check internet connection
   - Validate database URL

4. **SLiMS API Errors**:
   - Confirm API endpoint availability
   - Check authentication credentials
   - Verify API permissions

### Debug Mode

Enable debug mode for detailed logging:

```bash
python main.py --debug
```

## 📈 Monitoring and Logging

### Log Files

- `logs/system.log` - General system logs
- `logs/recognition.log` - Face recognition events
- `logs/firebase.log` - Firebase operations
- `logs/slims.log` - SLiMS integration logs

### Metrics Tracking

- Recognition accuracy rates
- Response times
- Database sync status
- Member attendance patterns

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run pre-commit hooks
pre-commit install

# Run linting
flake8 src/
black src/

# Run type checking
mypy src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors and Acknowledgments

- **Your Name** - Initial work - [YourGitHub](https://github.com/yourusername)
- **Contributors** - See [CONTRIBUTORS.md](CONTRIBUTORS.md)

### Special Thanks

- OpenCV community for computer vision tools
- face_recognition library by Adam Geitgey
- Firebase team for cloud services
- SLiMS development team

## 📞 Support

For support and questions:

- **Email**: support@yourproject.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/face-recognition-slims/issues)
- **Documentation**: [Wiki](https://github.com/yourusername/face-recognition-slims/wiki)
- **Discord**: [Project Discord Server](https://discord.gg/yourserver)

## 🗺️ Roadmap

### Version 2.0 Features

- [ ] Mobile app integration
- [ ] Advanced analytics dashboard
- [ ] Multi-library support
- [ ] Enhanced security features
- [ ] Cloud deployment options
- [ ] REST API for third-party integration

### Long-term Goals

- AI-powered library recommendations
- Facial emotion recognition for user experience
- Integration with more library management systems
- Advanced reporting and analytics
- Mobile SDK development

---

**Note**: This system is designed for educational and library management purposes. Ensure compliance with local privacy laws and regulations when implementing face recognition technology.