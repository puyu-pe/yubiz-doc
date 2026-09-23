# Gestionar documentos, series y correlativos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Revisar y, cuando la sesión lo permita, mantener la relación entre documento, serie,
establecimiento y correlativo sin asumir una política fiscal ni de numeración.

## Acceso condicional

Las acciones dependen de la sesión. La disponibilidad de series para una operación se
filtra por documento y establecimiento; no se infiere que crear, editar o eliminar una
serie esté autorizado ni que un número pueda reiniciarse.

## Requisitos y datos

- Documento y establecimiento que se necesita revisar.
- Serie, fecha y observación solo si el formulario los muestra.
- Confirmación autorizada antes de modificar una serie o correlativo.

## Punto de partida

Abra la lista de documentos y series disponible para su sesión, o la selección de
documento dentro de una operación que la requiera.

## Pasos

1. Identifique el documento y el establecimiento asociados antes de abrir una serie.
2. Revise la serie, el correlativo visible, la fecha y la visibilidad cuando aparezcan.
3. Para una operación, seleccione primero el documento y espere que carguen sus series.
4. Elija únicamente una serie disponible para el establecimiento mostrado.
5. Si una edición está habilitada, revise todos los datos visibles y guarde una sola vez.
6. Vuelva a la lista o al formulario y compruebe el resultado antes de continuar.

## Campos y validaciones observados

El formulario fuente exige documento, serie, establecimiento y fecha. La lista incluye
correlativo, observación, visibilidad y un dato de terminal cuando corresponda. Si no hay
series para el documento y establecimiento, el navegador informa esa ausencia.

## Resultado revisado en fuente

La fuente carga las series asociadas al documento seleccionado y al establecimiento de
la sesión. No garantiza formato fiscal, consecutividad, reinicio, aprobación ni emisión
de comprobantes; esos efectos deben verificarse en runtime.

## Advertencias y casos límite

No cambie un correlativo para corregir una operación anterior ni use esta ficha para
reiniciar numeración. Ante una numeración inesperada, deténgase y contacte a soporte
autorizado antes de guardar.

## Problemas frecuentes y condiciones de detención

- No hay series disponibles: confirme documento y establecimiento; no invente una serie.
- Falta un campo requerido: complete solo el dato autorizado antes de guardar.
- Correlativo inesperado o resultado incierto: no repita ni reinicie la operación.

## Verificaciones pendientes en runtime

- Permisos y acciones disponibles por sesión.
- Formatos, reglas de correlativo, fechas y visibilidad.
- Efectos sobre emisión, documentos existentes y procesos externos.

## Enlaces relacionados

- [Elegir documento, serie, fecha y almacén de una venta](../ventas/configurar-datos-del-documento.md)
- [Gestionar establecimientos y almacenes](gestionar-establecimientos-y-almacenes.md)
- [Configuración](index.md)
