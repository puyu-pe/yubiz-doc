<a id="consultar-reportes-consolidados-y-ventas-por-producto"></a>

# 2.14 Consultar reportes consolidados y ventas por producto

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo
Consultar los filtros y resultados disponibles en los reportes consolidados de ventas y de productos vendidos.

## Acceso condicional
Los reportes, filtros, columnas, usuarios, vendedores, establecimientos y exportaciones pueden variar según la sesión y configuración disponible.

## Requisitos y datos
- Periodo de consulta.
- Establecimiento, usuario o vendedor, cuando los filtros estén disponibles.
- Criterio para revisar resultados por venta o producto.

## Punto de partida
En un reporte de ventas disponible en el menú de reportes.

## Pasos
1. Ingrese las fechas de inicio y fin del periodo a revisar.
2. Seleccione establecimiento, usuario o vendedor solo cuando el filtro esté disponible.
3. Seleccione **Buscar** y revise que el periodo y los filtros mostrados sean los esperados.
4. En el consolidado, contraste las secciones de ventas emitidas, anuladas, métodos de pago y notas de crédito.
5. En ventas por producto, revise la tabla y use limpiar filtros, restablecer columnas o exportar solo si aparecen.

## Campos y validaciones observados
Los reportes observados incluyen fechas, establecimiento y usuario; el consolidado también presenta vendedor. El navegador muestra secciones y tablas de resultados, y el reporte por producto ofrece controles de filtros, columnas y exportación.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado
El navegador solicita datos para los filtros elegidos y presenta tablas o secciones de resumen. Los totales, alcance de los datos, exportaciones y su significado operativo pueden variar según la configuración disponible.

## Advertencias y casos límite
No use un total o un reporte exportado como conciliación definitiva sin contrastarlo con el periodo y los datos de origen. Un reporte no visible o un filtro sin resultados no prueba ausencia de operaciones.

## Problemas frecuentes y condiciones de detención
- Periodo o filtro incorrecto: corríjalo antes de interpretar resultados.
- Resultado inesperado: revise filtros y datos de origen antes de escalar.
- Exportación no disponible: no sustituya el control por un procedimiento no observado.

## Enlaces relacionados
- [Buscar, filtrar y revisar el detalle de ventas](consultar-ventas.md)
- [Vendedores y comisiones](vendedores-y-comisiones.md)
