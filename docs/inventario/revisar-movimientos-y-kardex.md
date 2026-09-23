# Revisar movimientos y kardex de un producto

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Revisar el historial de movimientos de un producto en un almacén para reconocer el
origen de una variación de cantidad.

## Acceso condicional

La pantalla de movimientos y sus detalles dependen de la navegación disponible para
la sesión. Las operaciones que aparecen pueden variar según el producto y el entorno.

## Requisitos y datos

- Un producto y, cuando aplique, un almacén para acotar la consulta.
- Un período u operación que permita reconocer el movimiento investigado.

## Punto de partida

Desde el detalle de inventario del producto, seleccione el almacén que desea revisar.
La tabla revisada se carga para el producto y el almacén en contexto.

## Pasos

1. Confirme el producto y el almacén antes de leer la tabla.
2. Use los filtros disponibles de fecha, operación, tipo o estado para reducir el
   conjunto de movimientos.
3. Compare cantidad, saldo y los datos de lote o serie cuando estén presentes.
4. Abra el detalle de la fila que necesita investigar; el comportamiento depende del
   tipo de operación de origen.
5. Registre la diferencia para el procedimiento autorizado de su organización; no
   modifique el historial solo para hacer coincidir un valor esperado.

## Campos y validaciones observados

La tabla revisada incluye fecha, operación, tipo, lote, cantidad, precio, total,
saldo y estado. La interfaz ofrece filtros para operación, tipo y estado, y un rango
de fecha. Un detalle de ajuste solo se abre cuando existe el registro de seguimiento
de la operación; los mensajes y filtros exactos requieren verificación en runtime.

## Resultado revisado en fuente

La fuente obtiene movimientos para el producto y almacén seleccionados, entrega
valores de filtro y permite abrir un detalle según la operación de origen. No se
afirma que la tabla constituya un kardex fiscal, contable o aprobado.

## Advertencias y casos límite

Una misma pantalla puede reunir ventas, compras, transferencias, ajustes y otras
operaciones. No concluya la causa de una diferencia solo por el nombre de la fila;
revise el detalle disponible y el contexto operativo.

## Problemas frecuentes y condiciones de detención

- Sin filas tras aplicar filtros: limpie o revise el almacén y período elegidos.
- Operación no identificable: no infiera el origen; solicite revisión operativa.
- Detalle no disponible: no sustituya la evidencia por una corrección manual.

## Verificaciones pendientes en runtime

- Etiquetas, opciones de filtrado y formato de columnas en el entorno.
- Alcance de cada estado y el contenido visible de los detalles.
- Correspondencia entre el saldo mostrado y las operaciones reales del tenant.

## Enlaces relacionados

- [Consultar stock por almacén](consultar-stock-por-almacen.md)
- [Registrar un ajuste de inventario](registrar-ajuste.md)
- [Inventario](index.md)
