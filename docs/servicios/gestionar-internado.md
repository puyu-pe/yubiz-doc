<a id="consultar-un-internado-y-agregar-procedimientos"></a>

# 5.3 Consultar un internado y agregar procedimientos

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Revisar el detalle de una orden de servicio y añadir un procedimiento cuando el
registro siga disponible para esa acción.

## Acceso condicional

El menú declarado incluye **Internados**. Desde la lista, el detalle muestra los
datos de cliente, unidad, intervención, observaciones, ítems y procedimientos.

## Requisitos y datos

- Orden identificada en la lista.
- Datos autorizados para el procedimiento, incluidos ítems si la pantalla los pide.

## Punto de partida

En **Internado**, abra **Internados** y seleccione la orden que necesita revisar.

## Pasos

1. Revise cliente, unidad, fechas, responsable y observaciones del detalle.
2. Verifique los ítems registrados y los totales antes de cambiar el registro.
3. Abra **Detalles procedimiento** y revise los procedimientos existentes.
4. Si la acción **Añadir** está disponible, complete el procedimiento y sus ítems.
5. Guarde y vuelva al detalle para comprobar que la información aparece en la lista.

## Campos y validaciones observados

El detalle presenta procedimiento, operador, descripción, recomendaciones y fecha.
Al agregar, la interfaz puede asociar almacén e ítems; valida el detalle antes de
guardarlo y recalcula los totales de la orden.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo registra el procedimiento y, si hay ítems, los incorpora a la orden dentro
de una transacción. La visualización final y los mensajes requieren verificación.

## Advertencias y casos límite

La acción de añadir se muestra deshabilitada para estados finales o anulados.
Deténgase si el estado no permite el cambio o si los ítems no son trazables.

## Problemas frecuentes y condiciones de detención

- La orden no aparece: revise filtros y no cree una orden duplicada.
- Añadir no está disponible: no intente forzar el procedimiento.
- Faltan datos de ítems: complete datos válidos o detenga el registro.

## Enlaces relacionados

- [Registrar una orden de servicio o internado](registrar-internado.md)
- [Convertir, anular o imprimir un internado](cerrar-o-anular-internado.md)
