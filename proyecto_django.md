## Estructura del Proyecto Django
La estructura básica de mi proyecto tras ejecutar `startproject` y `startapp` es la siguiente:

```text
actividad_m6_l2/
├── env/                # Entorno virtual (librerías aisladas)
├── mi_sitio/           # Carpeta del proyecto (configuración global)
│   ├── manage.py       # Utilidad de administración de Django
│   ├── mi_sitio/       # Configuración del proyecto (settings.py, urls.py)
│   └── principal/      # Aplicación creada con startapp
│       ├── views.py    # Lógica de las vistas
│       ├── urls.py     # Rutas de la aplicación
│       └── ...         # Otros archivos (models, admin, apps)
└── proyecto_django.md  # Este informe