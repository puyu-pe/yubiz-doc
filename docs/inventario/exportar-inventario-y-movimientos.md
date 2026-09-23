# Exportar inventario y movimientos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Generar un archivo de inventario o de movimientos con el contexto y filtros que se
estén consultando, cuando la opción de exportación esté disponible.

## Acceso condicional

La exportación depende de la pantalla y sesión disponibles. El archivo resultante no
sustituye una conciliación ni confirma una interpretación contable.

## Requisitos y datos

- Una consulta de inventario o el detalle de movimientos de un producto.
- Filtros y almacén revisados antes de generar el archivo.

## Punto de partida

Abra la grilla correspondiente. Para movimientos, confirme producto y almacén antes
de solicitar la exportación.

## Pasos

1. Aplique o revise los filtros de la grilla antes de exportar.
2. En movimientos, confirme si la consulta corresponde a un almacén o a todos los
   almacenes del producto.
3. Use la opción de exportación disponible y espere el enlace o mensaje de resultado.
4. Abra el archivo y revise que las columnas y filas respondan al contexto elegido.
5. Si necesita volver a exportar, ajuste filtros primero; no asuma que el archivo se
   actualiza solo tras una operación posterior.

## Campos y validaciones observados

La grilla de inventario muestra almacén, producto, códigos, categoría, marca, modelo,
medida, stock mínimo y stock. La de movimientos incluye fecha, operación, tipo, lote,
cantidad, precio, total, saldo y estado. La fuente rechaza una exportación si supera
10 000 filas. Las columnas efectivamente disponibles requieren verificación en runtime.

## Resultado revisado en fuente

La fuente consulta los registros con los parámetros de la grilla, formatea valores
numéricos y genera un enlace de descarga. Para movimientos incorpora el contexto de
producto y almacén; cuando se consulta todo, calcula un total de almacenes. No se
afirma precisión contable, fiscal ni exhaustividad del archivo sin comprobarlo.

## Advertencias y casos límite

Una exportación refleja el filtro enviado, no una garantía de disponibilidad actual.
Reduzca el conjunto cuando exceda el límite observado y proteja el archivo según el
procedimiento de su organización.

## Problemas frecuentes y condiciones de detención

- Exceso de registros: reduzca filtros antes de reintentar.
- Almacén o producto equivocado: corrija el contexto antes de descargar.
- Archivo no identificable: no lo distribuya hasta confirmar sus columnas y período.

## Verificaciones pendientes en runtime

- Permisos, formato, destino del enlace y límites efectivos de exportación.
- Aplicación real de cada filtro y actualización posterior a operaciones.
- Uso autorizado y significado contable de las columnas exportadas.

## Enlaces relacionados

- [Consultar stock por almacén](consultar-stock-por-almacen.md)
- [Revisar movimientos y kardex de un producto](revisar-movimientos-y-kardex.md)
- [Inventario](index.md)
