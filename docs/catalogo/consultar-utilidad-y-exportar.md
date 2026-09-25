<a id="consultar-utilidad-y-exportar-el-catálogo"></a>

# 3.12 Consultar utilidad y exportar el catálogo

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Consultar la lista de utilidad de productos, ajustar la vista disponible y generar
una salida cuando esas acciones estén habilitadas para la sesión.

## Acceso condicional

La lista y las exportaciones dependen del módulo y la sesión. Las columnas, filtros,
formatos y permisos visibles pueden variar según la configuración del entorno.

## Requisitos y datos

- Criterio de búsqueda o filtro que permita acotar la consulta.
- Período y columnas requeridos por el reporte disponible.
- Autorización para consultar o descargar información del catálogo.

## Punto de partida

Abra la lista de utilidad de productos si está disponible en la navegación. Antes de
exportar, revise los filtros y las columnas seleccionadas.

## Pasos

1. Revise la lista y aplique los filtros disponibles para acotar los productos.
2. Ajuste las columnas solo si necesita una vista específica para la consulta.
3. Verifique que los resultados y sus totales tengan sentido para el criterio usado.
4. Use la acción disponible para generar PDF o Excel cuando corresponda.
5. Si la exportación no se genera, reduzca el conjunto de resultados y vuelva a
   revisar los filtros antes de intentarlo nuevamente.

## Campos y validaciones observados

La interfaz incluye edición de columnas, limpieza y restablecimiento de
filtros, además de acciones para PDF y Excel. La consulta incorpora filtros de
producto y campos de cantidad, costo, venta y utilidad. La exportación revisada limita
la salida a 10 000 registros. La interpretación financiera de columnas y totales debe
confirmarse en el entorno.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz genera una lista paginada y puede preparar salidas PDF o Excel a partir de
los parámetros y columnas seleccionados. No se afirma que la descarga se entregue,
que los totales sean definitivos ni que la información tenga un uso contable o fiscal.

## Advertencias y casos límite

No use esta consulta para modificar precios, costos o productos. Trate los resultados
como información operativa hasta validar filtros, período y significado de cada
columna. Evite exportar conjuntos amplios si no necesita todos los registros.

## Problemas frecuentes y condiciones de detención

- Demasiados registros para exportar: reduzca el resultado antes de generar la salida.
- Totales inesperados: revise filtros, período y columnas antes de comunicar datos.
- Opción de exportación ausente: confirme módulo, permiso y sesión.
- No puede interpretar una columna: deténgase y valide el reporte con el responsable.

## Enlaces relacionados

- [Crear y editar productos del catálogo](gestionar-productos.md)
- [Configurar precios de venta por tipo y establecimiento](configurar-precios-de-venta.md)
- [Catálogo](index.md)
