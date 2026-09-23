# Registrar una inyección o ajuste manual de caja

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Registrar una inyección de caja o un ajuste manual cuando esas opciones estén
disponibles, y comprobar después cómo se muestra en el reporte filtrado.

## Acceso condicional

Estas acciones son condicionales y dependen de la sesión y configuración. Una
inyección se presenta como ingreso; un ajuste permite elegir ingreso o egreso. Esta
mecánica no reemplaza una autorización, conciliación, conversión de moneda ni el
procedimiento financiero de la organización.

## Requisitos y datos

- Tipo de operación: inyección o ajuste.
- Importe numérico mayor que cero, método y fecha y hora válidos.
- Para un ajuste, dirección de ingreso o egreso.
- Observación opcional que explique el contexto sin registrar información sensible.

## Punto de partida

Desde el reporte de caja, seleccione **Registrar inyección** o **Registrar ajuste**
y revise el título y los campos que se muestran antes de guardar.

## Pasos

1. Confirme el establecimiento, usuario y período del reporte que está revisando.
2. Para una inyección, abra su formulario y revise que se presente como ingreso.
3. Para un ajuste, seleccione primero la dirección de ingreso o egreso.
4. Ingrese importe, método y fecha y hora; agregue una observación si es necesaria
   para la trazabilidad operativa.
5. Revise que el importe sea positivo y que el tipo elegido corresponda al hecho que
   está documentando.
6. Seleccione **Guardar**, espere el resultado y vuelva a consultar el reporte.
7. Revise la fila de operación manual y el resumen antes de iniciar otro registro.

## Campos y validaciones observados

El formulario solicita tipo, importe, método, fecha y hora; la observación es
opcional. Para ajustes, la dirección es obligatoria y admite ingreso o egreso. La
validación revisada requiere tipo permitido, importe numérico mayor que cero, método
y fecha válida; el servidor acepta valores de moneda definidos por su validación,
pero la interfaz revisada no ofrece una conversión de moneda.

## Resultado revisado en fuente

La operación se registra como movimiento manual y, después de una respuesta exitosa,
el reporte se vuelve a cargar. La inyección usa dirección de ingreso; el ajuste usa
la dirección seleccionada. El resultado no confirma saldo físico, autorización,
conciliación, conversión ni consecuencias financieras o contables en runtime.

## Advertencias y casos límite

No use un ajuste para ocultar un descuadre sin revisar su origen. Antes de registrar
un egreso, confirme importe, dirección y evidencia operativa. Si el resultado no es
claro, no repita el envío: vuelva al reporte y valide los movimientos mostrados.

## Problemas frecuentes y condiciones de detención

- Tipo o dirección incorrectos: detenga el flujo y corrija antes de guardar.
- Importe no positivo o fecha inválida: complete datos válidos antes de continuar.
- Reporte no actualizado o saldo inesperado: no registre otra operación hasta revisar filtros y registros de origen.

## Verificaciones pendientes en runtime

- Tipos, métodos, moneda aceptada y controles disponibles para cada sesión.
- Resultado de guardar, actualización del reporte y mensajes de error.
- Autorización, conciliación y efectos financieros, contables o de entrega aplicables.

## Enlaces relacionados

- [Revisar ingresos, egresos y saldo de caja](revisar-ingresos-y-egresos.md)
- [Registrar el saldo inicial de caja](registrar-saldo-inicial.md)
- [Caja y reportes](index.md)
