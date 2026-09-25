<a id="registrar-un-ajuste-de-inventario"></a>

# 4.3 Registrar un ajuste de inventario

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar un ajuste de entrada o salida para un producto y almacén ya identificados,
solo después de confirmar que el procedimiento operativo autoriza la corrección.

## Acceso condicional

La acción aparece desde el historial del producto cuando hay un almacén específico
seleccionado. La configuración de seguimiento por lote o serie cambia los controles
disponibles. Esta guía no confirma permisos, aprobaciones ni políticas de auditoría.

## Requisitos y datos

- Producto y almacén específico seleccionados.
- Tipo de operación, cantidad y observación que permitan justificar el ajuste.
- Datos de lote o serie si el producto usa ese seguimiento.

## Punto de partida

Abra los movimientos del producto, seleccione un almacén concreto y use la acción de
ajuste solo cuando pueda explicar la diferencia que va a registrar.

## Pasos

1. Revise el stock actual mostrado y elija ingreso o salida según corresponda al
   hecho que está documentando.
2. Indique la cantidad y escriba una observación que permita reconocer el motivo.
3. Si el producto usa lotes o series, complete o seleccione los datos de seguimiento
   que la interfaz solicite.
4. Revise producto, almacén, tipo y cantidad antes de guardar.
5. Guarde y vuelva al historial para confirmar que la interfaz actualizó el contexto.
6. Deténgase si no puede justificar el ajuste; no use esta acción para eludir el
   seguimiento o el procedimiento de auditoría de su organización.

## Campos y validaciones observados

El formulario revisado contiene tipo de operación, stock actual de solo lectura,
cantidad y observación. La salida aparece deshabilitada cuando la cantidad actual no
es positiva. Para seguimiento por lote o serie, la interfaz adapta la captura; en
series distingue la entrada de la salida. La obligatoriedad, límites y mensajes
visibles deben verificarse en el entorno de trabajo.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz valida datos de seguimiento, registra el ajuste y su movimiento dentro de
una transacción, revierte ante un error y devuelve la cantidad del producto-almacén
para actualizar la vista. El efecto final en existencias y registros relacionados
debe comprobarse en el entorno.

## Advertencias y casos límite

Un ajuste de salida no se presenta como disponible en la condición observada de
stock no positivo. Lotes y series pueden exigir información adicional. No invente un
motivo ni continúe si el movimiento no es trazable.

## Problemas frecuentes y condiciones de detención

- No hay almacén específico: seleccione uno antes de intentar el ajuste.
- Salida no disponible: revise el stock y no fuerce una alternativa.
- Lote o serie incompletos: complete datos válidos o detenga el registro.
- Error al guardar: no reintente a ciegas; confirme si se creó un movimiento.

## Enlaces relacionados

- [Revisar movimientos y kardex de un producto](revisar-movimientos-y-kardex.md)
- [Gestionar lotes de productos](../catalogo/gestionar-lotes.md)
- [Gestionar series y trazabilidad de productos](../catalogo/gestionar-series.md)
- [Inventario](index.md)
