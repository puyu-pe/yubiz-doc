<a id="asignar-series-en-entradas-salidas-y-cargas"></a>

# 4.9 Asignar series en entradas, salidas y cargas

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Asignar las series requeridas durante una entrada, salida o carga, cuando el producto
use seguimiento por series y la opción esté habilitada.

## Acceso condicional

El seguimiento por series depende de la configuración del producto y del flujo. Esta
ficha trata la asignación durante movimientos, no el alta de series en el catálogo.

## Requisitos y datos

- Producto, almacén y lote cuando el flujo lo solicite.
- Series existentes para una salida o datos de series para una entrada.
- Cantidad coherente con las filas de series que se van a asignar.

## Punto de partida

Inicie una entrada, salida o carga que muestre controles de serie. Confirme primero el
producto, almacén y tipo de movimiento.

## Pasos

1. Para una entrada, agregue las filas de serie que correspondan a la cantidad.
2. Complete cada serie y los atributos adicionales que muestre la pantalla.
3. Para una salida, busque y seleccione las series disponibles para el lote y almacén.
4. Verifique que no haya series repetidas y que el total de series sea coherente.
5. En una carga, seleccione las series de contenedores disponibles para el lote y
   almacén antes de registrar la operación principal.

## Campos y validaciones observados

La entrada exige un valor de serie y aplica una validación de unicidad. Para categorías
de contenedor, añade tipo de propietario, propietario, contenido y estado de llenado.
La salida busca series por lote y almacén, impide agregarlas dos veces y exige al menos
una serie seleccionada. La obligatoriedad exacta depende del flujo y debe verificarse.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz reúne las series seleccionadas con el detalle del movimiento o carga. No
se afirma que asignar una serie cree una nueva serie de catálogo ni que confirme por
sí solo una variación de stock.

## Advertencias y casos límite

No registre una nueva serie desde este procedimiento si el flujo solo permite elegir
series existentes. Una serie repetida o sin lote/almacén identificable requiere detener
la operación y revisar la trazabilidad.

## Problemas frecuentes y condiciones de detención

- Serie duplicada: elimine la repetición antes de guardar.
- No aparecen series: confirme lote, almacén y seguimiento aplicable.
- Cantidad y filas no coinciden: no continúe hasta reconciliarlas.

## Enlaces relacionados

- [Gestionar series y trazabilidad de productos](../catalogo/gestionar-series.md)
- [Registrar ingresos y salidas de almacén](registrar-ingresos-y-salidas.md)
- [Registrar y consultar cargas de contenedores](gestionar-cargas-de-contenedores.md)
- [Inventario](index.md)
