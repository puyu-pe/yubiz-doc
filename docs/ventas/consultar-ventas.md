# Buscar, filtrar y revisar el detalle de ventas

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Ubicar una venta en la lista, aplicar los filtros disponibles y revisar su detalle
antes de continuar con una acción operativa.

## Acceso condicional

La lista, sus columnas, filtros, exportaciones y acciones del detalle dependen de
la sesión, módulo y configuración disponible.

## Requisitos y datos

- Acceso a la lista de ventas.
- Un dato de búsqueda o filtro, cuando sea necesario.
- Identificación de la venta que se desea revisar.

## Punto de partida

En la pantalla de lista de ventas.

## Pasos

1. Revise las columnas visibles para identificar documento, serie, correlativo,
   fecha, cliente, establecimiento, total, pagado, deuda y estado.
2. Aplique los filtros que estén disponibles para documento, fecha, línea,
   cliente, establecimiento o vendedor.
3. Si necesita reiniciar la búsqueda, use **Limpiar filtros** o
   **Restablecer columnas** cuando esas opciones estén visibles.
4. Abra el detalle de la venta seleccionada para revisar datos del cliente, datos
   generales, ítems y pagos mostrados.
5. Use las opciones de exportación o detalle solo después de confirmar que la fila
   corresponde a la operación que busca.

## Campos y validaciones observados

La lista define columnas para documento, serie, correlativo, fechas, línea,
cliente, establecimiento, subtotal, impuesto, total, pagado, deuda, usuario,
personalizables que aparezcan en el entorno no sustituyen la revisión del detalle.

## Resultado revisado en fuente

El navegador carga una tabla de ventas, permite abrir el detalle de una fila y
ofrece controles para editar columnas, limpiar o restablecer filtros y generar
salidas. El contenido, los filtros efectivos y los resultados de exportación
requieren verificación en runtime.

## Advertencias y casos límite

Los montos pagado y deuda son datos financieros. No tome una fila, un estado o una
salida generada como comprobación definitiva sin contrastarla con el detalle y la
operación real. La disponibilidad de exportaciones y acciones del detalle puede
variar.

## Problemas frecuentes y condiciones de detención

- No encuentra la venta: revise filtros, columnas y datos de documento antes de
  concluir que no existe.
- El detalle no coincide con la fila esperada: detenga cualquier acción y revise
  documento, serie y correlativo.
- Una exportación o control no está disponible: no lo sustituya con una acción no
  observada; confirme la configuración de su entorno.

## Verificaciones pendientes en runtime

- Filtros, columnas configurables y datos que devuelve la lista.
- Acceso al detalle y disponibilidad de acciones por estado.
- Resultado de exportaciones y comportamiento desplegado.

## Enlaces relacionados

- [Elegir documento, serie, fecha y almacén de una venta](configurar-datos-del-documento.md)
- [Registrar cobro posterior y consultar saldo](registrar-cobro-posterior-y-consultar-saldo.md)
- [Crear y gestionar cotizaciones](gestionar-cotizaciones.md)
