<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [SHE CODES] 🎯

## Basic Details

### Team Name: [SHE CODES]

### Team Members
- Member 1: [IRENE JIJO] - [SCMS SCHOOL OF ENGINEERING]
- Member 2: [ADHEENA LAIJU] - [SCMS SCHOOL OF ENGINEERING]

### Hosted Project Link
https://irene4368.github.io/she-codes-tinkherhack-4.0/

### Project Description
[*RoadWatch* is a web-based AI-powered alert system that helps locate missing persons by activating on-road workers like delivery and auto drivers. It generates smart, area-specific alerts with spotting tips to enable faster community response during critical early hours.]

### The Problem statement
[The missing reports once filed are shown in the newspapers which people rarely read thus wasting precious time when someone is missing thus an app which notifies the transport workers who are always on the  road to receive high alerts of missing person and keep th]

### The Solution
[Develop an AI-powered web system that instantly generates area-specific missing person alerts and activates high-visibility road workers like delivery and auto drivers through an “On-The-Road Mode.” This enables faster information spread, structured community participation, and quicker response during the critical early hours of a missing case.]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [HTML,CSS,JavaScript,Firebase]
- Frameworks used: [e.g., React, Django, Spring Boot]
- Libraries used: [e.g., axios, pandas, JUnit]
- Tools used: [ VS Code, Git]

**For Hardware:**
- Main components: [Laptop,internet connection]
- Specifications: [Technical specifications]
- Tools required: [web browser,vs code ,al tool like gemini]

---

## Features

List the key features of your project:
- Feature 1: [1. *Area-Based Selection*
   Users can select a specific area to view relevant missing person cases.]
- Feature 2: [2. *On-The-Road Mode Activation*
   Allows delivery drivers and auto drivers to activate alert mode while traveling.]
- Feature 3: [3. *AI-Generated Alert Messages*
   Uses *Gemini* to generate smart, high-priority alerts with spotting tips.]
- Feature 4: [4. *Cloud-Based Data Storage (Demo)*
   Missing person data is stored in Firebase and fetched dynamically

---
#### Screenshots (Add at least 3)

https://drive.google.com/file/d/1-yvj6y5OhhLkHlDwtDy2VSrTO18xPJGv/view?usp=drive_link
This shows the inside button

https://drive.google.com/file/d/1_znwL66Xd2e9OMtfoHOs0LXNMpR6_UGL/view?usp=drive_link
This shows the code of the project

https://drive.google.com/file/d/1s_IvdNIZMl8jlAYKZ6Z_aRG46MKot6EU/view?usp=drive_link
This shows the main website page
## Implementation

### For Software:

#### Installation
# Clone the repository
git clone https://github.com/YOUR-USERNAME/roadwatch.git
cd roadwatch

# Install Python dependencies
pip install -r requirements.txt

# Requirements include:
# Flask, flask-cors, firebase-admin

#### Run
# Start the Flask backend
python app.py

# The server runs at http://127.0.0.1:5000
# Open index.html directly in your browser
# OR visit the hosted GitHub Pages link
```

---

### For Hardware:
*This is a software-only project. No hardware components required.*

#### Components Required
- A computer or smartphone with a modern web browser (Chrome, Firefox, Edge)
- Internet connection (for Google Fonts and Firebase sync)
- Firebase project (Firestore database — free tier)

#### Circuit Setup
*Not applicable — this is a purely web-based software project.*

---

## Project Documentation

### For Software:

### Screenshots (Add at least 3)

https://drive.google.com/file/d/1_znwL66Xd2e9OMtfoHOs0LXNMpR6_UGL/view?usp=drive_link
This is the code of the website

https://drive.google.com/file/d/1_znwL66Xd2e9OMtfoHOs0LXNMpR6_UGL/view?usp=drive_link
this shows the interface after main page

https://drive.google.com/file/d/1_znwL66Xd2e9OMtfoHOs0LXNMpR6_UGL/view?usp=drive_link
This shows the main page

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
```
┌─────────────────────────────────────────────────────┐
│                   USER BROWSER                      │
│                                                     │
│  ┌───────────┐  ┌──────────────┐  ┌───────────────┐ │
│  │  Officer  │  │    Public    │  │   Transport   │ │
│  │  Portal   │  │    Search    │  │  Alert Portal │ │
│  └─────┬─────┘  └──────┬───────┘  └───────┬───────┘ │
│        │               │                  │         │
│        └───────────────┼──────────────────┘         │
│                        │                            │
│              localStorage (browser)                 │
└────────────────────────┼────────────────────────────┘
                         │ fetch (optional)
                         ▼
              ┌──────────────────┐
              │  Flask Backend   │
              │   (app.py)       │
              │  Python + CORS   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  Firebase        │
              │  Firestore DB    │
              │(cases collection)│
              └──────────────────┘
```
*The frontend is a single HTML file with three portals. Data is stored in browser localStorage for instant offline use, and optionally synced to Firebase Firestore via the Flask backend.*

**Application Workflow:**

![Workflow](docs/workflow.png)
```
Officer Registers/Logs In
        │
        ▼
Files Missing Person Case
(Name, Age, Photo, Location, District)
        │
        ▼
System Auto-assigns Urgency
  Age < 18 or > 75 → 🔴 HIGH
  Others           → 🟡 MEDIUM
        │
        ├──────────────────────────────────┐
        ▼                                  ▼
Case saved to localStorage         POST to Firebase
(instant, works offline)           via Flask backend
        │
        ├─────────────────┬────────────────────────┐
        ▼                 ▼                         ▼
  Public Search    Transport Workers          Officer sees
  can find the     in that district           case in their
  person by        see the alert with         filed cases
  name/district    photo + officer            list
                   contact number
---





## Project Demo

### Video
https://drive.google.com/file/d/1bugpIJlkijUEblf8ZO2XPPIP835ovR-d/view?usp=drive_link
This shows the proper workflow of the working of website from main page to sub pages. From officer and transport controls to logins and registers






## Team Contributions

- Irene: Backend and frontend
  Adheena: Documentation and firebase connection
- 

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
