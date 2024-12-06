# NU-CLEAR

> **Project Description**  
E.g., *"An open-source tool to manage and organize personal tasks efficiently."*

---

## **Table of Contents**

1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Setup and Installation](#setup-and-installation)  
5. [Running the Project](#running-the-project)  
6. [Environment Variables & Secrets](#environment-variables--secrets)  
7. [Contributing](#contributing)  
8. [Team Members](#team-members)  
9. [License](#license)

---

## **Introduction**

**Why does this project exist?**  
Provide a short summary of what the project does and its goals.

Every year, thousands of Northeastern students take on co-op placements, yet the feedback system doesn’t give students, employers, or advisors the insights they need. As a result, students struggle with limited information, employers lack guidance to improve their programs, and advisors can’t access real-time data to support students effectively. Meet NU CLEAR, a data-driven application designed to transform the way Northeastern students, advisors, and co-op employers engage with the acclaimed experiential learning initiative.  
CLEAR collects, analyzes, and presents detailed co-op feedback, allowing students to review co-ops and access other peer insights, helping employers improve their programs, and providing advisors with real-time data to supplement their guidance—all in one place. Unlike basic surveys or feedback forms, CLEAR is a centralized solution that offers personalized dashboards for administrators needing a high-level view of program impact, as well as students looking for peer-to-peer co-op reviews and anonymous feedback to employers to provide movement for change. This platform isn’t just gathering data; it’s contextualizing it to reveal the bigger picture, making experiential learning at Northeastern more transparent, informed, and impactful.

---

## **Features**

- Highlight key features and functionality of your project.  
E.g., *"User authentication, task prioritization, email reminders, etc."*

In NU-CLEAR, you can act as one of 5 personas or users who may want to use this application.

---

## **Tech Stack**

| **Technology**    | **Version** |  
|--------------------|-------------|  
| Programming Language | Python 3.9 |  
| Framework          | Streamlit & Flask |  
| Database           | mySQL |  
| Containerization   | Docker |  

---

## **Setup and Installation**

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. **Install Dependencies:**  
   Follow specific commands to install required dependencies.  
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables:**  
   Refer to [Environment Variables & Secrets](#environment-variables--secrets).

---

## **Running the Project**

### **Using Docker**
1. **Build the Docker Image:**  
   ```bash
   docker-compose build
   ```

2. **Run the Containers:**  
   ```bash
   docker compose up -d
   ```

3. **Access the Application:**  
   Visit `http://localhost:8501` in your browser.

---

## **Environment Variables & Secrets**

### **Required Secrets**
List all required secrets and their purposes.

| **Key**            | **Description**              | **Example**          |  
|--------------------|-----------------------------|----------------------|  
| `DB_PASSWORD`      | Database password            | `your_db_password`   |  
| `SECRET_KEY`       | Application secret key       | `random-string`      |  

### **How to Set Secrets:**
1. Create a `.env` file at the root of the project.
2. Add your environment variables:
   ```env
   DB_PASSWORD=your_db_password
   SECRET_KEY=random-string
   ```

---

## **Contributing**

1. Fork the repository.  
2. Create a new feature branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:  
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push the branch:  
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## **Team Members**

| **Name**          | **Role**               |  
|--------------------|------------------------|  
| Alice Johnson      | Project Manager       |  
| Bob Smith          | Backend Developer     |  
| Charlie Davis      | Frontend Developer    |  
| Dana Lee           | DevOps Engineer       |  

---

## **License**

This project is licensed under the MIT License. See `LICENSE` file for details.

---

## **Contact**

For questions or issues, reach out to **Team [Your Project Name]** at:  
- Email: team@example.com  
- GitHub Issues: [GitHub Issues Page](https://github.com/your-username/your-project/issues)

--- 

You can customize this template further based on your project's needs.