# Convertir, anular y consultar reportes de estancias

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Revisar una estancia antes de iniciar una conversión o anulación y consultar el
reporte disponible, sin afirmar que una acción haya quedado completada en un
entorno real.

## Acceso condicional

Abra el detalle de la estancia desde **Estancias**. Para consultar resultados,
abra el reporte declarado del mismo módulo y use datos ficticios en cualquier
prueba permitida.

## Punto de partida

Identifique la estancia correcta y revise su detalle antes de iniciar una acción.

## Requisitos y datos

- Una estancia identificada desde la lista o su detalle.
- Información de tiempo y relaciones disponibles para el caso.
- Filtros disponibles en el entorno para consultar el reporte.

## Pasos

1. Abra el detalle y confirme que sujeto, ítems, importe y tiempo corresponden
   al caso correcto.
2. Revise la información de tiempo disponible antes de solicitar una conversión.
3. Si el flujo ofrece una confirmación, revise las personas relacionadas que se
   muestran y no sustituya esa información por una autorización de software.
4. Complete la conversión solo cuando el entorno y el procedimiento operativo
   aplicable lo permitan; confirme el resultado visible después de ejecutarla.
5. Para anular, seleccione exclusivamente el registro confirmado y deténgase si
   hay dudas sobre su estado o impacto.
6. Abra el reporte, seleccione filtros disponibles y revise los resultados como
   una consulta; no los use como prueba de cierre operativo sin verificación.

## Campos y validaciones observados

- La fuente obtiene información de tiempo y relaciones de recojo antes de
  mostrar la confirmación de conversión.
- Si una estancia no puede encontrarse o la operación de anulación no se
  completa, la fuente informa un error; no se garantiza aquí qué estados son
  anulables en cada entorno.
- El reporte carga una vista con establecimientos asociados al contexto de
  sesión; filtros, columnas y resultados visibles quedan pendientes de runtime.

## Resultado revisado en fuente

La fuente contiene recorridos para preparar conversión, anular una estancia y
consultar un reporte. La finalización, mensajes, documentos generados y efectos
posteriores deben comprobarse en el entorno.

## Advertencias y casos límite

Conversión y anulación pueden cambiar el caso; confirme el detalle antes de continuar.

## Problemas frecuentes y condiciones de detención

- El detalle no corresponde al caso: no convierta ni anule.
- La opción no está disponible o aparece un error: deténgase y conserve el
  contexto para revisión; no repita acciones irreversibles a ciegas.
- El reporte no muestra lo esperado: revise filtros y contexto antes de extraer
  conclusiones operativas.

## Verificaciones pendientes en runtime

- Estados que permiten convertir o anular y los mensajes que se muestran.
- Resultado posterior de la conversión o anulación.
- Filtros, columnas, exportaciones y datos del reporte.

## Enlaces relacionados

- [Consultar las estancias del día, la lista y el detalle](gestionar-estancias.md)
- [Gestionar sujetos y personas relacionadas](gestionar-personas-de-la-estancia.md)
