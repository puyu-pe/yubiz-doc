# Elegir documento, serie, fecha y almacén de una venta

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Completar los datos del documento y del contexto de una venta antes de registrar
ítems y pagos.

## Acceso condicional

Los documentos, series, almacenes, líneas y vendedores disponibles dependen de la
sesión, módulo y configuración del entorno.

## Requisitos y datos

- Cliente seleccionado para la venta.
- Documento, serie, fecha de emisión y almacén disponibles en el formulario.
- Línea o vendedor, si el formulario los muestra y la operación los requiere.

## Punto de partida

En el formulario **Venta / Agregar**, antes de confirmar la operación.

## Pasos

1. Seleccione el documento disponible para la operación.
2. Espere la carga de las series asociadas y seleccione la serie correspondiente.
3. Ingrese o revise la fecha de emisión.
4. Seleccione el almacén desde el cual se realizará la venta.
5. Si aparecen, revise la línea y el vendedor; deje esos campos según el contexto
   de la operación.
6. Cambie de documento solo antes de continuar con los ítems: el formulario vuelve
   a cargar sus series y recalcula condiciones de los ítems.
7. Continúe con los productos y revise los datos otra vez antes de seleccionar
   **Registrar**.

## Campos y validaciones observados

El navegador exige cliente, documento, serie, fecha y almacén. La serie se valida
como requerida y con un máximo de cuatro caracteres. La fecha se valida como
requerida y contra el rango disponible del documento seleccionado; el formulario
muestra como máximo la fecha actual en el control observado.

## Resultado revisado en fuente

El formulario carga documentos, series, almacenes, líneas y vendedores según los

## Advertencias y casos límite

No use una serie, fecha o almacén como equivalentes de una autorización financiera
o fiscal. Si cambia el documento después de cargar ítems, revise precios,

## Problemas frecuentes y condiciones de detención

- No hay serie disponible: detenga el registro y confirme el documento elegido en
  el entorno.
- Fecha rechazada por el formulario: corrija la fecha o confirme el rango que
  admite el documento seleccionado.
- Almacén o vendedor no visible: no asuma un permiso o una configuración; use solo
  las opciones disponibles.

## Verificaciones pendientes en runtime

- Documentos, series, almacenes, líneas y vendedores habilitados.
- Rango de fechas aplicado por cada documento.
- Validaciones, efectos de cambio de documento y comportamiento desplegado.

## Enlaces relacionados

- [Seleccionar cliente](seleccionar-cliente.md)
- [Seleccionar productos y revisar condiciones](seleccionar-productos-y-revisar-condiciones.md)
- [Registrar pagos con uno o varios medios](registrar-multiples-medios-de-pago.md)
