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
- **User Dashboard**: different dashboard for different pages 
- **Investment Opportunities**: Showcase projects to attract funding.  
- **Registration Access**: register your role at one go 
- **Community Resources**: Access articles, tutorials, and tools for modern agriculture.  

## Getting Started  

### Prerequisites  
Before setting up the project, ensure you have the following installed:  
- [Python 3.8+](https://www.python.org/downloads/)  
- [Flask](https://flask.palletsprojects.com/)  
- npm (for managing frontend dependencies)  
- Git
- Docker

### Attention  
This is an ongoing project if you encounter any functional issues, be patient with us as it will be developed very soon.

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

4. Change the port from 80 to 5000 in app.py line 208  if your flask runs on default port of 5000, if not don't change it:  
   ```bash  
    app.run(host='0.0.0.0', port=5000, debug=True)
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

## Deployment  
This project is deployed and hosted on [adaptable.io](https://adaptable.io)

## Testing   
This project is tested using [selenium](https://www.selenium.dev/)
```bash
cd test
```
```bash
python3 seleniumtest.py
```

## Contact  
For any inquiries, feel free to reach out to us on Linkedin at [https://www.linkedin.com/company/uruti/](https://www.linkedin.com/company/uruti/).  
- [Send us a message](mailto:uruti.rw@gmail.com)

## Attention  
This is an ongoing project if you encounter any functional issues, be patient with us as it will be developed very soon.

## Responsiveness
<img src="https://github.com/user-attachments/assets/59f6ea63-6409-470a-ad64-673ae18bb2ab" width="500" />
<img src="https://github.com/user-attachments/assets/47dba72c-a7ec-49a6-af09-8e7796089163" width="200" />
<img src="https://github.com/user-attachments/assets/e63b6138-a329-42e2-9c43-1c6f4f46b886" width="300" />


