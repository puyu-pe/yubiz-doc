# Gestionar productos y reportes externos

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Usar los recorridos especializados para PLE, carga de ticket y reporte de ingresos externos sin exponer datos operativos.

## Acceso condicional

El menú declarado incluye **Reporte PLE**, **Cargar ticket abono** y **Reporte de ingresos externos**. La disponibilidad y el propósito operativo requieren verificación.

## Requisitos y datos

- Archivo de texto autorizado para la carga, cuando la acción esté disponible.
- Período y filtros para consultar el reporte externo.

## Punto de partida

Abra la acción especializada que corresponda y revise los campos visibles antes de seleccionar un archivo o solicitar un reporte.

## Pasos

1. Para PLE o reporte externo, complete los filtros disponibles y ejecute la consulta.
2. Revise filas, total y período antes de exportar.
3. Para una carga de ticket, seleccione un archivo de texto autorizado.
4. Revise la vista previa de los datos que muestre la interfaz.
5. Deténgase ante datos incompletos o inesperados; no confirme la carga sin revisión.

## Campos y validaciones observados

La interfaz de carga acepta archivos TXT de hasta 4 MB antes de generar una vista previa. La fuente rechaza secciones, fechas, números, importes o ítems no válidos. El reporte externo limita la exportación a 10 000 filas y el período a tres meses.

## Resultado revisado en fuente

La fuente puede mostrar una vista previa, guardar registros asociados a la carga y generar un reporte exportable. Sus efectos, mensajes y archivos finales son pendientes.

## Advertencias y casos límite

No cargue archivos con datos no autorizados ni use esta guía para interpretar saldos. Reduzca el período si supera el límite y deténgase ante una vista previa incorrecta.

## Problemas frecuentes y condiciones de detención

- Archivo no TXT o mayor que el límite: elija un archivo válido.
- Datos de vista previa incompletos: no continúe con el guardado.
- Período demasiado amplio: reduzca filtros antes de exportar.

## Verificaciones pendientes en runtime

- Formatos admitidos, etiquetas, vista previa, mensajes y resultados de carga.
- Campos, exportación y significado de los datos del reporte externo.

## Enlaces relacionados

- [Módulos especializados](index.md)
