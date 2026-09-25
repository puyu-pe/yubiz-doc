<a id="gestionar-establecimientos-y-almacenes"></a>

# 8.7 Gestionar establecimientos y almacenes

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Consultar establecimientos y almacenes, y editar únicamente controles habilitados y
autorizados para mantener su relación operativa.

## Acceso condicional

La gestión de establecimientos puede limitar alta, edición y eliminación según la
sesión. Almacenes también dependen de los controles disponibles; no se afirma que una
acción visible constituya autorización ni que sus efectos estén desplegados.

## Requisitos y datos

- Establecimiento o almacén identificable.
- Denominación y datos de ubicación solo cuando el formulario los muestre.
- Para un almacén: descripción, establecimiento y opciones operativas visibles.

## Punto de partida

Abra la lista de establecimientos o almacenes disponible para su sesión y localice el
registro que necesita revisar.

## Pasos

1. Revise el establecimiento asociado antes de crear o editar un almacén.
2. En un establecimiento, compruebe denominación, tipo, dirección y estado si aparecen.
3. En un almacén, revise descripción y establecimiento antes de cambiar opciones operativas.
4. Complete los campos requeridos que el formulario muestre y guarde una sola vez.
5. Regrese a la lista y confirme el valor visible antes de usar ese registro en otra operación.

## Campos y validaciones observados

La interfaz puede mostrar para establecimientos datos de identificación, ubicación, teléfono y
estado. Para almacenes exige descripción y establecimiento, y evita repetir la descripción;
puede presentar opciones operativas y una observación. Las reglas finales pueden variar según la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz relaciona cada almacén con un establecimiento y presenta controles para sus
opciones operativas. No confirma creación, eliminación, aprobación ni impacto sobre stock,
ventas, compras o usuarios existentes.

## Advertencias y casos límite

No cambie una relación de establecimiento o almacén para resolver una diferencia de stock.
Use el recorrido operativo correspondiente y detenga cambios que puedan afectar registros
existentes hasta contar con una indicación autorizada.

## Problemas frecuentes y condiciones de detención

- Descripción repetida o campo requerido vacío: corrija el dato antes de guardar.
- No aparece la acción esperada: no la fuerce; consulte a soporte autorizado.
- Resultado inesperado: no cree un registro alternativo para compensarlo.

## Enlaces relacionados

- [Transferir productos entre almacenes](../inventario/transferir-entre-almacenes.md)
- [Consultar stock por almacén](../inventario/consultar-stock-por-almacen.md)
- [Configuración](index.md)
