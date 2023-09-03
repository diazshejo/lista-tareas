# lista-tareas
Lista de tareas usando Arquitectura MVC y Repositorio

## Requisitos

- Python 3.11.5
- Django 4.2.4
- mysql 8.0

nombre_del_proyecto/
│
├── aplicacion1/               # Directorio de la primera aplicación Django
│   ├── migrations/           # Archivos de migración de la base de datos
│   ├── templates/            # Plantillas HTML para las vistas
│   ├── static/               # Archivos estáticos (CSS, JavaScript, imágenes)
│   ├── admin.py              # Configuración del panel de administración
│   ├── models.py             # Modelos de datos de la aplicación
│   ├── views.py              # Lógica de las vistas
│   └── ...
│
├── aplicacion2/               # Directorio de la segunda aplicación Django
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── nombre_del_proyecto/       # Directorio de configuración principal
│   ├── settings.py           # Configuración principal del proyecto
│   ├── urls.py               # Configuración de las URL del proyecto
│   ├── wsgi.py               # Punto de entrada para servidores web
│   ├── asgi.py               # Punto de entrada para servidores ASGI
│   └── ...
│
├── manage.py                  # Script de gestión de Django
├── requirements.txt           # Lista de dependencias del proyecto
├── README.md                  # Documentación del proyecto
├── .gitignore                 # Archivo para especificar archivos/directorios ignorados por Git
├── LICENSE.md                 # Licencia del proyecto (si es necesario)
├── datos_iniciales.json       # Datos iniciales para cargar en la base de datos
└── ...

