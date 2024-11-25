![Uruti-logo-e1732096555217](https://github.com/user-attachments/assets/18f917ec-4fe7-46e7-9942-51426c50c06a) 

**Connecting Young Rwandans in Agriculture with Opportunities**  

## Introduction  

Uruti is a web platform designed to bridge the gap between young Rwandans in agriculture and potential investors, mentors, and resources. With a focus on fostering AgriTech innovation, Uruti aims to empower youth to drive agricultural transformation in Rwanda through mentorship, funding opportunities, and community engagement.  

## Why Uruti?  

Agriculture remains a critical sector for Rwanda's economy, yet young people often face challenges such as:  
- Lack of access to investment and funding.  
- Limited mentorship and knowledge-sharing opportunities.  
- Difficulty in accessing modern agricultural resources and technology.  

Uruti provides a one-stop platform to address these challenges by:  
- Connecting users with investors and mentors.  
- Offering resources to enhance agricultural practices.  
- Promoting AgriTech solutions for sustainable growth.  

## Features  
- **User Dashboard**: Manage profiles, projects, and interactions.  
- **Investment Opportunities**: Showcase projects to attract funding.  
- **Mentorship Access**: Connect with experienced mentors in agriculture.  
- **Community Resources**: Access articles, tutorials, and tools for modern agriculture.  

## Getting Started  

### Prerequisites  
Before setting up the project, ensure you have the following installed:  
- [Python 3.8+](https://www.python.org/downloads/)  
- [Flask](https://flask.palletsprojects.com/)  
- npm (for managing frontend dependencies)  
- Git
- Docker

### Repository Setup  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/NiyonshutiDavid/uruti.git  
   cd uruti  
   ```  

2. Create a virtual environment and activate it:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # For Linux/Mac  
   venv\Scripts\activate     # For Windows  
   ```  

3. Install backend dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Install frontend dependencies:  
   ```bash  
   cd frontend  
   npm install  
   ```  

5. Set up the database:  
   ```bash  
   flask db init  
   flask db migrate  
   flask db upgrade  
   ```  

6. Run the development server:  
   ```bash  
   python3 app.py  
   ```  

7. Access the platform at `http://127.0.0.1:5000`.  

## Dependencies  

### Backend  
- Flask  
- SQLAlchemy  
- Flask-Migrate  
- Flask-Bcrypt (for authentication)  

### Frontend  
- HTML  
- CSS
- Javascript

## Contributing  
Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a new branch:  
   ```bash  
   git checkout -b feature/your-feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add your feature description"  
   ```  
4. Push to the branch:  
   ```bash  
   git push origin feature/your-feature-name  
   ```  
5. Open a pull request.  

## License  
This project is licensed under the MIT License. See the LICENSE file for more details.  

## Contact  
For any inquiries, feel free to reach out to us on Linkedin at `https://www.linkedin.com/company/uruti/`.  
