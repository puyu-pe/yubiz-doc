# Consultar stock por almacén

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Consultar la cantidad actual de un producto en un almacén concreto antes de revisar
su historial o iniciar una operación.

## Acceso condicional

La disponibilidad de inventario y de cada almacén depende de la configuración y de
la sesión. Esta guía no confirma qué almacenes podrá consultar cada persona.

## Requisitos y datos

- Un producto identificable en el catálogo.
- El almacén que desea revisar, cuando corresponda.

## Punto de partida

Abra el detalle de inventario del producto si está disponible en su navegación. La
pantalla revisada muestra el producto y un selector de almacén.

## Pasos

1. Confirme que el producto mostrado corresponde al que desea revisar.
2. Seleccione un almacén en el selector; use la vista de todos solo para una revisión
   general cuando esa alternativa esté disponible.
3. Revise el valor de stock actual asociado al contexto seleccionado.
4. Si necesita explicar una diferencia, continúe con la ficha de movimientos antes
   de modificar cantidades.

## Campos y validaciones observados

La vista revisada presenta producto, almacén y stock actual. También muestra precio
de compra, precio de venta, unidades vendidas y márgenes como datos de consulta. La
precisión de los decimales, la disponibilidad de todos los almacenes y los valores
mostrados deben verificarse en runtime.

## Resultado revisado en fuente

Al cambiar de almacén, la interfaz vuelve a cargar el contexto del producto con el
almacén elegido y muestra la cantidad asociada. No se afirma que el valor sea una
existencia disponible para una decisión comercial sin comprobar el entorno.

## Advertencias y casos límite

No use este dato aislado para corregir una diferencia de inventario. El valor puede
depender del almacén elegido y de operaciones que requieran revisión posterior.

## Problemas frecuentes y condiciones de detención

- Producto equivocado: vuelva a identificarlo antes de interpretar la cantidad.
- Almacén no disponible: confirme el contexto habilitado, sin asumir un permiso.
- Diferencia que no puede explicar: deténgase y revise los movimientos.

## Verificaciones pendientes en runtime

- Nombres visibles, almacenes disponibles y reglas de acceso de la sesión.
- Actualización de la cantidad después de una operación real.
- Significado operativo de los valores complementarios de precio y margen.

## Enlaces relacionados

- [Revisar movimientos y kardex de un producto](revisar-movimientos-y-kardex.md)
- [Crear y editar productos del catálogo](../catalogo/gestionar-productos.md)
- [Inventario](index.md)
