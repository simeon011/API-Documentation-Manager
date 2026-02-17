# Project Documentation: API Lab Manager🚀
**API Lab Manager** is a comprehensive web-based system designed for managing and documenting software interface (API) projects. It provides a unified platform for developers to organize their projects, detail specific API endpoints, and categorize them using a flexible tagging system.

---

## 🖥️ Setup & Installation
 - [Project Setup](https://github.com/simeon011/API-Documentation-Manager/blob/main/docs/project_setup.md)

---

## 🏗 Key Parts (Technical Core)
 - [Models](https://github.com/simeon011/API-Documentation-Manager/blob/main/docs/models.md)
 - [Views & Business Logic](https://github.com/simeon011/API-Documentation-Manager/blob/main/docs/views_and_buisness_logic.md)

---

## 🛠️ Key Technical Components

### 1. Database & ORM Optimization
* **Efficient Querying**: Implemented `prefetch_related` to handle Many-to-Many and reverse ForeignKey relationships, preventing the N+1 query problem.
* **Advanced Search**: Integrated a global search engine using **Django Q objects**, enabling multi-column filtering with partial matches.

### 2. Custom Validation Engine
* **Technical Standards**: Deployed `RegexValidator` for semantic versioning (`1.0.0`) and URL security enforcement (`https://`).
* **Logic Synchronization**: Applied identical validation logic at both the Model and Form levels to ensure double-layer data protection.

### 3. Structural Design (OOP)
* **Model Abstraction**: Used abstract base classes (`TimeStampedModel`) to implement universal audit fields (created/updated at) across the entire database schema.
* **Separation of Concerns**: Divided the project into modular applications to separate infrastructure logic from business-specific features.

### 4. Admin & UX Enhancements
* **Secure Administration**: Customized the Django Admin with `readonly_fields` to protect historical audit data.
* **Error Handling**: Implemented a custom `handler404` to provide a consistent brand experience even on broken links.
