<a id="registrar-pagos-de-compras-y-consultar-saldos"></a>

# 6.7 Registrar pagos de compras y consultar saldos

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar un pago para una orden de compra con deuda y revisar el total, monto pagado,
deuda e historial disponibles en el detalle.

## Acceso condicional

Las formas de pago, detalle, número de operación, asignación presupuestal y acciones
de constancia dependen de configuración y sesión. Esta ficha no confirma disponibilidad
de caja, fondos, autorización ni contabilización en el entorno desplegado.

## Requisitos y datos

- Orden de compra existente, proveedor y saldo revisados.
- Fecha, método de pago, monto mayor que cero y observación si corresponde.
- Detalle y número de operación para los métodos que la interfaz los habilite.
- Documento del proveedor relacionado si se necesita imprimir o notificar constancia.

## Punto de partida

Abra el detalle de una orden y elija Registrar pago. Revise primero total, pagado y
deuda; el formulario solo presenta una nueva línea mientras exista deuda.

## Pasos

1. Confirme el documento, proveedor, total, pagado y deuda antes de ingresar un monto.
2. Indique fecha y seleccione el método de pago disponible.
3. Complete detalle y número de operación cuando el método los habilite.
4. Ingrese un monto mayor que cero y confirme que el total pagado no exceda el total
   mostrado.
5. Añada una observación si ayuda a identificar el pago y registre la línea.
6. Revise el historial, el nuevo pagado y la deuda resultante antes de continuar.

## Campos y validaciones observados

El formulario muestra fecha, método, detalle del método, número de operación, monto y
observación. La interfaz valida monto positivo y que la suma no supere el total. El
historial muestra fecha, monto, método, número de operación, detalle, observación y
fecha de registro. La interfaz exige tipo de pago e identifica la compra antes de guardar.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo registra el pago y actualiza los campos de pagado y deuda de la compra dentro
de una transacción. El saldo es un dato de la orden, no un comprobante del proveedor.
No se afirma que registrar el pago produzca una salida de caja, validación bancaria,
registro presupuestal o asiento contable en un entorno desplegado.

## Advertencias y casos límite

No registre un pago si total, pagado o deuda no coinciden con el documento revisado.
Una constancia requiere que el pago esté relacionado con un documento del proveedor;
no envíe ni imprima una constancia sin verificar esa relación y el correo disponible.

## Problemas frecuentes y condiciones de detención

- No hay deuda: no agregue una nueva línea de pago.
- Monto cero, negativo o superior al saldo permitido: corrija el importe antes de guardar.
- Falta método de pago o la compra no se identifica: detenga el registro.
- Falta documento relacionado para la constancia: relaciónelo antes de imprimir o enviar.

## Enlaces relacionados

- [Registrar y relacionar documentos de compra](gestionar-documentos.md)
- [Consultar, exportar y notificar órdenes de compra](gestionar-ordenes.md)
- [Compras](index.md)
