<a id="emitir-una-nota-de-crédito-o-canjear-un-documento"></a>

# 2.13 Emitir una nota de crédito o canjear un documento

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo
Reconocer los flujos condicionales observados para una nota de crédito o el canje de una nota de venta, sin afirmar efectos fiscales u operativos no verificados.

## Acceso condicional
Estas opciones dependen del tipo, estado y emisión del documento, además de la sesión y configuración disponible.

## Requisitos y datos
- Venta fuente identificada y revisada.
- Cliente, documento, serie y fecha disponibles para el flujo elegido.
- Detalle u observación, si el formulario los muestra.

## Punto de partida
En el detalle de una venta donde la opción correspondiente esté habilitada.

## Pasos
1. Confirme que la venta fuente, el cliente y los montos son correctos.
2. Elija solo la opción habilitada para el documento mostrado.
3. Para canje, seleccione documento y serie, y revise la fecha de emisión permitida por el formulario.
4. Complete los datos obligatorios que aparezcan y revise detalle u observación antes de confirmar.
5. Si el flujo informa un resultado, vuelva al detalle y verifique la relación mostrada antes de continuar.

## Campos y validaciones observados
El canje observado requiere venta fuente, cliente, documento, serie y fecha de emisión. La serie se carga según el documento elegido y el control de fecha aplica un rango suministrado por la configuración. Las opciones de nota de crédito se condicionan en el detalle de venta.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado
El flujo de canje envía los datos para registrar un nuevo documento y después intenta comunicarlo e imprimirlo. El flujo ofrece una opción para generar nota de crédito en determinados documentos. La validez, aceptación y efectos fiscales pueden variar según la configuración disponible.

## Advertencias y casos límite
No trate esta guía como asesoría tributaria ni como una política de corrección. Si no puede establecer la relación correcta entre documentos o el efecto esperado, deténgase y escale la consulta a la persona responsable.

## Problemas frecuentes y condiciones de detención
- Opción ausente o deshabilitada: no suponga que el flujo aplica.
- Serie o fecha no aceptada: revise el documento y no fuerce valores.
- Relación con la venta fuente incierta: detenga la operación antes de confirmar.

## Enlaces relacionados
- [Visualizar, imprimir y comunicar una venta](imprimir-y-comunicar-venta.md)
- [Anular una venta con cautela](anular-venta.md)
- [Elegir documento, serie, fecha y almacén de una venta](configurar-datos-del-documento.md)
