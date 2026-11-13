<p align="center">
  <picture>
    <source srcset="assets/banner-tuyo.webp" type="image/webp" />
    <img src="assets/banner-tuyo.png" alt="Sebastián Clavijo — Software Developer, AI & Automation" width="100%" />
  </picture>
</p>

<p align="center">
  <a href="mailto:contacto@gamorasystems.com"><img src="https://img.shields.io/badge/contacto%40gamorasystems.com-E5502E?style=flat-square&logo=maildotru&logoColor=white" alt="Email" /></a>
  <a href="https://gamorasystems.com"><img src="https://img.shields.io/badge/gamorasystems.com-1E90FF?style=flat-square&logo=firefoxbrowser&logoColor=white" alt="Sitio" /></a>
  <img src="https://img.shields.io/badge/Medell%C3%ADn-Colombia-0B0E14?style=flat-square&logo=googlemaps&logoColor=white" alt="Ubicación" />
</p>

---

Diseño y construyo **sistemas de gestión a la medida** para pequeñas y medianas empresas: SaaS, POS y ERP que reemplazan el Excel y el cuaderno. Trabajo con **Django y PostgreSQL**, despliego en servidores Linux propios y uso IA donde de verdad ahorra trabajo — no donde solo se ve bonito.

Fundé **Gamora Systems**, con base en Medellín.

## Stack con el que trabajo

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter" />
  <img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" alt="Dart" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
</p>

## Proyectos

### AesthetiCare — SaaS multi-tenant para estudios de estética

Gestión completa de un estudio: citas, clientas, servicios, historial clínico y consentimientos informados.

Lo interesante no es la interfaz, es el aislamiento: **cada estudio vive en su propio esquema de PostgreSQL** (`django-tenants`), resuelto desde la sesión y no desde el subdominio. Un estudio no puede ver los datos de otro ni por error. Cada uno además personaliza sus colores, y esos ajustes persisten entre sesiones porque el middleware de tenant corre antes de la autenticación.

<p align="center">
  <img src="assets/aestheticare-dashboard.png" alt="Panel de AesthetiCare" width="88%" />
</p>

`Django` · `PostgreSQL` · `django-tenants` · `CSS vanilla` — **privado**, demo en vivo disponible a pedido.

---

### Balance — finanzas de negocio registradas desde Telegram

SaaS de control financiero. La particularidad es cómo se ingresa un gasto: le escribes al bot, le mandas una nota de voz o le tomas una foto al recibo.

El bot transcribe el audio con **Whisper en local** y parsea el texto con **Claude Haiku**; de la foto saca monto, fecha y comercio por OCR. Cada usuario tiene uno o varios negocios con finanzas completamente separadas.

`Django 5` · `PostgreSQL` · `python-telegram-bot` · `faster-whisper` · `Claude Haiku` — **privado**, demo a pedido.

---

### Orión — plataforma de gestión para un centro de formación

Sistema que cubre los **33 requisitos funcionales** de la especificación de un centro de formación del SENA, con chatbot integrado en la interfaz.

`Django 5` · `PostgreSQL` · `Tailwind CSS` · `Playwright` — **privado**.

---

### ReqAI — de la reunión con el cliente a los requisitos

App móvil en Flutter: grabas la reunión, la app transcribe el audio con Whisper vía Groq, y extrae **requisitos funcionales estructurados** que se convierten en tareas. Nació de un problema real: las reuniones de levantamiento se pierden en notas sueltas.

`Flutter` · `Dart` · `Supabase` · `Groq` · `OpenRouter`

<p>
  <a href="https://github.com/JuanSebastianClavijoTapias/requia"><img src="https://img.shields.io/badge/Ver%20c%C3%B3digo-181717?style=flat-square&logo=github&logoColor=white" alt="Repositorio ReqAI" /></a>
</p>

---

### KanView — API y panel para un taller de tapicería en cuero

API con Django REST Framework —vistas basadas en funciones, sin capas de abstracción innecesarias— más las páginas de interfaz servidas con templates.

`Django REST Framework` · `PostgreSQL`

<p>
  <a href="https://github.com/JuanSebastianClavijoTapias/djangoRestKanview"><img src="https://img.shields.io/badge/Ver%20c%C3%B3digo-181717?style=flat-square&logo=github&logoColor=white" alt="Repositorio KanView" /></a>
</p>

## Cómo trabajo

- **Django + PostgreSQL por defecto.** SQLite solo para prototipos. No elijo la tecnología por moda: elijo la que voy a poder mantener en dos años.
- **Despliegue real en Linux.** Systemd con Gunicorn y Nginx sirviendo estáticos, con HTTPS. No entrego un proyecto que solo corre en `runserver`.
- **Los archivos no viven en el servidor.** Fotos y documentos van a almacenamiento S3-compatible (Backblaze B2) detrás de Cloudflare. En producción, `MEDIA_ROOT` local es una bomba de tiempo.
- **Seguridad desde el día uno.** `django-axes` contra fuerza bruta, CSP y cabeceras endurecidas, validación en el backend. El frontend nunca es la única capa.
- **Cada proyecto se documenta.** Arquitectura, decisiones y por qué se tomó cada una, en Markdown dentro del repo. Es lo primero que leo cuando vuelvo a un proyecto de hace seis meses.

## Contacto

¿Tienes un proceso que todavía se lleva en Excel, en papel o por WhatsApp? Escríbeme y lo miramos.

**contacto@gamorasystems.com** · [gamorasystems.com](https://gamorasystems.com) · Medellín, Colombia
