<a id="emitir-una-nota-de-crédito-o-canjear-un-documento"></a>

# 2.8 Emitir una nota de crédito

<a id="213-emitir-una-nota-de-credito-o-canjear-un-documento"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Emita una nota de crédito desde una venta identificada y compruebe el documento resultante antes de continuar.

## Antes de empezar
Estas opciones dependen del tipo, estado y emisión del documento, además de la sesión y configuración disponible.

### Datos necesarios
- Venta fuente identificada y revisada.
- Cliente, documento, serie y fecha disponibles para el flujo elegido.
- Detalle u observación, si el formulario los muestra.

## Cómo acceder
En el detalle de una venta donde la opción correspondiente esté habilitada.

## Cómo acceder

1. En la barra lateral, abra **Ventas** y seleccione **Ventas**.
2. Haga doble clic en la fila de la venta para abrir su detalle.
3. En el menú de acciones del detalle, seleccione **Nota de crédito** solo si la opción está habilitada. Se abrirá **Nota de crédito / Agregar**.

## Pasos
1. Confirme que la venta fuente, el cliente, los ítems y los montos son correctos.
2. Elija la opción de nota de crédito disponible para el documento mostrado.
3. Complete los datos obligatorios y revise el detalle u observación antes de confirmar.
4. **Antes de confirmar,** deténgase si no puede identificar con claridad el documento fuente y el motivo de la corrección.
5. Cuando el flujo informe un resultado, vuelva al detalle y verifique el documento generado antes de continuar.

### Datos que debe revisar
Las opciones de nota de crédito se condicionan en el detalle de venta. Los datos solicitados pueden depender del documento y de la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado
El flujo ofrece una opción para generar una nota de crédito en determinados documentos. Compruebe el documento resultante y su relación con la venta fuente antes de usar cualquier opción posterior.

## Situaciones frecuentes
No trate esta guía como asesoría tributaria ni como una política de corrección. Si no puede establecer la relación correcta entre documentos o el efecto esperado, deténgase y escale la consulta a la persona responsable.

### Si necesita detenerse
- Opción ausente o deshabilitada: no suponga que el flujo aplica.
- Datos no aceptados: revise el documento fuente y no fuerce valores.
- Relación con la venta fuente incierta: detenga la operación antes de confirmar.

## Continuar con
- [Consultar una venta, imprimirla o comunicarla](consultar-ventas.md)
- [Canjear un documento de venta](canjear-documento-de-venta.md)
