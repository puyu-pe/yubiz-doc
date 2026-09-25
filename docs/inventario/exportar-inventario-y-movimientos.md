<a id="exportar-inventario-y-movimientos"></a>

# 4.7 Exportar inventario y movimientos

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

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
cantidad, precio, total, saldo y estado. La interfaz evita una exportación si supera
10 000 filas. Las columnas efectivamente disponibles pueden variar según la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz consulta los registros con los parámetros de la grilla, formatea valores
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

## Enlaces relacionados

- [Consultar stock por almacén](consultar-stock-por-almacen.md)
- [Revisar movimientos y kardex de un producto](revisar-movimientos-y-kardex.md)
- [Inventario](index.md)
