from django.db import migrations


def add_initial_data(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    Tag = apps.get_model('endpoints', 'Tag')
    Endpoint = apps.get_model('endpoints', 'Endpoint')

    # 1. СЪЗДАВАНЕ НА РАЗНООБРАЗНИ ТАГОВЕ
    tags_data = [
        ("Beta", "New features currently in the testing phase."),
        ("Deprecated", "Old endpoints that will be removed soon."),
        ("Production-Ready", "Stable and fully tested API routes."),
        ("Read-Only", "Endpoints that do not modify database state."),
        ("Security-Critical", "Handles sensitive data or authentication."),
        ("External-API", "Integration with third-party services."),
        ("High-Performance", "Optimized for high-speed data processing.")
    ]

    created_tags = {}
    for name, desc in tags_data:
        tag_obj, _ = Tag.objects.get_or_create(name=name, description=desc)
        created_tags[name] = tag_obj

    # 2. ПРОЕКТИ С ПЪЛЕН МИКС ОТ МЕТОДИ (ВКЛЮЧИТЕЛНО DELETE)
    projects_to_create = [
        {
            "name": "Nexus Auth",
            "language": "Python",
            "version": "1.2.4",
            "base_url": "https://docs.python.org/3/",
            "description": "Centralized identity provider focusing on security.",
            "endpoints": [
                {"path": "/api/v1/login", "method": "POST", "desc": "User auth",
                 "tags": ["Security-Critical", "Production-Ready"]},
                {"path": "/api/v1/profile", "method": "GET", "desc": "User details", "tags": ["Read-Only"]},
                {"path": "/api/v1/account/terminate", "method": "DELETE", "desc": "Delete user account",
                 "tags": ["Security-Critical"]}
            ]
        },
        {
            "name": "Quantum Store",
            "language": "JavaScript",
            "version": "2.1.0",
            "base_url": "https://developer.mozilla.org/en-US/",
            "description": "Scalable e-commerce engine for digital assets.",
            "endpoints": [
                {"path": "/orders/create", "method": "POST", "desc": "Place order", "tags": ["Production-Ready"]},
                {"path": "/cart/items/clear", "method": "DELETE", "desc": "Empty shopping cart",
                 "tags": ["Production-Ready"]},
                {"path": "/payments/verify", "method": "POST", "desc": "Verify payment",
                 "tags": ["Security-Critical", "External-API"]},
                {"path": "/inventory/item/{id}", "method": "DELETE", "desc": "Remove product from stock",
                 "tags": ["High-Performance"]}
            ]
        },
        {
            "name": "Gopher Stream",
            "language": "Go",
            "version": "0.9.5",
            "base_url": "https://go.dev/doc/",
            "description": "Low-latency real-time analytics stream.",
            "endpoints": [
                {"path": "/stream/raw", "method": "GET", "desc": "Raw data stream",
                 "tags": ["Beta", "High-Performance"]},
                {"path": "/cache/flush", "method": "DELETE", "desc": "Purge stream cache",
                 "tags": ["High-Performance"]},
                {"path": "/health", "method": "GET", "desc": "Service health", "tags": ["Production-Ready"]}
            ]
        },
        {
            "name": "Legacy Billing",
            "language": "Java",
            "version": "5.4.1",
            "base_url": "https://docs.oracle.com/en/java/",
            "description": "Maintenance mode financial system.",
            "endpoints": [
                {"path": "/export/csv", "method": "GET", "desc": "CSV Export", "tags": ["Deprecated"]},
                {"path": "/old-records/{id}", "method": "DELETE", "desc": "Wipe old audit log", "tags": ["Deprecated"]}
            ]
        },
        {
            "name": "Titan Scraper",
            "language": "Python",
            "version": "3.0.0",
            "base_url": "https://www.crummy.com/software/BeautifulSoup/bs4/doc/",
            "description": "Next-gen web crawler for big data.",
            "endpoints": [
                {"path": "/jobs/status", "method": "GET", "desc": "Track progress", "tags": ["Read-Only"]},
                {"path": "/jobs/{id}/cancel", "method": "DELETE", "desc": "Stop scraping job",
                 "tags": ["High-Performance"]},
                {"path": "/proxy/list", "method": "GET", "desc": "Active proxies", "tags": ["External-API"]}
            ]
        },
        {
            "name": "Rocket UI Kit",
            "language": "TypeScript",
            "version": "1.0.1",
            "base_url": "https://www.typescriptlang.org/docs/",
            "description": "Component library and asset documentation.",
            "endpoints": [
                {"path": "/assets/icons", "method": "GET", "desc": "SVG icons",
                 "tags": ["Read-Only", "Production-Ready"]},
                {"path": "/themes/custom/{id}", "method": "DELETE", "desc": "Delete custom theme", "tags": ["Beta"]},
                {"path": "/fonts/download", "method": "GET", "desc": "Brand fonts", "tags": ["Read-Only"]}
            ]
        }
    ]

    for p_info in projects_to_create:
        project, _ = Project.objects.get_or_create(
            name=p_info["name"],
            language=p_info["language"],
            version=p_info["version"],
            base_url=p_info["base_url"],
            description=p_info["description"]
        )

        for e_info in p_info["endpoints"]:
            endpoint, _ = Endpoint.objects.get_or_create(
                project=project,
                path=e_info["path"],
                method=e_info["method"],
                description=e_info["desc"]
            )
            for tag_name in e_info["tags"]:
                tag = created_tags.get(tag_name)
                if tag:
                    endpoint.tags.add(tag)


def remove_initial_data(apps, schema_editor):
    # Това ще изтрие всичко при rollback
    apps.get_model('projects', 'Project').objects.all().delete()
    apps.get_model('endpoints', 'Tag').objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0005_alter_project_base_url_alter_project_version'),
        ('endpoints', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_initial_data, remove_initial_data),
    ]