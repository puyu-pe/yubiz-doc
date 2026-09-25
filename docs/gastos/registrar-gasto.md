<a id="registrar-un-gasto"></a>

# 6.10 Registrar un gasto

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar un gasto con su proveedor, datos del documento, categoría y detalle de
ítems para revisarlo posteriormente en el listado.

## Acceso condicional

Los documentos, series, proveedores, categorías, medios de pago y presupuestos
mostrados dependen de la sesión y configuración. Seleccionar una asignación de
presupuesto es opcional en la validación revisada; no confirma una autorización ni
un efecto financiero o contable en el entorno de trabajo.

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
la interfaz compara la moneda y valida el monto disponible antes de guardar.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo guarda un gasto inicialmente pendiente con sus detalles y solicita abrir
una impresión tras una respuesta exitosa. Cuando se selecciona una asignación
compatible, la interfaz registra un consumo asociado. La persistencia, la impresión,
el estado final y sus consecuencias operativas pueden variar según la configuración disponible.

## Advertencias y casos límite

No use el total mostrado como sustituto de revisar los ítems. Si el presupuesto no
aparece, no asuma que debe crearse ni que el gasto quedará sin control. No infiera
moneda, tratamiento fiscal, caja, stock ni aprobación a partir de este formulario.

## Problemas frecuentes y condiciones de detención

- Faltan datos obligatorios: complete los campos marcados y los detalles antes de guardar.
- La asignación no coincide con la moneda o no tiene disponibilidad: detenga el registro y revise el contexto presupuestario.
- Total o ítems no son claros: corrija el detalle antes de confirmar.

## Enlaces relacionados

- [Consultar, aprobar y exportar gastos](gestionar-gastos.md)
- [Gestionar períodos, asignaciones y consumo de presupuesto](../compras/gestionar-presupuesto.md)
- [Gastos](index.md)
