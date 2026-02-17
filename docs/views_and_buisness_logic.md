# [1. Views in common](https://github.com/simeon011/API-Documentation-Manager/blob/main/common/views.py)

### 1. Unified Dashboard

The `dashboard` function is designed to provide a snapshot of the API Registry's state by aggregating data from various applications (`projects` and `endpoints`).

- 📊 **Real-time statistics:** The system calculates the total number of projects and endpoints, giving the user a quick overview of the documentation's scale.
- 🚀 **Optimized retrieval:** `annotate(endpoints_count=Count('endpoints'))` is used to fetch the count of associated paths directly within a single SQL query.
- ⏱️ **Recent activity:** The last 5 updated projects are displayed, sorted by edit time (`-updated_at`), for easy access to current work.

### 2. System Resilience

- 🛡️ **Custom 404 Handling:** A dedicated `custom_404_view` is implemented, redirecting users to a branded page when a non-existent URL is requested.
- 🏷️ **Dynamic Context:** Each view passes a `page_title` variable to the templates, ensuring a consistent tab title and navigation labeling.

---
# [2. Views in endpoints](https://github.com/simeon011/API-Documentation-Manager/blob/main/endpoints/views.py)

The logic in `endpoints/views.py` is designed to work in close relation with the `Project` model, ensuring that every endpoint operation is contextually bound to its parent project.

### 1. Endpoint Management (CRUD)

- **Creation (`add_endpoint`):** Allows adding a new endpoint to a specific project. `commit=False` is used to automatically assign the `project_id` from the URL before saving.
- **Read (`details_endpoint`):** Retrieves detailed information about the path, method, and description, while providing easy access back to the parent project's data.
- **Update (`edit_endpoint`):** Uses `EditEndpointForm` with an object instance, allowing parameter modifications without losing the relationship to the project.
- **Delete (`delete_endpoint`):** Securely deletes the resource, after which the user is automatically redirected to the corresponding project's management dashboard.

### 2. Tagging System & Search

- **Global Tag List (`tags_list`):** Includes a built-in search engine using `icontains` filtering by name, for fast navigation between categories.
- **Tag Details (`tag_details`):** Implements a reverse lookup, displaying all endpoints to which the given tag is attached via `tag.endpoint_set.all()`.
- **Tag CRUD:** Standalone logic for adding and editing tags, ensuring metadata consistency throughout the entire system.

---

# [3. Views in projects](https://github.com/simeon011/API-Documentation-Manager/blob/main/projects/views.py)

The logic in `projects/views.py` is optimized for high performance and security, leveraging modern Django ORM tools.

### 1. Advanced Search & Filtering

The main view `project_list_view` implements complex filtering logic:

- **Real-time search:** `Q` objects are used to perform searches across multiple fields simultaneously: project name, description, and programming language.
- **Optimization:** To avoid the N+1 queries problem, `.prefetch_related('endpoints')` is used, allowing all related endpoints to be loaded with a single optimized database query.

### 2. Project Lifecycle (CRUD)

- **Create (`project_add`):** Handles the creation of new projects via `ProjectCreateForm`, automatically redirecting the user to the details page upon successful submission.
- **Read (`project_details`):** Uses `get_object_or_404` for safe data retrieval, ensuring that invalid requests will result in a controlled 404 error.
- **Update (`project_edit`):** Implements editing of existing records by loading the project instance into the form for easy modification.
- **Delete (`project_delete`):** A secure process for removing projects, requiring confirmation via a form before finalizing the operation.

---

[Home](https://github.com/simeon011/API-Documentation-Manager/blob/main/README.md)
