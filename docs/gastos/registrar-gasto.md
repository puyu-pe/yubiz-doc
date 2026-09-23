# Registrar un gasto

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Registrar un gasto con su proveedor, datos del documento, categoría y detalle de
ítems para revisarlo posteriormente en el listado.

## Acceso condicional

Los documentos, series, proveedores, categorías, medios de pago y presupuestos
mostrados dependen de la sesión y configuración. Seleccionar una asignación de
presupuesto es opcional en la validación revisada; no confirma una autorización ni
un efecto financiero o contable en runtime.

## Requisitos y datos

- Proveedor, documento, serie, moneda, medio de pago, categoría y fecha.
- Al menos un ítem con cantidad, descripción, valor e importe revisados.
- Si corresponde, una asignación presupuestaria disponible en la misma moneda.

## Punto de partida

Abra la opción para registrar un gasto y espere a que carguen los selectores antes
de completar el formulario.

## Pasos

1. Seleccione el proveedor y complete documento, serie y moneda.
2. Indique el medio de pago, la categoría y la fecha del gasto.
3. Si aparece una asignación presupuestaria, elija una que corresponda a la moneda
   del gasto; si no corresponde, continúe sin seleccionarla.
4. Agregue los ítems y revise cantidad, descripción, valor unitario, tipo de IGV e
   importe de cada fila.
5. Revise subtotal, IGV y total calculados; agregue detalles para impresión u
   observación interna solo cuando sean necesarios.
6. Seleccione **Guardar**, confirme la acción y revise el resultado mostrado antes
   de continuar con una impresión o un nuevo registro.

## Campos y validaciones observados

La validación del navegador requiere proveedor, documento, serie, moneda, medio de
pago, categoría, fecha, descripción, tipo de IGV y total. Al elegir presupuesto,
la fuente revisada compara la moneda y valida el monto disponible antes de guardar.

## Resultado revisado en fuente

El flujo guarda un gasto inicialmente pendiente con sus detalles y solicita abrir
una impresión tras una respuesta exitosa. Cuando se selecciona una asignación
compatible, la fuente registra un consumo asociado. La persistencia, la impresión,
el estado final y sus consecuencias operativas requieren verificación en runtime.

## Advertencias y casos límite

No use el total mostrado como sustituto de revisar los ítems. Si el presupuesto no
aparece, no asuma que debe crearse ni que el gasto quedará sin control. No infiera
moneda, tratamiento fiscal, caja, stock ni aprobación a partir de este formulario.

## Problemas frecuentes y condiciones de detención

- Faltan datos obligatorios: complete los campos marcados y los detalles antes de guardar.
- La asignación no coincide con la moneda o no tiene disponibilidad: detenga el registro y revise el contexto presupuestario.
- Total o ítems no son claros: corrija el detalle antes de confirmar.

## Verificaciones pendientes en runtime

- Campos, documentos, series, proveedores, categorías y medios disponibles para la sesión.
- Resultado de guardar, impresión, numeración y mensajes de error.
- Efectos de presupuesto, caja, fiscalidad, contabilidad y autorización aplicables.

## Enlaces relacionados

- [Consultar, aprobar y exportar gastos](gestionar-gastos.md)
- [Gestionar períodos, asignaciones y consumo de presupuesto](../compras/gestionar-presupuesto.md)
- [Gastos](index.md)
