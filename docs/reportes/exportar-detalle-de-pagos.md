# Exportar el detalle de pagos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Filtrar el listado de pagos, revisar las columnas disponibles y generar el detalle
en PDF cuando la acción esté habilitada.

## Acceso condicional

El listado, sus filtros, columnas y la generación del archivo dependen de la sesión
y configuración. La exportación conserva el contexto del listado observado, pero no
garantiza formato, contenido completo, disponibilidad del archivo ni uso contable.

## Requisitos y datos

- Acceso al listado de pagos.
- Un criterio de revisión, por ejemplo fecha de venta, fecha de pago, documento o usuario.
- Un conjunto de resultados suficientemente acotado antes de generar el archivo.

## Punto de partida

Abra el listado de pagos disponible para su sesión.

## Pasos

1. Revise las columnas visibles antes de filtrar o exportar.
2. Aplique los filtros disponibles, en particular los rangos de fecha, documento o usuario cuando aparezcan.
3. Verifique que cada fila corresponde al criterio que desea revisar: venta, pago o registro.
4. Ajuste las columnas si necesita identificar mejor los resultados y conserve solo las necesarias.
5. Seleccione **Generar PDF** cuando la acción esté disponible.
6. Si la generación no se completa, reduzca el conjunto mediante filtros y vuelva a intentarlo.

## Campos y validaciones observados

El listado observado muestra datos de la venta y del pago, incluidos documento,
serie, correlativo, fechas de venta y pago, cliente, deuda, total, pagado, método,
detalle, número de operación y usuario. Permite filtrar fechas y algunos valores de
columna, editar o restablecer columnas y solicitar un PDF.

## Resultado revisado en fuente

La generación toma los parámetros y las columnas configuradas en el listado. La
fuente impone un límite de resultados para el PDF; cuando se supera, la solicitud no
debe tratarse como una exportación válida y requiere acotar los filtros.

## Advertencias y casos límite

No confunda la fecha de emisión de la venta, la fecha del pago y la fecha de registro.
El detalle puede incluir deuda y pagado junto con el pago individual: contraste el
campo que usa antes de sumar o comparar. No complete manualmente un archivo fallido
con datos no verificados.

## Problemas frecuentes y condiciones de detención

- Archivo no generado: revise filtros y reduzca resultados antes de repetir la acción.
- Columnas insuficientes: ajuste la vista antes de exportar; no suponga columnas ocultas.
- Totales o filas inesperados: detenga la distribución del archivo y revise fechas y filtros.
- Sin resultados: confirme el período y el criterio de fecha elegido antes de escalar.

## Verificaciones pendientes en runtime

- Límite efectivo de exportación, formato y descarga del PDF.
- Filtros, columnas y filas visibles para la sesión.
- Tratamiento de archivos generados y su uso operativo.

## Enlaces relacionados

- [Consultar pagos y deudas de ventas](consultar-pagos-y-deudas.md)
- [Buscar, filtrar y revisar el detalle de ventas](../ventas/consultar-ventas.md)
- [Consultar reportes consolidados y ventas por producto](../ventas/revisar-reportes-de-ventas.md)
