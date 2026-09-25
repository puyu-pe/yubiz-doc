<a id="crear-y-consultar-guías-de-remisión"></a>

# 4.6 Crear y consultar guías de remisión

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Preparar y consultar una guía de remisión cuando esta opción esté habilitada para la
operación y el contexto de la sesión.

## Acceso condicional

Los documentos, series, motivos, almacenes y opciones de transporte disponibles
dependen de la configuración y de la sesión. Esta guía no confirma requisitos legales
ni el envío, aceptación o validez de un documento fuera del entorno.

## Requisitos y datos

- Documento, serie, almacén y fecha de traslado disponibles.
- Destinatario, motivo y puntos de partida y llegada identificables.
- Productos, cantidades y peso para cada detalle; lote o serie si se solicitan.

## Punto de partida

Abra la lista de guías si está disponible. Use sus filtros para localizar un registro
o inicie un registro nuevo solo cuando cuente con los datos de traslado necesarios.

## Pasos

1. Elija documento, serie, almacén y fecha de traslado.
2. Seleccione el motivo y complete el documento relacionado o su descripción solo
   cuando correspondan al caso.
3. Identifique al destinatario y complete ubicación y dirección de partida y llegada.
4. Seleccione la modalidad de transporte; complete los datos que la interfaz muestre
   para esa alternativa.
5. Agregue productos, cantidades, peso y el seguimiento por lote o serie aplicable.
6. Revise el detalle antes de registrar y consulte la lista para ubicar el resultado.

## Campos y validaciones observados

La interfaz incluye documento, serie, almacén, fecha, motivo, destinatario,
ubicaciones, direcciones, modalidad de transporte, productos, cantidad y peso. La
el formulario valida documento-serie, fecha, destinatario, ubicaciones y direcciones, además
de producto, descripción y peso por detalle. Los mensajes y condiciones exactas deben
verificarse en el entorno de trabajo.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo registra cabecera y detalles en una transacción y devuelve éxito o error. La
lista puede filtrar el conjunto disponible. No se afirma que el resultado produzca una
aceptación fiscal, transporte autorizado o cambio de stock sin evidencia del entorno.

## Advertencias y casos límite

No use una guía para sustituir una transferencia, ingreso o salida ya pendiente de
revisión. Si un documento ya fue impreso o enviado, la posibilidad de editarlo puede
estar restringida por condiciones del sistema.

## Problemas frecuentes y condiciones de detención

- Serie, destinatario o ubicaciones sin identificar: complete los datos antes de seguir.
- Detalle sin peso o producto: no registre una guía incompleta.
- Resultado incierto: consulte la lista antes de reenviar la operación.

## Enlaces relacionados

- [Registrar ingresos y salidas de almacén](registrar-ingresos-y-salidas.md)
- [Transferir productos entre almacenes](transferir-entre-almacenes.md)
- [Inventario](index.md)
