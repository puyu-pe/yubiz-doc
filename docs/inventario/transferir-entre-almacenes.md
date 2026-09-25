<a id="transferir-productos-entre-almacenes"></a>

# 4.4 Transferir productos entre almacenes

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar una transferencia interna entre dos almacenes distintos con los productos
y datos de seguimiento correspondientes.

## Acceso condicional

La disponibilidad de transferencias, documentos y almacenes depende de la sesión y
la configuración. Esta ficha no afirma quién puede registrar, aprobar o imprimir una
transferencia.

## Requisitos y datos

- Documento y serie disponibles para la operación.
- Fecha de movimiento, almacén de origen y almacén de destino.
- Productos, cantidades y, si aplican, lote o series.
- Responsable, detalle imprimible u observación solo cuando correspondan.

## Punto de partida

Abra el registro de transferencia interna si está disponible. La pantalla revisada
presenta documento, serie, fecha, origen, destino y una tabla de productos.

## Pasos

1. Seleccione el documento disponible y revise la serie cargada para ese documento.
2. Elija fecha, almacén de origen y almacén de destino.
3. Confirme que origen y destino son distintos antes de agregar productos.
4. Agregue cada producto y su cantidad; complete lote o series cuando el producto
   los requiera.
5. Incluya detalle u observación solo si el procedimiento de su organización lo usa.
6. Revise el resumen y registre la transferencia.
7. Si la interfaz informa un error, deténgase y confirme el resultado antes de
   volver a enviar la operación.

## Campos y validaciones observados

La interfaz contiene documento, serie, fecha de movimiento, responsable,
origen, destino, productos, cantidades, detalle para impresión y observación. Para
una transferencia interna, el navegador aplica una validación para que origen y
destino no sean iguales y adapta el stock mostrado al almacén de origen. Los límites,
campos obligatorios y mensajes pueden variar según la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz separa el envío de transferencias internas de otras transferencias y
devuelve una respuesta de éxito o error. No se garantiza aquí la actualización final
del stock, la impresión ni el estado de aprobación sin evidencia del entorno.

## Advertencias y casos límite

No sustituya una transferencia por un ajuste para mover productos entre almacenes.
No registre la misma operación más de una vez si la respuesta es incierta; primero
revise el listado o el historial disponible.

## Problemas frecuentes y condiciones de detención

- Origen y destino iguales: elija almacenes distintos.
- Serie o lote sin identificar: detenga la operación y complete la trazabilidad.
- Stock o cantidad no explicables: revise movimientos antes de registrar.
- Error de envío: no duplique la transferencia sin confirmar el resultado.

## Enlaces relacionados

- [Consultar stock por almacén](consultar-stock-por-almacen.md)
- [Revisar movimientos y kardex de un producto](revisar-movimientos-y-kardex.md)
- [Inventario](index.md)
