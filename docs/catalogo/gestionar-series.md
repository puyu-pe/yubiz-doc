# Gestionar series y trazabilidad de productos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Consultar y actualizar la identificación individual de una serie vinculada a un
producto y a su lote, cuando el seguimiento por series esté habilitado.

## Acceso condicional

Esta capacidad es condicional: depende del módulo, del tipo de producto y de la
sesión. Los controles complementarios para contenedores solo se observan en ciertos
casos; no se debe asumir que aparecen para todas las series.

## Requisitos y datos

- Una serie existente y el producto/lote al que está vinculada.
- Descripción de serie y detalle actualizado, cuando sea necesario.
- Datos de contenido, estado o propietario únicamente si esos controles aparecen.

## Punto de partida

Abra la lista de series disponible en su sesión, ubique la serie por producto, lote o
descripción y seleccione la acción de edición disponible.

## Pasos

1. Revise producto, lote y ubicación antes de editar la serie.
2. Actualice la descripción y el detalle solo con información verificable.
3. Si aparecen controles de contenedor, revise contenido, estado de llenado, estado
   operativo y tipo de propietario antes de guardar.
4. Complete atributos adicionales únicamente si el formulario los presenta.
5. Guarde y confirme que la serie sigue identificable en la lista.
6. Si necesita cambiar el producto asociado, deténgase y confirme el contexto de
   almacén y el procedimiento autorizado antes de continuar.

## Campos y validaciones observados

La edición revisada muestra producto, lote de solo lectura, serie, ubicación de solo
lectura y detalle. Para ciertos contenedores aparecen contenido, llenado, condición
operativa, tipo de propietario y atributos. La fuente rechaza una descripción de serie
duplicada. Las reglas de visibilidad, valores admitidos y mensajes requieren runtime.

## Resultado revisado en fuente

La fuente actualiza la serie y conserva su vínculo con lote, producto y ubicación. Un
cambio de producto tiene condiciones adicionales en la fuente; esta ficha no afirma
que esté disponible ni describe sus efectos sobre existencias en un entorno desplegado.

## Advertencias y casos límite

No use esta ficha para asignar series en entradas, salidas o cargas: son flujos
operativos distintos. La ubicación, el propietario y los campos de contenedor pueden
limitar la modificación. No infiera trazabilidad completa sin validarla en runtime.

## Problemas frecuentes y condiciones de detención

- Serie o lote no encontrado: revise la identificación antes de editar.
- Descripción repetida: use un identificador distinto o revise el registro existente.
- La serie no está en el contexto esperado: no intente forzar un cambio de producto.
- Controles de contenedor ausentes: confirme si aplican al tipo de producto.

## Verificaciones pendientes en runtime

- Habilitación, permisos, etiquetas y filtros de la lista de series.
- Campos adicionales por tipo de producto y sus validaciones visibles.
- Consecuencias reales de cambios de ubicación, propietario o producto asociado.

## Enlaces relacionados

- [Gestionar lotes de productos](gestionar-lotes.md)
- [Crear y editar productos del catálogo](gestionar-productos.md)
- [Catálogo](index.md)
