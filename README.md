# GorillaAlert

GorillaAlert es un gestor de tareas único y potente, diseñado no solo para organizar tus tareas, sino para garantizar que nunca olvides los eventos importantes. Su característica principal es la capacidad de interrumpir cualquier actividad con un recordatorio de pantalla completa, obligándote a prestar atención a la tarea pendiente. Ideal para personas que suelen estar profundamente concentradas en su trabajo, este programa asegura que no te pierdas recordatorios cruciales como eventos importantes, cumpleaños o tareas críticas.

---

## Características principales

- **Gestión de tareas**: Añade, elimina y visualiza tareas con facilidad.
- **Recordatorios inteligentes**: Recibe notificaciones emergentes (pop-ups) que cubren toda la pantalla.
- **Modo de ejecución en segundo plano**: Permite que el programa funcione sin necesidad de tener la interfaz abierta, lo que es especialmente útil para personas olvidadizas o con tareas críticas que no pueden permitirse pasar por alto.
- **Diseño en desarrollo**: Este proyecto está en su primer estado funcional y carece de diseño avanzado, pero se planea mejorar tanto el aspecto visual como implementar nuevas funcionalidades en futuras versiones.
- **Diseño personalizable**: Icono personalizado y configuración adaptable.
- **Inicio automático**: Configurable para ejecutarse automáticamente al encender el equipo.

---

## Requisitos del sistema

- **Sistema operativo**: Windows (64 bits)
- **Python**: Versión 3.12 o superior
- **Librerías necesarias**:
  - tkinter (incluido con Python)
  - Pillow
  - pystray
  - pyinstaller

---

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <URL del repositorio>
   cd TaskManager
   ```

2. **Instala las dependencias necesarias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Compila el programa en un archivo .exe** (opcional):
   ```bash
   pyinstaller --noconsole --onefile --icon=icono_gorila.ico main.py
   ```

   El ejecutable estará disponible en la carpeta `dist/`.

4. **Mueve el programa compilado**:
   - Crea una carpeta en `C:\Archivos de programa\` llamada `GorillaAlert`.
   - Copia el archivo `GorillaAlert.exe` y el archivo `tasks.json` (vacío inicialmente) a esa carpeta.

---

## Uso

### Ejecución inicial

- Si no has compilado el programa, ejecuta el script directamente:
  ```bash
  python main.py
  ```

- Si has compilado el programa, simplemente ejecuta el archivo `GorillaAlert.exe`.

### Configurar inicio automático

1. Presiona `Win + R`, escribe `shell:startup` y presiona Enter.
2. Crea un acceso directo de `GorillaAlert.exe` dentro de la carpeta de inicio.
3. Reinicia tu computadora para verificar que el programa se ejecuta automáticamente.

### Funcionalidad de la aplicación

1. **Añadir tarea**:
   - Rellena los campos:
     - Nombre
     - Descripción
     - Fecha (YYYY-MM-DD)
     - Hora (HH:MM)
     - Nivel de importancia (Muy importante, Importante, Regular, Simple).
   - Haz clic en `Agregar Tarea`.

2. **Eliminar tarea**:
   - Selecciona una tarea de la lista.
   - Haz clic en `Eliminar Tarea`.

3. **Recordatorios**:
   - Cuando una tarea está próxima, aparecerá un pop-up que permite:
     - **Completar la tarea**: Elimina la tarea de la lista.
     - **Posponer la tarea**: Permite reprogramar el recordatorio.

---

## Licencia

Este proyecto está bajo la **Licencia MIT**, lo que permite su uso, modificación y distribución sin restricciones. Consulta el archivo `LICENSE` para más detalles.

---

## Créditos

Desarrollado por IM@kodebidean, estudiante apasionado de la programación y la automatización.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar GorillaAlert, considera las siguientes áreas:

1. **Mejoras en la interfaz**:
   - Implementación de nuevos estilos visuales.
   - Añadir animaciones o transiciones.

2. **Nuevas funcionalidades**:
   - Integrar sincronización con calendarios externos.
   - Añadir soporte multiplataforma.

3. **Optimización del código**:
   - Mejorar la eficiencia del proceso en segundo plano.
   - Reducir el uso de memoria.

Para contribuir, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz tus cambios y realiza un commit (`git commit -m "Añade nueva funcionalidad"`).
4. Envía tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

---

## Contacto

Si tienes preguntas, sugerencias o simplemente quieres saludar, puedes contactarme en:

- GitHub: [kodebidean](https://github.com/kodebidean)
- Email: [kodebidean@gmail.com](mailto:kodebidean@gmail.com)
