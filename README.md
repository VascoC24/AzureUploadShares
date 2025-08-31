# 📂 Azure File Sharing Website

This project is a web application that enables users to share files via **Azure** using **SAS Tokens**, **Azure Blob Storage**, and **Flask**.

---

## 📜 Project Overview

The application allows users to upload files through a Flask-based website, store them in Azure Blob Storage, and generate time-limited sharing links.  
It has evolved through several development stages, adding new features.

---

## 🛠 Development Stages

### **Step 1 — Initial Flask Application**
- Built a simple Flask website in Python to allow users to upload files locally.
- Core code:
  - Frontend: `index.html`, `result.html`, `uploadpage.html`
  - Backend API: `application.py`

### **Step 2 — File uploading to Azure**
- Added Azure Containers to the app so files would be uploaded into blobs
- Used **Access Keys**, **Connection Strings**, and **Storage Account Keys**.

### **Step 3 — SAS Token Integration**
- Implemented **Shared Access Signatures (SAS)**.
- Files are now accessible through links and for only **1 hour**, ensuring time-limited sharing.

### **Step 4 — Azure Web App Deployment**
- Deployed the application to Azure Web Apps on a **Linux-based plan**.
- Used the **F1 Free Pricing Plan** mainly for testing small apps.

### **Step 5 — Automatic File Deletion** *(In Development)*
- Implementing automatic deletion of files **1 hour after creation** to optimize storage usage.

### **Step 6 — CI/CD Pipeline** *(In Development)*
- Setting up **GitHub Actions** for continuous integration and deployment.
- Upgraded Azure plan since the free tier does not support CI/CD.

### **Step 7 — Custom Domain & SSL** *(In Development)*
- Planning to configure a **custom domain** with **SSL certification** for secure access.

---

## 🚀 Technologies Used
- **Python** (Flask)
- **HTML / CSS**
- **Azure Blob Storage**
- **Azure Web Apps**
- **SAS Tokens**
- **GitHub Actions** (CI/CD)

---

## 📄 License
This project is licensed under the MIT License.
