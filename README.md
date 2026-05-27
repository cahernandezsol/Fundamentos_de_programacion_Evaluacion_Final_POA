# Fundamentos_de_programacion_Evaluacion_Final_POA

Repositorio público con la entrega final de la asignatura Fundamentos de programación.

Contenido
- `213022_711_Fase_5_Camilo_Hernandez.py` : Script que clasifica sesiones por nivel de compromiso (Alto / Medio / Bajo).

# Fundamentos_de_programacion_Evaluacion_Final_POA

Repositorio público con la entrega final de la asignatura "Fundamentos de programación" — Evaluación POA (Prueba Objetiva Abierta).

---

## Problema

Una matriz almacena datos de sesiones de clientes con el formato: **[ID Cliente, Duración (segundos), Eventos Clics]**. Se necesita una herramienta para evaluar el nivel de compromiso de cada sesión.

### Requisitos de Desarrollo

#### 1. Datos Iniciales
- Una matriz con al menos 5 filas de datos.
- Formato: `[ID_Dispositivo, Duración_en_segundos, Cantidad_de_Clics]`

#### 2. Módulos
Se requiere una función para calcular la clasificación de compromiso de una sesión basándose en su duración y clics.

#### 3. Lógica de Negocio
Clasificar cada sesión según los siguientes criterios:

- **"Alto"**: Duración > 180 segundos **Y** Clics > 8
- **"Bajo"**: Duración < 60 segundos **O** Clics < 3
- **"Medio"**: Todos los demás casos

#### 4. Salida
Generar un informe listando el ID del cliente y su clasificación final con alineación clara de columnas.
