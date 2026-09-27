<a id="anular-una-venta-con-cautela"></a>

# 2.7 Anular una venta

<a id="212-anular-una-venta-con-cautela"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Anule una venta identificada y compruebe el estado resultante antes de iniciar otra corrección.
Revisar el mecanismo observado para solicitar la anulación de una venta sin ejecutar una operación real desde esta guía.

## Antes de empezar
La anulación se muestra solo para determinados documentos y puede depender del estado, la emisión, una condición de acceso y la configuración disponible.

### Datos necesarios
- Venta correcta abierta en detalle.
- Estado, documento y fecha revisados.
- Motivo y decisión sobre devolución de productos, cuando el formulario los solicite.

## Cómo acceder
En el menú de acciones del detalle de una venta elegible.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Ventas**.
3. Seleccione la venta para abrir su detalle.

## Pasos
1. Confirme documento, serie, correlativo, cliente, ítems y montos antes de abrir la acción.
2. Revise si **Anular** está habilitado; si no lo está, no intente continuar por otra vía.
3. En el formulario observado, complete el motivo y revise la opción sobre devolución de productos.
4. Deténgase si no puede validar el impacto operativo con la persona responsable.
5. Solo una persona autorizada en su operación debe confirmar la solicitud.

### Datos que debe revisar
El formulario observado incluye motivo y una opción para devolución de productos. Para documentos distintos de nota de venta, el navegador compara la fecha con un límite suministrado por la configuración; no se documenta aquí una ventana universal.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado
La interfaz envía la solicitud de anulación con esos datos y vuelve a cargar el detalle de la venta. La anulación efectiva y sus efectos sobre productos, caja, documentos o comunicaciones pueden variar según la configuración disponible.

## Situaciones frecuentes
Es una operación destructiva. No infiera una política de aprobación, una regla tributaria ni un efecto de stock o caja desde la mecánica observada. Si existe duda sobre el impacto, detenga el proceso y escale la decisión.

### Si necesita detenerse
- Acción no disponible o deshabilitada: revise el estado y escale la consulta.
- Motivo o decisión de devolución incompletos: no confirme.
- Fecha fuera del rango mostrado: no suponga una excepción; solicite orientación operativa.

## Continuar con
- [Consultar una venta, imprimirla o comunicarla](consultar-ventas.md)
