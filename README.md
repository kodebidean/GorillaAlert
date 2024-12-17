# GorillaAlert 🍌

<p align="center">
    <strong>GorillaAlert es un gestor de tareas único y potente, diseñado no solo para organizar tus tareas, sino para garantizar que nunca olvides los eventos importantes. Su característica principal es la capacidad de interrumpir cualquier actividad con un recordatorio de pantalla completa, obligándote a prestar atención a la tarea pendiente. Ideal para personas que suelen estar profundamente concentradas en su trabajo, este programa asegura que no te pierdas recordatorios cruciales como eventos importantes, cumpleaños o tareas críticas.
</p>
<div align="center">
    <img src="GorillaAlert_ico.png" alt="GorillaAlert Screenshot" width="300">
</div>
        
## 🐒 Características principales 

- **Gestión de tareas**: Añade, elimina y visualiza tareas con facilidad.
- **Recordatorios inteligentes**: Recibe notificaciones emergentes que cubren toda la pantalla.
- **Inicio automático**: Configurable para ejecutarse al encender el equipo.
- **Diseño en desarrollo**: Este proyecto es funcional pero en constante evolución.

<br>

## 🐵 Requisitos del sistema

<table align="center">
<tr>
<td><strong>Sistema operativo</strong></td>
<td>Windows (64 bits)</td>
</tr>
<tr>
<td><strong>Python</strong></td>
<td>Versión 3.12 o superior</td>
</tr>
<tr>
<td><strong>Librerías necesarias</strong></td>
<td>tkinter, Pillow, pystray, pyinstaller</td>
</tr>
</table>

<br>

## 🙈 Instalación

1. **Clona el repositorio**:
    ```bash
        git clone <URL del repositorio>
        cd TaskManager
    ```
   
2. **Instala las dependencias necesarias**:
    ```bash
        pip install -r requirements.txt
    ```

3. **Compila el programa en un archivo .exe (opcional)**:
    ```bash
        pyinstaller --noconsole --onefile --icon=icono_gorila.ico main.py
    ```

4. **Mueve el programa compilado**:
* Crea una carpeta en C:\Archivos de programa\ llamada GorillaAlert.
* Copia el archivo GorillaAlert.exe y el archivo tasks.json (vacío inicialmente) a esa carpeta.

<br>

## 🙊 Uso
**Ejecución inicial**
    ```bash
        python main.py  # Para desarrolladores
    ```

**Configurar inicio automático**
1. Presiona Win + R, escribe shell:startup y presiona Enter.
2. Crea un acceso directo de GorillaAlert.exe en la carpeta de inicio.
3. Reinicia tu computadora para verificar.

<br>

## 🙉 Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

<br>

## 📫 Créditos y Contacto
Desarrollado por kodebidean, estudiante apasionado de la programación y la automatización.

<p align="center"> <a href="mailto:kodebidean@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-blue?style=flat-square&logo=gmail"></a> <a href="https://github.com/kodebidean"><img src="https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github"></a> </p>

<br>

## ➕ Contribuciones
<details> <summary>Áreas de mejora</summary> <ul> <li>Mejorar la interfaz visual</li> <li>Añadir nuevas funcionalidades como sincronización con calendarios</li> <li>Optimizar procesos en segundo plano</li> 
<li>zenflow: Actualización del README: eliminar funcionalidad en segundo plano, trabajando en primer plano para evitar problemas.</li> </ul> </details> 

