# AI-Powered Personalized Product Ad Composer
*(Copy the below content to your Word Document and fill in the missing details like Enrolment No)*

---

### [COVER PAGE]
**Project Title**: AI-Powered Personalized Product Ad Composer
**By**: <Your Name>
**Enrolment No**: <Your Enrolment No>
**Under the Supervision of**: Ms. Swati Solanki
**A Report Submitted to**: Gujarat University
**In Partial Fulfilment of the Requirements for the Degree of**: M.Sc. IT Data Management & Visual insight (5 years integrated)
**Date**: April 2026
**Centre for Professional Courses, Gujarat University, Ahmedabad**

---

### CERTIFICATE
This is to certify that research work embodied in this report entitled “AI-Powered Personalized Product Ad Composer” was carried out by <Your Name> (Enrolment No: <>) at the Centre for Professional Course for partial fulfilment of M.Sc. IT degree to be awarded by Gujarat University. This research work has been carried out under my supervision and is to the satisfaction of the department.
**Date**: _____
**Place**: _____
**Ms. Swati Solanki (Guide)**
**Ms. Namita Doshi (Program In-Charge)**
**Dr. Paavan Pandit (Director)**

---

### DECLARATION OF ORIGINALITY
I hereby certify that I am the sole author of this Project report and that neither any part of this Project report nor the whole of the Project report has been submitted for a degree to any other University or Institution.
I certify that, to the best of my knowledge, my Project report does not infringe upon any one’s copyright nor violate any proprietary rights and that any ideas, techniques, quotations, or any other material from the work of other people included in my Project report, published or otherwise, are fully acknowledged in accordance with the standard referencing practices. 
I declare that this is a true copy of my Project report, including any final revisions, as approved by my Project report review committee.
**Date**: _____
**Place**: _____
**Sign of Student**: _____

---

### ACKNOWLEDGMENT
We are sincerely thankful to our guide, Prof. Swati Solanki, for her constant support, stimulating suggestions, and encouragement, which greatly assisted us in successfully completing our project work. Her close supervision over the past few months and helpful insights have been invaluable. 
I, hereby, take an opportunity to convey my gratitude for the generous assistance and cooperation that I received from Prof. Namita Doshi and to all those who helped me directly and indirectly.
We are deeply indebted & thankful to our Department Faculties who helped and rendered their valuable time, knowledge, and information. We also thank Dr. Paavan Pandit, Director, CPC-GU, for extending all the help and cooperation during our training period.

---

### ABSTRACT
The "AI-Powered Personalized Product Ad Composer" is an intelligent software system developed to automate and optimize the creation of product advertisements. Traditionally, developing marketing campaigns requires extensive manual effort from copywriters and graphic designers. This project addresses this bottleneck by leveraging Machine Learning (ML) and Generative AI. The system utilizes Natural Language Processing (NLP)—specifically a Random Forest classifier employing TF-IDF vectorization—to analyze product descriptions and predict the optimal consumer demographic (Teenagers, Professionals, Seniors). Furthermore, it utilizes generative algorithms to dynamically formulate compelling ad copy (Headlines, Descriptions, and Slogans) and natively integrates with the Hugging Face Inference API (FLUX.1-schnell model) to synthesize high-fidelity, high-conversion advertisement graphics. Deployment is realized through an interactive Streamlit web application, demonstrating a novel, data-driven approach to instant digital marketing.
**Keywords**: Machine Learning, NLP, Generative AI, Streamlit, Digital Marketing, FLUX.1, Hugging Face.

---

# CHAPTER 1: INTRODUCTION

### 1.1 Introduction
The rapid growth of the e-commerce sector necessitates fast, cost-effective, and personalized digital marketing. Creating customized advertisements for thousands of products is a logistically complex task. This project focuses on building an automated "Ad Composer" that seamlessly links product datasets to instant advertising outputs, generating both text (Ad Copy) and visuals (Images). 

### 1.2 Motivation
Small and medium-scale businesses often lack the resources to hire professional marketing agencies. The motivation behind this project is to democratize high-quality advertising by providing a tool that uses data science and AI to automatically identify the target audience and generate premium ad materials with a single click.

### 1.3 Objectives
- To clean and preprocess real-world e-commerce data (Flipkart dataset).
- To train a Machine Learning model capable of predicting the ideal target audience for a product based on its textual description.
- To formulate engaging and demographically accurate advertisement text parameters.
- To integrate state-of-the-art Text-to-Image models (Hugging Face FLUX.1) to generate realistic advertisement banners.
- To deploy the comprehensive model architecture via an interactive web interface using Streamlit.

### 1.4 Organization of Report
Chapter 2 discusses the Background Theory. Chapter 3 contains the Literature Survey. Chapter 4 introduces the Proposed Work. Chapter 5 covers the Implementation Environment. Chapter 6 explores the Dataset and Data Visualization. Chapter 7 covers Model Training, Evaluation, and Deployment. Chapter 8 provides the Conclusion and References.

---

# CHAPTER 2: BACKGROUND THEORY

### 2.1 Machine Learning and NLP
Natural Language Processing (NLP) enables computers to understand unstructured text. Techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) are used to extract meaningful features from product descriptions to feed into supervised classification models like Random Forest, ensuring accurate text categorization.

### 2.2 Generative AI and Diffusion Models
Generative AI refers to deep-learning models capable of creating new content. Specifically, Text-to-Image diffusion models like FLUX.1 evaluate textual prompts to synthesize incredibly realistic graphic designs. Integrating API-based inference drastically reduces the local computational overhead while maintaining high output fidelity.

---

# CHAPTER 3: LITERATURE SURVEY

### 3.1 Literature Survey
Recent studies in e-commerce automation heavily emphasize the role of AI in reducing Customer Acquisition Cost (CAC). Previous methodologies relied on basic rule-based template generation for marketing textual copy, which resulted in robotic and repetitive ads. Comparatively, newer state-of-the-art models emphasize matching demographics dynamically to localized aesthetics.

### 3.2 Comparative Study
Unlike standard static marketing tools out in the market (which require manual configuration of audience styles), this project introduces an NLP auto-classifier that inherently detects the necessary audience traits and dynamically constructs API-payloads capable of rendering typography directly on AI-generated images.

---

# CHAPTER 4: PROPOSED WORK

### 4.1 Problem Statement and Research Gap
Most existing systems either generate images or text independently. There is a research gap in unified platforms that auto-evaluate an e-commerce product from a raw CSV file, classify its audience smartly, and generate a composed visual and textual ad jointly in a lightweight UI.

### 4.2 Proposed Approach
The architecture incorporates a Jupyter Notebook pipeline for back-end Data Cleaning, EDA, and Model Export (.joblib format). The ML model is a Scikit-Learn Pipeline combining a TF-IDF Vectorizer and a Random Forest Classifier. The front-end consists of a Streamlit Framework that loads the CSV dataset, runs the Pickle/Joblib model to recognize audiences, and interfaces with Hugging Face via REST API for visual synthesis.

### 4.3 Expected Outcome
A robust web application where users simply type or choose a product name, and the system automatically provides an analytical breakdown, engaging copywriting, and an aesthetically superior image advertisement customized to the predicted demographic.

### 4.4 Workplan
1. Dataset Sourcing and Cleaning (Pandas/NumPy).
2. Exploratory Data Analysis (Matplotlib/Seaborn).
3. NLP Feature Engineering and ML Training.
4. Model Export (Joblib).
5. Development of the Web UI (Streamlit).
6. Integration of the FLUX.1 Hugging Face API.
7. Testing and Deployment.

---

# CHAPTER 5: IMPLEMENTATION ENVIRONMENT

### 5.1 System Specification
- **Hardware**: Standard minimum 8GB RAM, i5 or equivalent processor.
- **Operating System**: Windows OS.

### 5.2 Programming Environment
- **Language**: Python 3.10+
- **Database**: CSV Data format.
- **Libraries**: Pandas, NumPy, Scikit-Learn, Streamlit, Requests, Python-dotenv, Joblib.
- **API Models**: Black-Forest-Labs/FLUX.1-Schnell (via Hugging Face).

### 5.3 Tools Used
- Jupyter Notebook (Development, EDA, and Model Formulation)
- Visual Studio Code (Application Architecture and Frontend execution)

---

# CHAPTER 6: DATASET AND VISUALIZATION

### 6.1 Dataset Gathering
The project utilizes the "Flipkart E-commerce Sample" dataset, initially comprising around 20,000 product listings carrying attributes such as Product Name, Main Category, Brand, and Description.

### 6.2 Data Preprocessing
Data was ingested and cleansed in an automated pipeline. Missing NaN values in crucial columns were handled (e.g., dropping empty descriptions while safely filling missing 'Brand' attributes to preserve data). Furthermore, duplicate entries, special characters, and HTML noise were stripped from product descriptions to optimize the NLP model ingestion.

### 6.3 Data Visualization
Various distribution plots via Matplotlib were employed to study product categorization frequencies and target demographic distributions prior to modeling, revealing heavy densities in standard e-commerce groups (Clothing, Footwear).

---

# CHAPTER 7: IMPLEMENTATION AND EVALUATION

### 7.1 Training the model
A synthetic labeling algorithm mapped demographic keywords ("trendy", "comfort", "premium") into target classes (Teenagers, Seniors, Professionals). An 80-20 Train-Test split was executed, and features were extracted using a 1000-feature limit TF-IDF Vectorizer connected concurrently to a Random Forest Classifier consisting of 100 estimators.

### 7.2 Testing the model
The Scikit-Learn pipeline was tested on unseen test splits to evaluate accuracy in assigning correct demographic brackets given complex, overlapping text strings.

### 7.3 Evaluation of model
The primary evaluation metrics extracted from the `classification_report` showed significant precision and recall for text separation, minimizing biased assumptions. 

### 7.4 Deployment of the model (Result App)
The evaluated model was serialized via Joblib into `audience_predictor.joblib`. The deployment utilized the Streamlit library. Within the Application (`app.py`), the model loads securely into `@st.cache_resource` memory. Upon user selection of a product, the Python app cross-references the ML predictor, dynamically adjusts the UI to state the detected audience, generates the contextual slogan template, and fires a payload to the FLUX.1 endpoint generating a final image.

---

# CHAPTER 8: CONCLUSION

### 8.1 Conclusion
The AI-Powered Personalized Product Ad Composer successfully demonstrates the integration of Machine Learning text classification with Generative visual pipelines. By resolving the disparity between data analytics and marketing generation, this project proves that complex creative marketing endeavors can be highly automated and personalized simultaneously. The use of a serialized NLP predictor ensures the platform maintains zero-latency response times for the demographic assessment, proving its readiness for production-level digital infrastructure.

---

# REFERENCES
1. Python Software Foundation. (2026). "Python Language Reference." Available at https://www.python.org/
2. Pedregosa, F. et al. (2011). "Scikit-learn: Machine Learning in Python", JMLR 12, pp. 2825-2830.
3. McKinney, W. (2010). "Data Structures for Statistical Computing in Python".
4. Hugging Face API Documentation. (2026). "Serverless Inference API reference".
5. Streamlit Documentation. (2026). "The fastest way to build data apps".
