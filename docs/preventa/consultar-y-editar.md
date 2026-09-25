<a id="consultar-y-editar-preventas"></a>

# 7.2 Consultar y editar preventas

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Buscar una preventa en la lista moderna, revisar su detalle y actualizar la
observación o los ítems mientras el estado permita la acción.

## Acceso condicional

La lista moderna es un recorrido distinto del pedido heredado. Los filtros, columnas,
estados y edición disponibles dependen de la sesión; no confirme que toda preventa
pueda editarse ni que un cambio preserve reservas o resultados operativos.

## Requisitos y datos

- Un criterio como fecha, usuario, establecimiento, almacén, cliente o estado.
- Identificación de la preventa antes de abrir el detalle.
- Observación e ítems correctos si la edición está disponible.

## Punto de partida

Abra la **Lista de preventas** disponible para su sesión.

## Pasos

1. Aplique filtros o ajuste columnas para encontrar la preventa.
2. Abra el detalle y revise documento, fecha, cliente, almacén, observación e ítems.
3. Confirme el estado antes de elegir **Editar**.
4. Actualice la observación o los ítems disponibles y revise cantidades, precios e importes.
5. Seleccione **Actualizar** y vuelva a la lista para revisar el resultado.

## Campos y validaciones observados

La lista muestra documento, serie, correlativo, fecha, usuario, establecimiento,
almacén, cliente, total y estado, con filtros y columnas configurables. El formulario
de edición carga cliente, documento, fecha, usuario, observación e ítems; envía el
identificador, la observación y el detalle de ítems para validación.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El detalle moderno expone los estados borrador, confirmada, procesada y cancelada.
La edición aparece solo para borrador en la interfaz. La interfaz maneja actualizaciones
y movimientos de reserva, pero su efecto real pueden variar según la configuración disponible.

## Advertencias y casos límite

No edite desde el pedido heredado una preventa de esta lista. Una fila sin resultados
puede responder a filtros o estado. Revise el estado antes de modificar ítems.

## Problemas frecuentes y condiciones de detención

- Preventa no encontrada: limpie o ajuste filtros antes de concluir que no existe.
- Estado no editable: no fuerce una modificación; revise el detalle y el contexto.
- Ítems o total inesperados: detenga la actualización y revise el origen.

## Enlaces relacionados

- [Crear un pedido de preventa](crear-pedido.md)
- [Confirmar, anular o convertir una preventa en venta](confirmar-anular-convertir.md)
