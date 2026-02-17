# APILab Manager - Projects Documentation

## Overview
The **Projects** application is the core container of the APILab Manager. It manages the high-level metadata of software services, including their versioning, technology stack, and base access points. Every API endpoint documented in the system must belong to a specific project.

The main components are:
* **Project Model**: The primary data entity.
* **Custom Validators**: Advanced checks for versioning and URL security.
* **Search Logic**: Multi-field filtering for project discovery.

---

## Project Model
The `Project` model inherits from `TimeStampedModel` and serves as the parent entity for all API documentation. It uses `TextChoices` for language selection to ensure data consistency.



| Field | Type | Description |
| :--- | :--- | :--- |
| **name** | `CharField` | Project name (Min: 3, Max: 100 characters). |
| **language** | `CharField` | Programming language (Choices: Python, JS, Go, Java, C#, PHP). |
| **version** | `CharField` | Software version (Regex Validated: `X.X.X` or `X.X.X.X`). |
| **base_url** | `URLField` | Root API address (Validated: must start with `https://www.`). |
| **description** | `TextField` | Comprehensive overview of the project. |

### Meta Options
* **Inheritance**: Inherits from `TimeStampedModel` (`created_at`, `updated_at`).
* **String Representation**: Returns the `name` of the project.

---

## Technical Highlights

### 1. Advanced Regex Validation
Data integrity is enforced at the model level using `RegexValidator` within `projects/validators.py`:
* **`validate_version_format`**: Restricts version input to standard semantic versioning formats.
* **`validate_base_url_format`**: Ensures all documented projects use secure HTTPS and follow the `www.` naming convention.

### 2. Programming Language Choices
By using `models.TextChoices`, the system limits the `language` field to a predefined list. This prevents fragmentation in the database (e.g., prevents having both "Py" and "Python" as entries).

---

[Home](https://github.com/simeon011/API-Documentation-Manager/blob/main/README.md)
