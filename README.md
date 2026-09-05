# Mentora — AI-Powered Learning & Tutor Marketplace

> **Learn with the right course. Find the right mentor. Reach your goal.**

Mentora is an **AI-powered learning and tutoring marketplace** that connects students with expert tutors while providing personalized learning paths, course-based AI assistance, and intelligent tutor/course recommendations.

Unlike traditional course platforms that primarily ask *"Which course do you want to buy?"*, Mentora focuses on a more important question:

> **"What do you need to learn, how should you learn it, and when do you need human guidance?"**

The platform combines **online courses, 1-to-1 tutoring, AI recommendations, RAG-based learning assistance, assessments, progress tracking, and payments** into a single ecosystem.

---

## 🎯 Problem Statement

Online learning platforms provide thousands of courses, but this creates several problems:

* Students struggle to choose the right course.
* Finding a tutor suited to a student's specific needs is difficult.
* Students often don't know what they should learn next.
* Generic AI assistants may provide answers unrelated to the student's actual course material.
* Students can complete courses without actually understanding the concepts.
* Tutors have limited tools to organize courses, materials, assessments, and students.
* Students who need personalized human assistance have to search for tutors separately.

Mentora addresses these problems by combining **AI-driven personalization with human tutoring**.

---

# 💡 Core Idea

Mentora is built around a simple learning cycle:

```text
                    STUDENT
                       │
                 Learning Goal
                       │
                       ▼
                AI Assessment
                       │
                       ▼
             Personalized Path
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
       Courses                    Tutors
          │                         │
          └────────────┬────────────┘
                       ▼
                     Learn
                       │
                       ▼
                AI Course Assistant
                       │
                       ▼
                 Assess Progress
                       │
                       ▼
              Identify Weak Areas
                       │
              ┌────────┴────────┐
              ▼                 ▼
         More Learning      Human Tutor
                                │
                                ▼
                         Book + Pay
                                │
                                ▼
                           Improve
```

The goal is not simply to sell courses.

**The goal is to help students achieve learning outcomes.**

---

# 👥 User Roles

Mentora supports three primary roles.

## 🎓 Student

Students can:

* Create an account
* Define learning goals
* Browse courses
* Search and filter tutors
* Receive AI-powered recommendations
* Enroll in courses
* Purchase courses
* Access course materials
* Ask questions using Course AI
* Take quizzes and assessments
* Track learning progress
* Identify weak areas
* Book 1-to-1 tutoring sessions
* Make payments
* Review tutors and courses

---

## 👨‍🏫 Tutor

Tutors can:

* Create a tutor profile
* Add expertise and subjects
* Submit verification information
* Create courses
* Upload course materials
* Upload syllabus PDFs
* Create modules and lessons
* Create quizzes
* Set course prices
* Set tutoring rates
* Define availability
* Accept tutoring bookings
* View enrolled students
* Track course performance
* View earnings

---

## 🛡️ Admin

Administrators can:

* Manage students
* Manage tutors
* Verify tutor applications
* Manage courses
* Manage categories
* Monitor payments
* Handle reports
* View platform analytics
* Moderate reviews
* Suspend inappropriate accounts/content

---

# 📚 Course System

Tutors can create structured courses.

```text
Course
│
├── Course Information
│   ├── Title
│   ├── Description
│   ├── Category
│   ├── Difficulty
│   ├── Price
│   └── Syllabus
│
├── Module 1
│   ├── Lesson 1
│   ├── Lesson 2
│   └── Quiz
│
├── Module 2
│   ├── Lesson 3
│   ├── Lesson 4
│   └── Assignment
│
└── Final Assessment
```

Courses can contain:

* PDF notes
* Syllabus documents
* Recorded videos
* Assignments
* Quizzes
* Reference materials
* Additional resources

Live streaming is **not required**.

The platform focuses on structured learning and optional 1-to-1 tutoring.

---

# 🧑‍🏫 Tutor Marketplace

Students can search for tutors based on:

* Subject
* Skill
* Experience
* Rating
* Price
* Difficulty level
* Availability
* Teaching preferences

Instead of showing hundreds of tutors, Mentora can use its recommendation engine to identify the most suitable tutors.

Example:

```text
YOUR BEST MATCHES

🥇 Priya
94% Match
SQL + Power BI
₹400/hour
⭐ 4.9

🥈 Rahul
88% Match
SQL + Statistics
₹350/hour
⭐ 4.8

🥉 Ananya
83% Match
Data Analytics
₹500/hour
⭐ 4.9
```

---

# 📅 1-to-1 Tutoring

Students can book individual tutoring sessions.

```text
Student
   ↓
Select Tutor
   ↓
Select Date
   ↓
Select Available Time
   ↓
Payment
   ↓
Booking Confirmed
   ↓
Online Session
```

The platform handles:

* Availability
* Scheduling
* Booking
* Payment
* Meeting information
* Booking history

The actual video/audio call can initially use an external meeting service.

Native calling using WebRTC can be added as an advanced feature.

---

# 💳 Payment System

Students can purchase courses or tutoring sessions.

Example:

```text
Course Price = ₹1,000

Student
   │
   ▼
Payment
   │
   ▼
Payment Verification
   │
   ▼
Order = PAID
   │
   ▼
Enrollment Created
```

For tutoring:

```text
Tutor Rate = ₹500/hour

Student books 1 hour
        ↓
Payment
        ↓
Booking confirmed
```

The platform can also support tutor commissions.

Example:

```text
Student Payment     ₹1,000
Platform Commission    ₹100
Tutor Earnings         ₹900
```

For the college project, payments can initially be implemented using a mock payment flow and later integrated with a real payment gateway.

---

# 🤖 AI Features

AI is not implemented merely as a generic chatbot.

It is integrated into the actual learning workflow.

---

## 1. AI Course & Tutor Recommendation

The recommendation engine considers:

* Student interests
* Learning goals
* Current skill level
* Completed courses
* Quiz performance
* Course topics
* Tutor expertise
* Tutor ratings
* Price
* Availability

It produces personalized recommendations.

```text
Student Profile
      +
Learning Goal
      +
Course Data
      +
Tutor Data
      +
Learning History
      ↓
Recommendation Engine
      ↓
Personalized Courses & Tutors
```

A hybrid recommendation approach can combine:

* Content similarity
* User preferences
* Course ratings
* Previous interactions
* Embedding similarity

---

# 📄 2. RAG-Based Course AI

Mentora includes a **Retrieval-Augmented Generation (RAG)** system.

Tutors can upload:

* PDFs
* Notes
* Syllabus
* Course documents
* Reference material

The documents are processed and indexed.

```text
PDF
 ↓
Text Extraction
 ↓
Cleaning
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
```

When a student asks a question:

```text
Student Question
       ↓
Question Embedding
       ↓
Vector Search
       ↓
Relevant Course Chunks
       ↓
LLM
       ↓
Context-Aware Answer
```

Example:

> "Explain normalization according to my DBMS course."

The system retrieves relevant content from that specific course and generates an answer based on the retrieved material.

The response can also provide document/page references.

---

# 🔐 Course-Isolated RAG

A key part of the architecture is keeping course information separated.

For example:

```text
Vector Database

Course A
 ├── Physics Notes
 ├── Physics Syllabus
 └── Assignments

Course B
 ├── DBMS Notes
 ├── DBMS Syllabus
 └── Assignments

Course C
 ├── Python Notes
 └── Python Exercises
```

When a student asks a question inside Course B, retrieval can be restricted using:

```text
course_id = Course_B
```

This prevents irrelevant documents from other courses from being retrieved.

---

# 🧠 3. Personalized Learning Assistant

Mentora combines RAG with student progress.

Example:

```text
Student Progress
       +
Quiz Results
       +
Course Content
       +
Learning Goal
       ↓
AI Learning Assistant
```

The AI can identify weak areas.

Example:

> You completed SQL Joins, but your recent quiz performance indicates difficulty with aggregation. Review the Aggregation module before moving to Subqueries.

The student can then:

```text
Review Material
       OR
Ask AI
       OR
Book Tutor
```

This creates a bridge between **AI assistance and human tutoring**.

---

# 📝 4. AI Quiz Generation

Tutors can upload course material and request:

> Generate a 10-question quiz on this module.

AI generates draft questions based on the material.

The tutor reviews and approves them before publishing.

```text
Course Material
      ↓
AI
      ↓
Quiz Draft
      ↓
Tutor Review
      ↓
Publish
```

Human approval is required to prevent incorrect AI-generated educational content from being published automatically.

---

# 🎯 Personalized Learning Path

A student can specify a goal.

Example:

> "I want to become a Data Analyst in 3 months."

Mentora analyzes the student's current knowledge and generates a roadmap.

```text
Data Analyst Goal
       ↓
Current Skill Assessment
       ↓
Skill Gap Analysis
       ↓
Learning Roadmap

Excel
  ↓
SQL
  ↓
Advanced SQL
  ↓
Statistics
  ↓
Python
  ↓
Pandas
  ↓
Visualization
  ↓
Projects
```

The platform can then recommend appropriate courses and tutors for each stage.

---

# 📊 Progress Tracking

Student progress is tracked at the lesson level.

```text
DBMS

████████████░░░░ 75%

✓ Introduction
✓ ER Model
✓ Relational Model
✓ SQL
✓ Joins
○ Transactions
○ Normalization
```

The system can calculate:

```text
Progress =
Completed Lessons / Total Lessons × 100
```

Quiz performance can also contribute to the student's learning profile.

---

# ⭐ Reviews & Ratings

Students can review:

* Courses
* Tutors

Example:

```text
Course Rating: ⭐ 4.8

Teaching Quality: ⭐⭐⭐⭐⭐
Course Material:  ⭐⭐⭐⭐
Difficulty:       ⭐⭐⭐⭐⭐
```

Reviews can help both:

* Future students choose courses/tutors
* The recommendation engine improve its ranking

---

# 🗄️ Database Design

A relational database can contain entities such as:

```text
USER
 │
 ├───────────────┐
 ↓               ↓
STUDENT         TUTOR
                  │
                  ↓
                COURSE
                  │
                  ↓
                MODULE
                  │
                  ↓
                LESSON
                  │
            ┌─────┴─────┐
            ↓           ↓
        MATERIAL       QUIZ
                         │
                         ↓
                     QUESTION
```

Additional relationships:

```text
STUDENT
   ↓
ENROLLMENT
   ↓
COURSE

STUDENT
   ↓
BOOKING
   ↓
TUTOR

STUDENT
   ↓
ORDER
   ↓
PAYMENT

STUDENT
   ↓
REVIEW
   ↓
COURSE / TUTOR

STUDENT
   ↓
PROGRESS
   ↓
LESSON
```

---

# 📦 File Storage

Large files such as PDFs and videos do not need to be stored directly inside the relational database.

Recommended architecture:

```text
PostgreSQL / MySQL
       │
       ├── Course metadata
       ├── User information
       ├── Enrollment
       ├── Payment
       ├── Progress
       └── File metadata + URL
       
Object Storage
       │
       ├── PDFs
       ├── Notes
       └── Videos
```

The database stores information such as:

```text
file_id
course_id
file_name
file_type
file_url
uploaded_at
```

---

# 🏗️ High-Level Architecture

```text
                         FRONTEND
                            │
                            ▼
                       REST API
                            │
                 ┌──────────┼──────────┐
                 ↓          ↓          ↓
             Auth API   Course API   Booking API
                 │          │          │
                 └──────────┼──────────┘
                            ↓
                      APPLICATION
                         SERVER
                            │
        ┌───────────────────┼──────────────────┐
        ↓                   ↓                  ↓
   SQL Database       Object Storage       Vector DB
        │                   │                  │
        ↓                   ↓                  ↓
 Users/Courses          PDFs/Videos      Embeddings
 Payments              Documents          RAG Data
 Bookings
 Progress
                            │
                            ▼
                       AI SERVICES
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
             RAG       Recommendations   LLM
```

---

# 🔒 Authentication & Authorization

Mentora uses role-based access control.

```text
USER
 │
 ├── STUDENT
 ├── TUTOR
 └── ADMIN
```

Examples:

* Students cannot create courses.
* Tutors cannot access admin controls.
* Only verified tutors can publish courses.
* Only enrolled students can access paid course content.
* Only participants of a tutoring session can access its meeting information.
* Only authorized users can access course-specific RAG content.

---

# 🔄 Core Workflows

## Student Enrollment

```text
Browse Course
     ↓
View Course
     ↓
Enroll
     ↓
Payment
     ↓
Payment Verification
     ↓
Create Enrollment
     ↓
Access Course
```

## Tutor Course Creation

```text
Tutor Registration
       ↓
Verification
       ↓
Create Course
       ↓
Add Modules
       ↓
Add Lessons
       ↓
Upload Materials
       ↓
Create Quiz
       ↓
Publish
```

## AI Question Answering

```text
Question
   ↓
Authenticate Student
   ↓
Identify Course
   ↓
Generate Query Embedding
   ↓
Filter by Course
   ↓
Vector Search
   ↓
Retrieve Relevant Chunks
   ↓
LLM
   ↓
Answer + Sources
```

## Tutor Booking

```text
Find Tutor
   ↓
View Availability
   ↓
Select Slot
   ↓
Create Booking
   ↓
Payment
   ↓
Confirm Booking
   ↓
Online Session
```

---

# 🧰 Suggested Technology Stack

The project can be implemented using:

### Frontend

* React
* Next.js
* Tailwind CSS

### Backend

* Node.js
* Express.js

or:

* Python
* FastAPI

### Database

* PostgreSQL

### Authentication

* JWT
* OAuth (optional)

### File Storage

* AWS S3
* Cloudinary
* Firebase Storage
* Local storage for development

### Vector Database

* PostgreSQL + pgvector
* Pinecone
* Chroma
* Weaviate

For a college project, **PostgreSQL + pgvector** is particularly attractive because it allows relational data and vector search to coexist in one database system.

### AI

* LLM API
* Embedding model
* RAG pipeline
* Recommendation engine

### Payments

* Razorpay / Stripe for production
* Mock payment gateway for initial development

### Communication

* External meeting provider initially
* WebRTC as an advanced extension

---

# 🚀 Future Enhancements

Possible future improvements include:

* Native WebRTC audio/video calling
* AI-powered skill assessment
* Advanced collaborative whiteboard
* AI-generated personalized assignments
* Automatic assignment evaluation
* Learning analytics
* Tutor performance analytics
* Course completion certificates
* Gamification
* Learning streaks
* AI voice tutor
* Multilingual course assistance
* Advanced recommendation models
* Fraud/payment monitoring
* Semantic course search

---

# 🎯 Why Mentora?

Traditional learning platforms primarily focus on **content delivery**.

Mentora focuses on the complete learning journey:

```text
DISCOVER
   ↓
UNDERSTAND YOUR GOAL
   ↓
FIND THE RIGHT COURSE
   ↓
FIND THE RIGHT TUTOR
   ↓
LEARN
   ↓
ASK AI
   ↓
ASSESS
   ↓
IDENTIFY WEAKNESSES
   ↓
GET HUMAN HELP
   ↓
IMPROVE
```

The platform combines:

**AI + RAG + Human Tutoring + Course Marketplace + Personalized Learning**

rather than treating them as separate systems.

---

# 💼 Placement Value

Mentora provides opportunities to demonstrate knowledge of:

* Full-stack development
* REST API design
* Database design
* SQL and relational modeling
* Authentication
* Role-based authorization
* File storage
* Payment workflows
* Scheduling
* Concurrency handling
* Search
* Recommendation systems
* Vector databases
* Embeddings
* RAG
* LLM integration
* AI evaluation
* System design
* Cloud deployment

The project can therefore be discussed at multiple levels during technical interviews, from **DBMS and APIs** to **AI/RAG and system architecture**.

---

# 📌 Project Vision

> **Mentora aims to move online learning from course discovery to outcome-driven personalized education — connecting students with the right knowledge, the right AI assistance, and the right human mentor at the right time.**

---

## Status

🚧 **Currently under development**

Future releases will progressively introduce:

* Core authentication
* Course marketplace
* Tutor profiles
* Course creation
* Enrollment
* Payments
* Tutoring bookings
* Learning progress
* RAG-based Course AI
* Personalized recommendations
* AI learning assistant
