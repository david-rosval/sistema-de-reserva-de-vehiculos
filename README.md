# Sistema de Reserva de Vehículos

Este proyecto implementa un sistema de reservas de bicicletas y scooters utilizando **FastAPI** y patrones de diseño como Factory Method, Builder, Proxy y Strategy.

## **Requisitos Previos**

Asegúrate de tener instalado lo siguiente en tu sistema:

- **Python 3.8+**
- **pip** (Administrador de paquetes de Python)

## **Pasos para Configurar el Proyecto**

### **1. Clonar el Repositorio**

Clona este repositorio en tu máquina local:
```bash
# Reemplaza URL_DEL_REPOSITORIO con la URL de tu repositorio
git clone URL_DEL_REPOSITORIO
cd vehicle_reservation
```

### **2. Crear un Entorno Virtual**

Crea y activa un entorno virtual para gestionar las dependencias del proyecto:

- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### **3. Instalar Dependencias**

Instala las dependencias necesarias desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### **4. Ejecutar la API**

Inicia el servidor FastAPI utilizando **Uvicorn**:
```bash
uvicorn app.main:app --reload
```

Si todo está configurado correctamente, deberías ver un mensaje como este:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### **5. Probar la API**

#### **Interfaz Interactiva de Swagger**

1. Abre tu navegador y navega a:
   - `http://127.0.0.1:8000/docs`

2. Aquí encontrarás la documentación generada automáticamente para interactuar con los endpoints.

#### **Endpoints Principales**

- **`POST /reservar`**: Reserva un vehículo.
  - Parámetros:
    - `vehicle_type`: Tipo de vehículo (`"bicycle"` o `"scooter"`).
    - `duration`: Duración de la reserva en horas.

- **`POST /personalizar-reserva`**: Personaliza un vehículo (si está habilitado en el código).

### **6. Cerrar el Entorno Virtual**

Cuando termines de usar el proyecto, puedes desactivar el entorno virtual:
```bash
deactivate
```

---

## **Ampliaciones Sugeridas**

- Integrar una base de datos para persistir las reservas.
- Añadir más tipos de vehículos (por ejemplo, motocicletas).
- Crear nuevas estrategias de precios (por ejemplo, precios para clientes frecuentes).

---

¡Listo! El proyecto debería estar funcionando en tu máquina local.