# APILab Manager - Common Models Documentation

## Overview
The **Common** application serves as the foundation for the APILab Manager ecosystem. It contains shared logic and base classes that are inherited by other applications (`projects` and `endpoints`). By centralizing common fields like timestamps, the system ensures a **"DRY" (Don't Repeat Yourself)** architecture and consistent data tracking across all entities.

The main component is:
* **TimeStampedModel**: An abstract base model for automatic auditing.

---

## TimeStampedModel
The `TimeStampedModel` is an **abstract model** that provides self-updating date and time fields. It does not create a table in the database itself but injects its fields into any model that inherits from it.



### Model Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `created_at` | **DateTimeField** | Automatically stores the date and time when the object is first created (`auto_now_add=True`). |
| `updated_at` | **DateTimeField** | Automatically updates to the current date and time every time the object is saved (`auto_now=True`). |

### Meta Options
* **Abstract: True**: This ensures Django doesn't create a separate database table for this model.
* **Ordering: `['-created_at']`**: By default, all inheriting models will be ordered with the newest entries first.

---


## Usage Example
Instead of defining `created_at` and `updated_at` in every single model, we simply inherit from `TimeStampedModel`.

---

#### **Next model** :  [Endpoints](#)
---
[Home](#)

