from flask import Flask, render_template, jsonify, request
from flask_compress import Compress
from flask_talisman import Talisman
from flask_caching import Cache
import os
import csv
import logging
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Security Configuration
    app.config.update(
    SECRET_KEY=os.getenv('SECRET_KEY', 'dev-key-change-in-production'),
    WTF_CSRF_ENABLED=True,
    SESSION_COOKIE_SECURE=True if os.getenv('ENV') == 'production' else False,
    SESSION_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME=timedelta(hours=1),
    CACHE_TYPE='simple',
    CACHE_DEFAULT_TIMEOUT=300,
    MAIL_SERVER=os.environ.get('MAIL_SERVER') or 'smtp.gmail.com',
    MAIL_PORT=int(os.environ.get('MAIL_PORT') or 587),
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1'],
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER')
)
    
    # Extensions
    Compress(app)
    Cache(app)
    
    # Security headers
    Talisman(app, force_https=False, content_security_policy={
        'default-src': "'self'",
        'script-src': [
            "'self'",
            "'unsafe-inline'",
            "https://cdn.jsdelivr.net",
            "https://cdnjs.cloudflare.com",
            "https://www.googletagmanager.com"
        ],
        'style-src': [
            "'self'",
            "'unsafe-inline'",
            "https://cdn.jsdelivr.net",
            "https://cdnjs.cloudflare.com",
            "https://fonts.googleapis.com"
        ],
        'font-src': [
            "'self'",
            "https://fonts.gstatic.com",
            "https://cdnjs.cloudflare.com"
        ],
        'img-src': ["'self'", "data:", "https:"],
        'connect-src': ["'self'"]
    })
    
    return app

app = create_app()

# Security headers
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

# Data Management Class
class PortfolioData:
    @staticmethod
    def _load_from_csv(file_path, expected_fields):
        if not os.path.exists(file_path):
            logging.warning(f"{file_path} not found. Returning empty list.")
            return []
        
        data = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if not all(field in row for field in expected_fields):
                        logging.warning(f"Skipping invalid row in {file_path}: {row}")
                        continue
                    data.append(row)
        except Exception as e:
            logging.error(f"Error reading {file_path}: {e}")
            return []
        return data

    @staticmethod
    def load_certifications():
        csv_path = os.path.join('data', 'certifications.csv')
        expected_fields = ['title', 'issuer', 'date', 'category', 'url']
        return PortfolioData._load_from_csv(csv_path, expected_fields)

    @staticmethod
    def load_projects():
        csv_path = os.path.join('data', 'projects.csv')
        expected_fields = ['title', 'description', 'tech_stack', 'category', 'github_url', 'demo_url', 'is_current', 'image_url']
        projects_data = PortfolioData._load_from_csv(csv_path, expected_fields)
        
        projects = []
        for row in projects_data:
            project = {
                'title': row['title'] or 'Untitled Project',
                'description': row['description'] or 'No description provided',
                'tech_stack': row['tech_stack'].split(',') if row['tech_stack'] else ['Unknown'],
                'category': row['category'] or 'other',
                'github_url': row['github_url'] or '#',
                'demo_url': row['demo_url'] or '#',
                'is_current': row['is_current'].lower() == 'true',
                'image_url': row['image_url'] or '/static/images/projects/default.png'
            }
            projects.append(project)
        return projects

    @staticmethod
    def load_blog_posts():
        csv_path = os.path.join('data', 'blog_posts.csv')
        expected_fields = ['title', 'date', 'description', 'url', 'image_url']
        return PortfolioData._load_from_csv(csv_path, expected_fields)

    @classmethod
    def get_portfolio_data(cls):
        return {
            'name': 'Adem Youssfi',
            'title': 'AI Expert | Full Stack Developer | Technical Educator',
            'about': "A results-driven Computer Science student with over five years of hands-on experience in full-stack development and AI. I have a proven ability to build high-performance, ML-powered applications, lead technical teams, and educate peers through workshops and technical articles. My experience includes a web development internship where I developed over 22 unique web pages for a large-scale e-commerce marketplace. I am passionate about developing scalable, well-documented software and am always eager to learn new technologies.",
            'experience': [
                {
                    'title': 'Web Development Intern',
                    'description': 'Developed over 22 unique web pages and components for a large-scale e-commerce marketplace project within one month. Contributed to a significant project that has been under continuous development for two years, demonstrating adaptability and rapid integration into existing complex codebase.'
                },
                {
                    'title': 'Technical Educator & Workshop Leader',
                    'description': 'Provided private lessons in algorithmics, problem-solving, and web development. Organized and led comprehensive workshops on Flutter, software design, API/backend architecture, AI/ML, and LLM API integration.'
                },
                {
                    'title': 'Project Team Leader & System Architect',
                    'description': 'Led development teams of 3-5 members in delivering complex software projects from conception to deployment. Created comprehensive system architecture using UML diagrams. Developed detailed API documentation and technical specifications. Implemented software design patterns and best practices.'
                }
            ],
            'education': {
                'degree': "Bachelor of Science in Computer Science",
                'level': 'ISITCom (Higher Institute of Information and Communication Technologies), Sousse, Tunisia. Expected Graduation: June 2025 - Current Year: 3rd Year',
                'courses': 'Relevant Coursework: Data Structures & Algorithms, Database Systems, Software Engineering, Machine Learning, Web Development, Mobile Application Development, Computer Vision'
            },
            'blog_posts': cls.load_blog_posts(),
            'projects': cls.load_projects(),
            'certifications': cls.load_certifications(),
            'contact': {
                'email': 'ademyoussfi57@gmail.com',
                'whatsapp': '+216 55 905 236',
                'whatsapp_url': 'https://wa.me/21655905236',
                'linkedin': 'Adem Youssfi',
                'linkedin_url': 'https://www.linkedin.com/in/adem-youssfi-2289672a4',
                'github': 'Ad2m1109',
                'github_url': 'https://github.com/Ad2m1109',
                'blogger': 'behindthecodebyadem.blogspot.com'
            },
            'stats': {
                'projects_completed': '40+',
                'technologies_mastered': '24+',
                'years_coding': '5+',
                'github_repos': '40+'
            }
        }

# Note: portfolio data is loaded dynamically on each request to reflect CSV updates without restarting

# Routes
@app.route('/')
def index():
    return render_template('index.html', data=PortfolioData.get_portfolio_data())

@app.route('/api/projects')
def api_projects():
    """API endpoint for projects"""
    return jsonify(PortfolioData.get_portfolio_data()['projects'])

@app.route('/api/certifications')
def api_certifications():
    """API endpoint for certifications"""
    return jsonify(PortfolioData.get_portfolio_data()['certifications'])

@app.route('/api/blog')
def api_blog_posts():
    """API endpoint for blog posts"""
    return jsonify(PortfolioData.get_portfolio_data()['blog_posts'])

@app.route('/api/stats')
def api_stats():
    """API endpoint for statistics"""
    return jsonify(PortfolioData.get_portfolio_data()['stats'])


@app.route('/api/version')
def api_version():
    """Return a simple API version for service worker update checks"""
    return jsonify({'version': '1.0.0'})

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, message]):
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Here you would typically send an email or store in database
        # For now, just log the message
        logging.info(f"Contact form submission from {name} ({email}): {message}")
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    
    except Exception as e:
        logging.error(f"Contact form error: {e}")
        return jsonify({'success': False, 'message': 'An error occurred'}), 500

@app.route('/manifest.json')
def manifest():
    """PWA manifest"""
    return jsonify({
        "name": "Adem Youssfi Portfolio",
        "short_name": "AY Portfolio",
        "description": "Portfolio of Adem Youssfi - Computer Science Student",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#2563eb",
        "icons": [
            {
                "src": "/static/images/icon-192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/static/images/icon-512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    })


@app.route('/offline.html')
def offline():
    """Offline fallback page for the PWA"""
    return render_template('offline.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Run app
    app.run(
        host='0.0.0.0', 
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('FLASK_ENV') == 'development'
    )