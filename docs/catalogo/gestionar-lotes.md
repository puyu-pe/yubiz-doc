# Gestionar lotes de productos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Registrar, consultar o actualizar lotes asociados a un producto cuando el seguimiento
por lote esté habilitado en el entorno.

## Acceso condicional

Esta capacidad depende de la configuración de seguimiento, del módulo y de la sesión.
El nombre mostrado para lote puede variar según la configuración; no supone que todos
los productos ni entornos usen este control.

## Requisitos y datos

- Un producto disponible para asociar al lote.
- Descripción del lote, precio y fecha de vencimiento cuando correspondan.
- Detalle que permita reconocer el registro sin incluir datos sensibles.

## Punto de partida

Abra la lista de lotes solo si está disponible en la navegación de su sesión. Revise
la lista antes de agregar o editar un registro.

## Pasos

1. Use la acción disponible para agregar un lote o abra el registro que desea editar.
2. Al crear, seleccione el producto y complete la descripción del lote.
3. Registre precio, fecha de vencimiento y detalle únicamente cuando correspondan al
   producto y al procedimiento de su organización.
4. Guarde y vuelva a la lista para identificar el lote por producto y descripción.
5. Al editar, revise la distribución mostrada por almacén antes de cambiar datos del
   lote; deténgase si no puede explicar el efecto operativo.

## Campos y validaciones observados

El formulario revisado muestra producto, lote, precio, fecha de vencimiento y detalle.
La edición muestra además stock por almacén y un total. La fuente rechaza una
descripción duplicada para el mismo producto durante la actualización. La obligatoriedad
exacta, los rangos y los mensajes visibles requieren verificación en runtime.

## Resultado revisado en fuente

La fuente revisada crea o actualiza el registro de lote asociado al producto y permite
consultar su información junto con cantidades por almacén. No se afirma un efecto de
stock ni una política de vencimientos sin evidencia del entorno.

## Advertencias y casos límite

No cambie un lote para corregir una operación de inventario sin seguir el procedimiento
autorizado. El alias, las columnas y las acciones visibles pueden cambiar por
configuración. Un lote no sustituye la trazabilidad individual por series.

## Problemas frecuentes y condiciones de detención

- Lote duplicado para el producto: revise el listado antes de crear otro.
- Producto o lote no identificable: deténgase y valide los datos maestros.
- No puede confirmar el impacto sobre existencias: no continúe con la modificación.
- Opción ausente: confirme la habilitación del módulo y el seguimiento aplicable.

## Verificaciones pendientes en runtime

- Disponibilidad, alias, permisos y campos obligatorios de la sesión.
- Mensajes de guardado, filtros y actualización de cantidades mostradas.
- Efecto real de crear, editar o usar un lote en operaciones posteriores.

## Enlaces relacionados

- [Crear y editar productos del catálogo](gestionar-productos.md)
- [Gestionar series y trazabilidad de productos](gestionar-series.md)
- [Catálogo](index.md)
