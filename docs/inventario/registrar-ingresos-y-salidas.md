# Registrar ingresos y salidas de almacén

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Registrar un ingreso o una salida de almacén mediante el tipo de documento disponible
y los datos de origen o destino correspondientes.

## Acceso condicional

Las acciones de ingreso y salida, los documentos y las opciones de origen o destino
dependen de la configuración y de la sesión. No se asumen permisos ni consecuencias
tributarias, contables o de despacho.

## Requisitos y datos

- Documento, serie y fecha de movimiento disponibles.
- Almacén y descripción de la contraparte cuando correspondan.
- Productos, cantidades y datos de lote o serie si se solicitan.

## Punto de partida

Abra el registro de ingreso o salida de almacén si está disponible. Ambas entradas
revisadas usan una pantalla con datos del movimiento y una tabla de productos.

## Pasos

1. Seleccione el documento y revise la serie que se carga para él.
2. Confirme la fecha y, si corresponde, el responsable.
3. Para un ingreso, complete el origen disponible y el almacén de destino.
4. Para una salida, confirme el almacén de origen y complete el destino disponible.
5. Agregue los productos y cantidades; complete lote o series cuando se soliciten.
6. Revise detalle y observación antes de registrar.
7. Tras guardar, compruebe el listado o historial disponible antes de repetir la
   operación.

## Campos y validaciones observados

La pantalla revisada incluye documento, serie, fecha, responsable, tipos y valores de
origen/destino, productos, cantidades, detalle e información interna. El navegador
reconfigura los campos según el documento: ingreso usa una descripción de origen y
almacén de destino; salida usa almacén de origen y una descripción de destino. Los
requisitos exactos y las validaciones de cantidades deben verificarse en runtime.

## Resultado revisado en fuente

La fuente prepara el encabezado y detalle de la operación, incluyendo productos,
cantidades y seguimiento, y los envía al flujo de transferencia externo. El servidor
responde éxito o error; el efecto final sobre existencias y documentos queda pendiente
de comprobación en el entorno.

## Advertencias y casos límite

No convierta una salida o ingreso en una transferencia interna: cada flujo describe
orígenes y destinos distintos. No interprete el documento seleccionado como prueba de
un cumplimiento fiscal o de una autorización organizacional.

## Problemas frecuentes y condiciones de detención

- Documento o serie no disponibles: no sustituya valores sin confirmar el contexto.
- Origen o destino incorrecto: corrija antes de agregar productos.
- Seguimiento incompleto: detenga el registro hasta identificar lote o series.
- Resultado incierto: confirme el historial antes de reenviar.

## Verificaciones pendientes en runtime

- Nombres, documentos, series y campos obligatorios disponibles en la sesión.
- Reglas de stock, trazabilidad y mensajes de éxito o error.
- Resultado operativo, fiscal, contable y de despacho de cada tipo de movimiento.

## Enlaces relacionados

- [Transferir productos entre almacenes](transferir-entre-almacenes.md)
- [Revisar movimientos y kardex de un producto](revisar-movimientos-y-kardex.md)
- [Inventario](index.md)
