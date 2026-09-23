# Revisar ingresos, egresos y saldo de caja

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Consultar el resumen de movimientos de caja para un período y revisar ingresos,
egresos, saldo, detalle comercial y montos agrupados por método mostrado.

## Acceso condicional

Los establecimientos, personas usuarias, métodos, cifras y acciones disponibles
dependen de la sesión y configuración. El saldo mostrado es un cálculo del reporte
para el filtro seleccionado; no confirma conciliación, cierre, entrega ni una regla
contable de la organización.

## Requisitos y datos

- Establecimiento, persona usuaria y rango de fechas que se desea revisar.
- Un rango donde la fecha inicial no sea posterior a la final.
- Contexto operativo para interpretar ventas, compras, gastos y operaciones manuales.

## Punto de partida

Abra el reporte de ingresos y egresos. Revise los filtros antes de buscar y espere
que se actualicen los datos después de cambiar el establecimiento.

## Pasos

1. Seleccione un establecimiento o mantenga **Todos** cuando necesite una vista
   amplia disponible para su sesión.
2. Elija una persona usuaria si corresponde; el selector se actualiza al cambiar el
   establecimiento.
3. Indique las fechas **Desde** y **Hasta** y seleccione **Buscar**.
4. Revise ingresos, egresos y el saldo mostrado para ese filtro antes de tomar una
   decisión operativa.
5. Contraste el detalle comercial de ventas, compras y gastos, incluidos los valores
   válidos, anulaciones y total presentados.
6. Revise saldo inicial, inyecciones y ajustes manuales por separado; no los mezcle
   con una confirmación de dinero físico.
7. Si el resumen requiere entrega o conciliación, confirme primero los registros de
   origen y el procedimiento aplicable de su organización.

## Campos y validaciones observados

El formulario incluye establecimiento, usuario, fecha inicial y fecha final. La
fuente revisada rechaza fechas inválidas y una fecha inicial posterior a la final.
El tablero muestra totales de ingreso y egreso, saldo, detalle comercial, operaciones
manuales y montos agrupados por los métodos disponibles en la interfaz.

## Resultado revisado en fuente

El reporte calcula el saldo como ingresos menos egresos para el filtro recibido y
presenta totales por tipo de movimiento y método. Una pantalla sin datos limpia los
valores mostrados. La exactitud de registros, alcance del filtro y significado de
cada total deben verificarse en runtime.

## Advertencias y casos límite

No interprete un saldo positivo como efectivo disponible ni un resumen por método
como conciliación bancaria. Un movimiento anulado puede mostrarse de forma separada.
Evite comparar períodos o establecimientos distintos sin revisar los filtros activos.

## Problemas frecuentes y condiciones de detención

- Fechas inválidas o invertidas: corrija el rango antes de buscar.
- Datos inesperados: detenga la revisión y confirme establecimiento, usuario y período.
- Saldo sin respaldo operativo: no entregue ni ajuste caja hasta revisar los movimientos de origen.

## Verificaciones pendientes en runtime

- Establecimientos, usuarios, métodos y filtros disponibles para la sesión.
- Cálculo, actualización y formato de los totales mostrados.
- Conciliación, entrega, autorización y efectos contables aplicables a la organización.

## Enlaces relacionados

- [Registrar el saldo inicial de caja](registrar-saldo-inicial.md)
- [Registrar una inyección o ajuste manual de caja](registrar-operacion-manual.md)
- [Caja y reportes](index.md)
