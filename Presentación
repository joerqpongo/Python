from pptx import Presentation
from pptx.util import Inches
 
# Crear la presentación
prs = Presentation()
 
# Función para añadir diapositiva con título y contenido en bullet points
def add_slide_with_bullets(title, bullet_points):
    slide_layout = prs.slide_layouts[1]  # Diapositiva de título y contenido
    slide = prs.slides.add_slide(slide_layout)
    title_placeholder = slide.shapes.title
    body_placeholder = slide.placeholders[1]
 
    title_placeholder.text = title
    for point in bullet_points:
        p = body_placeholder.text_frame.add_paragraph()
        p.text = point
 
# Diapositiva de portada
slide_layout = prs.slide_layouts[0]  # Título
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Informe sobre el Sistema de Fichajes"
subtitle.text = "Descripción y Configuraciones"
 
# Diapositiva 1: Resumen
add_slide_with_bullets("Resumen", [
    "Descripción de las características y configuraciones del sistema de fichajes.",
    "Personalización del registro de entradas y salidas.",
    "Monitoreo y control de la jornada laboral."
])
 
# Diapositiva 2: Dispositivos de Fichaje
add_slide_with_bullets("Dispositivos de Fichaje", [
    "Dispositivos desde los que se puede hacer checkin.",
    "Dispositivo facial: fichajes biométricos que solo registran la acción de fichaje.",
    "Dispositivo facial - Tiempo entre fichajes: tiempo mínimo en segundos entre dos fichajes faciales.",
    "Dispositivo facial - Reinicio a Entrada: se marca como entrada si han pasado más de X horas desde el último fichaje."
])
 
# Diapositiva 3: Validaciones y Reglas de Fichaje (Parte 1)
add_slide_with_bullets("Validaciones y Reglas de Fichaje (Parte 1)", [
    "Repetir Entrada/Salida: evita repeticiones de eventos de entrada o salida.",
    "Corregir Entradas/Salidas propias: permite la corrección o adición manual de fichajes.",
    "Permitir tipos de entradas distintos al laboral: si está desactivado, el tipo de entrada será siempre laboral.",
    "Permitir tipos de salidas distintos al laboral: si está desactivado, el tipo de salida será siempre laboral."
])
 
# Diapositiva 4: Validaciones y Reglas de Fichaje (Parte 2)
add_slide_with_bullets("Validaciones y Reglas de Fichaje (Parte 2)", [
    "Tiempo limitado para editar/borrar un fichaje: tiempo máximo permitido para editar o cancelar un fichaje.",
    "Denegar fichaje de entrada antes de hora: margen de antelación permitido para el primer fichaje.",
    "Impedir fichaje sin 12 horas de descanso: mínimo de 12 horas entre jornadas.",
    "Requiere geoposición para fichar: necesidad de activar la geoposición para poder fichar."
])
 
# Diapositiva 5: Validaciones y Reglas de Fichaje (Parte 3)
add_slide_with_bullets("Validaciones y Reglas de Fichaje (Parte 3)", [
    "Limitar distancia al centro de trabajo: obliga a fichar a una distancia máxima del centro de trabajo (solo móvil).",
    "Ignorar tiempo antes de la hora oficial de entrada: se ignora el tiempo fichado antes de la hora indicada.",
    "Permitir fichajes en días no laborables: si está desactivado, no se podrá fichar en días no laborables o festivos.",
    "Permitir fichajes en vacaciones: si está desactivado, no se podrá fichar durante las vacaciones.",
    "Permitir fichajes con baja laboral: se podrá fichar estando de baja cuando exista el parte de alta.",
    "Permitir fichajes sin turno asignado: se podrá fichar sin tener un turno asignado."
])
 
# Diapositiva 6: Validaciones y Reglas de Fichaje (Parte 4)
add_slide_with_bullets("Validaciones y Reglas de Fichaje (Parte 4)", [
    "Notificar fichajes después de jornada laboral: notifica al responsable cuando un empleado ficha después del tiempo configurado.",
    "Exento de fichar: indica qué grupo o usuario está exento de fichar.",
    "Mostrar fichajes: muestra al empleado solo fichajes del periodo seleccionado."
])
 
# Diapositiva 7: Preferencias de Configuración (Parte 1)
add_slide_with_bullets("Preferencias de Configuración (Parte 1)", [
    "Duración de la sesión: minutos sin actividad antes de cerrar la sesión.",
    "Zona Horaria: muestra el tiempo teniendo en cuenta la zona horaria.",
    "Mostrar personal de la empresa: indica si cualquier empleado puede ver el listado de personal.",
    "Mostrar código ERP del empleado: indica si en los listados del responsable se muestran los códigos ERP de los empleados."
])
 
# Diapositiva 8: Preferencias de Configuración (Parte 2)
add_slide_with_bullets("Preferencias de Configuración (Parte 2)", [
    "Informe de jornada: el empleado puede ver su informe de jornada.",
    "Mostrar exceso de jornada: el empleado puede ver el exceso (positivo o negativo) de jornada.",
    "Planner - Acceso para empleados y supervisores: permite acceso al planner a usuarios que no sean managers.",
    "Desactivar secciones: oculta secciones en la App y la Web (vacaciones, notas de gasto, etc.).",
    "Habilitar bolsa de horas: habilita la bolsa de horas.",
    "Habilitar avatares de empleados: habilita fotos de avatar personalizadas.",
    "Mostrar logo de empresa en cabecera: posibilidad de mostrar u ocultar el logo de la empresa en la cabecera web."
])
 
# Diapositiva 9: Notificaciones y Correos (Parte 1)
add_slide_with_bullets("Notificaciones y Correos (Parte 1)", [
    "Copias de correos al asesor: el asesor recibe todos los correos que reciben los managers.",
    "Enviar copias de correos al supervisor: el supervisor recibe todos los correos de los usuarios que supervise.",
    "Enviar correos duplicados al manager con supervisores: el manager recibe también los correos enviados a los supervisores.",
    "Notificaciones mobile: notificaciones emergentes al teléfono.",
    "Recordatorio de fichaje: notificaciones de recordatorio de fichaje."
])
 
# Diapositiva 10: Notificaciones y Correos (Parte 2)
add_slide_with_bullets("Notificaciones y Correos (Parte 2)", [
    "Informe de Incidencias de fichaje para los responsables: se envía el informe de incidencias de fichaje a los responsables.",
    "Informe de tareas pendientes a responsables: se envía el informe de tareas pendientes.",
    "Envío de notificaciones por email al empleado: notificaciones de permisos, vacaciones, incidencias, documentos, etc.",
    "Envío de peticiones por email al responsable: el responsable recibe correos de peticiones de permisos, vacaciones, incidencias, notas de gasto, bajas y formularios completados.",
    "Mostrar aviso de comunicaciones pendientes: aviso si hay comunicaciones pendientes de leer.",
    "Mostrar aviso de tareas pendientes: aviso si hay tareas pendientes por hacer.",
    "Periodicidad notificaciones de tareas pendientes: periodicidad de notificaciones por email de las tareas pendientes."
])
 
# Diapositiva 11: Horarios y Turnos (Parte 1)
add_slide_with_bullets("Horarios y Turnos (Parte 1)", [
    "Horario por defecto: indica el horario por defecto para los nuevos empleados.",
    "Sistema avanzado de turnos: disponibilidad del sistema avanzado de turnos.",
    "Turnos - supervisión: los supervisores pueden gestionar sus equipos de turnos.",
    "Máxima duración de la jornada: tiempo máximo que puede durar una jornada.",
    "Ocultar tipos de permiso genéricos: oculta los tipos de permisos por defecto.",
    "Tipos de permiso disponibles para el empleado: configuración de tipos de permiso según usuario, departamento, etc."
])
 
# Diapositiva 12: Horarios y Turnos (Parte 2)
add_slide_with_bullets("Horarios y Turnos (Parte 2)", [
    "Permitir auto aceptación de ausencias: el responsable o supervisor puede aceptar sus propios permisos, vacaciones, bajas, etc.",
    "Permitir solicitar permisos cuando superen el límite anual: los empleados pueden solicitar permisos cuando superen el límite anual.",
    "Permitir medios días de vacaciones: se permite solicitar medios días de vacaciones.",
    "Mostrar días de vacaciones generados durante el año: muestra los días de vacaciones generados hasta la fecha.",
    "Días de vacaciones laborales según turnos: muestra el número de días de vacaciones.",
    "Cambiar contraseñas de empleados: permiso al supervisor para modificar contraseñas.",
    "Crear vacaciones, incidencias, etc.: permiso al supervisor para crear solicitudes de vacaciones, notas de gasto e incidencias."
])
 
# Diapositiva 13: Módulo de Teletrabajo
add_slide_with_bullets("Módulo de Teletrabajo", [
    "Habilitar módulo de teletrabajo.",
    "Notificar al empleado: envía un correo cuando el responsable responde peticiones de teletrabajo.",
    "Máximo número de días de teletrabajo al mes: establece el máximo de días de teletrabajo por mes.",
    "Máximo de horas de teletrabajo al año: establece el máximo de horas de teletrabajo al año."
])
 
# Diapositiva 14: Conclusión
add_slide_with_bullets("Conclusión", [
    "El sistema de fichajes proporciona una solución completa para el control y gestión de la jornada laboral.",
    "Personalización y flexibilidad en las reglas de fichaje.",
    "Notificaciones y alertas automáticas para una mejor supervisión.",
    "Soporte para teletrabajo y jornadas flexibles."
])
 
# Guardar la presentación
pptx_file = "Informe_Sistema_de_Fichajes.pptx"
prs.save(pptx_file)
 
pptx_file