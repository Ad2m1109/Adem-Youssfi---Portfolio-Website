# Adem Youssfi - Portfolio Website

A technical portfolio and research platform documenting high-performance systems, AI orchestration, and assistive technology development.

**Live Site**: [ademyoussfi.onrender.com](https://ademyoussfi.onrender.com/)

---

## Purpose

This platform serves as a central engineering hub for showcasing applied research and production systems across three core domains:

- **High-Performance Computing**: Optimized C++ systems leveraging TensorRT and CUDA for real-time inference
- **AI Orchestration**: End-to-end ML pipelines integrating computer vision, NLP, and deployment infrastructure
- **Assistive Technology**: Mobile applications addressing accessibility challenges in healthcare and education

The site functions as both a project portfolio and a technical knowledge base, documenting architectural decisions, performance benchmarks, and lessons learned from building scalable systems.

---

## Tech Stack

### Backend
- **Flask** (Python 3.8+) - Application server
- **Flask-Compress** - Response compression
- **Flask-Caching** - Performance optimization
- **CSV** - Lightweight data storage

### Frontend
- **HTML5/CSS3** - Semantic markup and responsive design
- **JavaScript (ES6+)** - Interactive UI components
- **Bootstrap 5** - Grid system and utilities
- **Font Awesome** - Iconography

### Infrastructure
- **Render** - Cloud deployment platform
- **Gunicorn** - WSGI HTTP server
- **GitHub Actions** - CI/CD pipeline

---

## Core Sections

### Projects Portfolio

The platform showcases production-ready systems and research prototypes:

#### **Coach Pro**
AI-powered football analytics backend featuring:
- YOLOv8-based player tracking and tactical analysis
- Real-time match event detection
- RESTful API for mobile client integration

**Repository**: [Coach-Pro-Backend](https://github.com/Ad2m1109/Coach-Pro-Backend)

#### **Harmonia**
Assistive mobile application for Alzheimer's patients and caregivers:
- Flutter-based cross-platform architecture
- Firebase integration for real-time synchronization
- Cognitive assistance features and medication tracking

**Repository**: [Harmonia](https://github.com/Ad2m1109/Harmonia)

#### **Additional Projects**
- **Football Analytics AI**: C++ tool with TensorRT optimization for high-throughput video processing
- **Gemini GUI Agent**: Desktop automation leveraging Google's Gemini API
- **Phone-to-Graphic-Tablet**: Cross-platform drawing solution with low-latency input handling

### Technical Blog

Engineering notes and deep dives covering:
- **C++ Optimization**: Template metaprogramming, memory management, and SIMD vectorization
- **AI Infrastructure**: Model quantization, inference optimization, and deployment strategies
- **System Design**: Microservices architecture, API design patterns, and scalability considerations

---

## Navigation

### Project Repositories
- [Coach Pro Backend](https://github.com/Ad2m1109/Coach-Pro-Backend) - YOLOv8 Football Analytics
- [Harmonia](https://github.com/Ad2m1109/Harmonia) - Alzheimer's Support App
- [Football Analytics AI](https://github.com/Ad2m1109/Football-Analytics-AI) - C++ Computer Vision System
- [DragNDropTeX](https://github.com/Ad2m1109/DragNDropTeX) - No-Code LaTeX Editor
- [Mr. Grammar](https://github.com/Ad2m1109/Mr-Grammar) - AI Writing Assistant

### Additional Resources
- **Full Project Portfolio**: [GitHub Profile](https://github.com/Ad2m1109)
- **Professional Network**: [LinkedIn](https://www.linkedin.com/in/adem-youssfi-2289672a4)
- **Contact**: ademyoussfi57@gmail.com

---

## Vision

This platform documents a progression toward advanced research in Computer Science, with focus areas in:

- **Efficient AI Systems**: Bridging the gap between model accuracy and production constraints
- **Real-Time Computing**: Optimizing latency-critical applications for edge deployment
- **Human-Centered Design**: Building technology that addresses genuine accessibility challenges

Each project represents an iteration in understanding the full lifecycle of software systems—from initial research and prototyping to production deployment and maintenance. The technical blog serves as a knowledge repository, capturing insights that emerge from hands-on implementation.

The goal is not merely to showcase completed work, but to demonstrate a methodical approach to problem-solving, an understanding of performance-accuracy tradeoffs, and a commitment to engineering rigor.

---

## Local Development

```bash
# Clone repository
git clone https://github.com/Ad2m1109/my-portfolio-website.git
cd my-portfolio-website

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```

Access the site at `http://localhost:5000`

---

## Project Structure

```
.
├── app.py                  # Flask application
├── templates/              # HTML templates
├── static/
│   ├── style.css          # Core styles
│   ├── app.js             # Client-side logic
│   └── images/projects/   # Project assets
├── data/
│   ├── projects.csv       # Project metadata
│   └── certifications.csv # Credentials
└── requirements.txt        # Python dependencies
```

---

## Contributing

This repository primarily serves as a personal engineering portfolio. However, suggestions for technical improvements—particularly regarding performance optimization, accessibility, or code quality—are welcome via GitHub Issues.

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

**Built with focus on engineering excellence and clarity of communication.**

*Documenting the intersection of theoretical computer science and practical system implementation.*
