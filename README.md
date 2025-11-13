# Football Analyzer
## 💻 Tech Stack & Dependencies

This project uses Python and several libraries for **video processing, computer vision, data analysis, and database storage**.

### Core
- **Python 3.11+** → Main programming language.
- **NumPy** → Numerical computations, arrays, vectorized operations.
- **Pandas** → Data processing, CSV/JSON management, statistics calculations.

### Computer Vision
- **OpenCV (opencv-python)** → Video frame extraction and manipulation.
- **YOLOv8 (ultralytics)** → Player and ball object detection.
- **Mediapipe (optional)** → Advanced player tracking (pose estimation, multi-object tracking).

### Video & Image Processing
- **FFmpeg-python** → Video manipulation, generating highlights.
- **Pillow** → Image processing (saving, annotations, thumbnails).
- **Matplotlib** → Visualization, heatmaps of player positions.

### Database
- **PostgreSQL** → Store matches, events, and statistics.
- **psycopg2** → PostgreSQL Python connector for database operations.

### Dev & Environment
- **Python virtual environment (venv)** → Isolated Python environment.
- **Docker (optional)** → Containerization of the full analysis pipeline.
- **Git/GitHub** → Version control and code repository.

### Optional / Future Extensions
- **Streamlit** → Simple interactive dashboard for visualization.
- **Airflow** → Automate batch processing pipelines.

> All dependencies can be installed via `pip install -r requirements.txt`.
