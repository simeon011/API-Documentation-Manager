# APILab Manager - Endpoints & Tags Documentation

## Overview
The **Endpoints** application is the functional heart of the project. It provides the necessary tools to document specific API routes, associate them with projects, and classify them using a flexible tagging system. This structure allows for a granular view of a project's architecture.

The main components are:
* **Endpoint Model**: Detailed route documentation.
* **Tag Model**: Metadata and categorization labels.
* **Custom Validators**: Path format enforcement.

---

## Tag Model
The `Tag` model allows for non-linear organization. Unlike projects, which are containers, tags act as labels that can span across multiple endpoints and projects.

| Field | Type | Description |
| :--- | :--- | :--- |
| **name** | `CharField` | Unique identifier for the tag (e.g., "Public", "Auth", "v2"). |
| **description** | `TextField` | Optional context regarding the tag's purpose. |

### Meta Options
* **Inheritance**: Inherits from `TimeStampedModel` (`created_at`, `updated_at`).
* **String Representation**: Returns the `name` of the tag.

---

## Endpoint Model
The `Endpoint` model is where the specific API technicalities are stored. It links directly to a parent `Project` and maintains a many-to-many relationship with `Tags`.



| Field | Type | Description |
| :--- | :--- | :--- |
| **project** | `ForeignKey` | Links to `Project` (Related name: `endpoints`). Deletes on cascade. |
| **path** | `CharField` | The API route URL. Validated to ensure it starts with `/`. |
| **method** | `CharField` | HTTP Method choice (GET, POST, PUT, DELETE). |
| **description** | `TextField` | Detailed explanation of what the endpoint does. |
| **tags** | `ManyToManyField` | Links to multiple `Tag` instances for categorization. |

---

## Technical Highlights

### 1. Custom Path Validation
To maintain industry standards, a custom validator `validate_start_slash` is applied to the `path` field. This prevents routes from being saved without a leading forward slash, ensuring consistency in the documentation.

### 2. Choice Enumeration
The `method` field utilizes `models.TextChoices`, restricting entries to valid HTTP verbs. This prevents "dirty data" and simplifies filtering in the UI.

---

#### **Next model**: [Projects](https://github.com/simeon011/API-Documentation-Manager/blob/main/docs/models/projects.md)
---
[Home](https://github.com/simeon011/API-Documentation-Manager/blob/main/README.md)
