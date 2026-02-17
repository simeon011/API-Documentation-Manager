# 🗂 APILab Manager - Models Documentation Index

## Overview
The database architecture of **APILab Manager** is designed to be modular and scalable. It is built upon a foundation of abstract inheritance and relational integrity, ensuring that API documentation is structured, searchable, and consistent.

Click on any model name below to navigate to its detailed documentation section.

---

## System Architecture & Models

### 1. [Common Models](#)
*The infrastructure layer of the project.*
* **TimeStampedModel**: An abstract base class that provides automated `created_at` and `updated_at` fields to all other models. It ensures a consistent audit trail without code duplication.

### 2. [Endpoints Application](#)
*The functional layer describing the API resources.*
* **Endpoint**: Documents specific API routes. It uses a **Many-to-One** relationship with `Project` and features custom path validation to ensure industry-standard formatting.
* **Tag**: A metadata entity used for categorization. It uses a **Many-to-Many** relationship with `Endpoint` to allow flexible, non-linear organization of resources.

### 3. [Projects Application](#)
*The top-level container for all documentation.*
* **Project**: Represents a standalone software service. Stores critical metadata such as programming language, versioning (via Regex validation), and secure base URLs.
---

## 📊 Relationship Schema

The following diagram illustrates how these models interact within the Django ORM:



| Model | Inherits From | Relations | Key Responsibility |
| :--- | :--- | :--- | :--- |
| **Project** | `TimeStampedModel` | One-to-Many (`Endpoints`) | Root container for services. |
| **Endpoint** | `TimeStampedModel` | Many-to-One (`Project`), M2M (`Tags`) | Specific API route documentation. |
| **Tag** | `TimeStampedModel` | Many-to-Many (`Endpoints`) | Categorization and filtering. |

---

## 🛠 Technical Highlights

* **DRY Principle**: Implemented via `TimeStampedModel` inheritance.
* **Data Integrity**: Enforced by `RegexValidators` and `ChoiceFields`.
* **Performance**: Optimized using `prefetch_related` across relations.

---

[Home](https://github.com/simeon011/API-Documentation-Manager/blob/main/README.md)
