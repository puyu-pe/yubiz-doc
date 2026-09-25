<a id="registrar-y-consultar-cargas-de-contenedores"></a>

# 4.8 Registrar y consultar cargas de contenedores

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar o consultar una carga de contenedores cuando el módulo especializado esté
habilitado, manteniéndola separada de las órdenes de carga de distribución.

## Acceso condicional

Esta capacidad es condicional por módulo, configuración y sesión. Una carga de
contenedores no debe interpretarse como una orden de carga de distribución.

## Requisitos y datos

- Contenido, documento, serie y almacén disponibles.
- Contenedores, cantidades, medida y datos de lote o serie cuando se soliciten.

## Punto de partida

Abra la lista de cargas de contenedores si está disponible. Use los filtros para
revisar registros existentes o inicie uno nuevo con el contenido y almacén definidos.

## Pasos

1. Seleccione el contenido y el almacén; revise el stock de solo lectura mostrado.
2. Elija documento y serie disponibles.
3. Agregue cada contenedor con cantidad, descripción, medida y seguimiento aplicable.
4. Revise el total, detalle e información interna antes de registrar.
5. Tras guardar, consulte el detalle o la impresión disponible para comprobar el
   resultado sin asumir un efecto adicional.

## Campos y validaciones observados

La pantalla revisada contiene contenido, documento, serie, almacén, stock de solo
lectura, contenedores, cantidad, descripción, medida, total, detalle y observación
interna. La lista permite filtrar por documento, fecha, usuario y establecimiento.
La obligatoriedad y los límites exactos pueden variar según la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El navegador actualiza el stock según contenido y almacén, envía cabecera y detalles,
y puede abrir o imprimir el resultado. La lista entrega registros paginados y totales.
No se afirma una salida de almacén, despacho o entrega por registrar una carga.

## Advertencias y casos límite

Los contenedores pueden requerir lotes o series. No mezcle este flujo con una orden
de carga de distribución ni use el total como garantía de stock disponible.

## Problemas frecuentes y condiciones de detención

- Módulo ausente: confirme su habilitación sin asumir acceso.
- Stock o seguimiento no identificables: detenga el registro.
- Resultado de envío incierto: consulte la lista antes de repetir la carga.

## Enlaces relacionados

- [Asignar series en entradas, salidas y cargas](asignar-series-en-movimientos.md)
- [Gestionar lotes de productos](../catalogo/gestionar-lotes.md)
- [Inventario](index.md)
