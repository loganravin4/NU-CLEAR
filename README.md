# NU-CLEAR

> **Project Description**  
NU CLEAR is a centralized, data-driven platform that empowers Northeastern students, advisors, and employers by transforming co-op feedback into actionable insights, enabling informed decision-making and continuous improvement for the university’s experiential learning programs.
>
> **Link to application demo:** https://drive.google.com/file/d/1_PiGyZjMVYR2Ahyp5HcwQNAQJU2_POIZ/view?usp=sharing

---

## **Table of Contents**

1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Setup and Installation](#setup-and-installation)  
5. [Running the Project](#running-the-project)  
6. [Environment Variables & Secrets](#environment-variables--secrets)   
7. [Team Members](#team-members)

---

## **Introduction**

**Why does this project exist?**  
Every year, thousands of Northeastern students take on co-op placements, yet the feedback system doesn’t give students, employers, or advisors the insights they need. As a result, students struggle with limited information, employers lack guidance to improve their programs, and advisors can’t access real-time data to support students effectively. Meet NU CLEAR, a data-driven application designed to transform the way Northeastern students, advisors, and co-op employers engage with the acclaimed experiential learning initiative.  

CLEAR collects, analyzes, and presents detailed co-op feedback, allowing students to review co-ops and access other peer insights, helping employers improve their programs, and providing advisors with real-time data to supplement their guidance—all in one place. Unlike basic surveys or feedback forms, CLEAR is a centralized solution that offers personalized dashboards for administrators needing a high-level view of program impact, as well as students looking for peer-to-peer co-op reviews and anonymous feedback to employers to provide movement for change. This platform isn’t just gathering data; it’s contextualizing it to reveal the bigger picture, making experiential learning at Northeastern more transparent, informed, and impactful.

---

## **Features**

In NU-CLEAR, you can act as one of 5 personas or users who may want to use this application. 

### Employer
As an employer, you can view a list of reviews of your specific company, and filter by a variety of factors like minimum rating, role, and the start and end date. You can also view other reviews for other companies to compare against the reviews for your company to better guide decisions on your hiring process and efficiency of HR. 

### Data Analyst
As a data analyst, you can retrieve review data to generate reports and visualizations. You can add a summary report for a company with the company ID, the average rating, and a generated summary. You can also update a report for a company at any time. Another feature includes filtering reviews by student demographics, such as the student's level of co-op experience, year, and major. Lastly, you can add a visualization report, by adding the company ID, visualization type, and filters. You can also update this at any time.

### Student
As a student, you can do a variety of things, such as viewing all co-op listings. You can also view co-op reviews to aid you in your co-op search and filter by the role, minimum rating, minimum salary, start and end date, and whether the reviewer is anonymous and/or if they would recommend the role. You can also create your own co-op review and choose whether or not to post anonymously. You can go back and see the reviews you've posted in the past as well.

### Advisor
As an advisor, you can make, delete, and view announcements to quickly convey information to all students using the site to help them with their job search. Additionally, you can recommend jobs to students and view all reviews that have been posted to better advise students on what to look for in co-ops.

### System Administrator
As a system administrator, you can manage all the users of the site and their permissions. You can also assign modules and manage the co-op listings that have been posted on the site to ensure functional system performance.

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
   git clone https://github.com/your-username/your-project.git](https://github.com/loganravin4/NU-CLEAR.git)
   ```

2. **Setup Environment Variables:**  
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
   docker compose up db -d
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
2. Copy and paste the code from .env.template
3. Edit DB_PASSWORD with a password of your choice:
   ```env
   DB_PASSWORD=your_db_password
   ```

---

## **Team Members**

| **Name**          | **Email**               |  
|--------------------|------------------------|  
| Diya Ganesh      | ganesh.di@northeastern.edu       |  
| Thillainayaki Sudhakar          | sudhakar.th@northeastern.edu     |  
| Logan Ravinuthala      | ravinuthala.l@northeastern.edu    |  
| Diya Kadakia           | kadakia.d@northeastern.edu       |  
| Deekshita Madhalam           | madhalam.d@northeastern.edu       |  

For questions or issues, reach out to **Team NEXUS** at: ganesh.di@northeastern.edu

--- 
