# Registrar pagos con uno o varios medios

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Distribuir el pago de una venta entre los medios que el formulario tenga
disponibles, revisando el total pagado, la deuda y el vuelto calculados.

## Acceso condicional

Esta guía aplica solo cuando el detalle de pago y los medios correspondientes están
habilitados para la venta, la sesión y la configuración del entorno.

## Requisitos y datos

- Venta con cliente, documento, serie, fecha, almacén e ítems revisados.
- Total mostrado por el formulario.
- Monto y, cuando aparezca, detalle u operación del medio de pago.

## Punto de partida

En el detalle de pago que se abre al registrar una venta.

## Pasos

1. Revise el total de la venta antes de agregar o modificar un medio de pago.
2. Agregue los medios que estén disponibles, como efectivo, billetera móvil o
   transferencia, solo si corresponden al cobro recibido.
3. Ingrese un monto positivo en cada medio y complete el detalle u operación cuando
   el formulario lo solicite.
4. Revise **Total pagado**, **Deuda** y **Vuelto** después de cada cambio.
5. Si queda deuda, complete una fecha de vencimiento posterior a la fecha de
   emisión antes de confirmar.
6. Confirme únicamente cuando la suma de los medios y los importes mostrados
   representen la operación real.

## Campos y validaciones observados

El formulario calcula total pagado, deuda y vuelto a partir de los montos
ingresados. Cada monto debe ser válido y mayor que cero. Solo permite un medio de

## Resultado revisado en fuente

El navegador incorpora los medios de pago junto con la venta y sus ítems en el
flujo de registro. Los datos de cada medio incluyen monto y, según el tipo, detalle

## Advertencias y casos límite

Esta es una operación financiera. No ajuste importes para forzar un resultado ni
interprete el vuelto o la deuda calculados como una conciliación externa. Los medios
disponibles y sus nombres pueden variar; no infiera políticas, permisos ni efectos
contables desde esta guía.

## Problemas frecuentes y condiciones de detención

- Monto vacío, no numérico o no positivo: corrija el importe antes de confirmar.
- Dos medios de efectivo: retire uno; el control observado admite solo uno.
- Suma mayor que el total o deuda con fecha inválida: detenga el registro y revise
  medios, montos y fechas.

## Verificaciones pendientes en runtime

- Medios, detalles y campos de operación habilitados.
- Cálculo de deuda, vuelto y fecha de vencimiento en el entorno.
- Registro financiero, comunicación, impresión y comportamiento desplegado.

## Enlaces relacionados

- [Registrar venta al contado](registrar-venta-al-contado.md)
- [Registrar una venta con saldo pendiente](registrar-venta-con-saldo-pendiente.md)
- [Registrar cobro posterior y consultar saldo](registrar-cobro-posterior-y-consultar-saldo.md)
