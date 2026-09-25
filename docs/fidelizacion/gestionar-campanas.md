<a id="gestionar-campañas-de-descuento"></a>

# 7.8 Gestionar campañas de descuento

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar o revisar una campaña de descuento y los productos asociados cuando el
módulo esté habilitado, sin inferir una política comercial universal.

## Acceso condicional

La campaña depende de módulo, sesión, rol y configuración. No se confirma que una
campaña se aplique a todas las ventas, productos, clientes o establecimientos.

## Requisitos y datos

- Descripción de campaña.
- Fechas de inicio y fin.
- Monto mínimo y porcentaje de descuento.
- Productos visibles para asociar, cuando la campaña ya esté registrada.

## Punto de partida

Abra la lista de campañas o el formulario de creación cuando las opciones aparezcan.

## Pasos

1. Revise la lista y sus filtros antes de iniciar una nueva campaña.
2. Ingrese descripción, fechas, monto mínimo y porcentaje visibles.
3. Confirme los valores antes de registrar una sola vez.
4. Si el detalle aparece disponible, revise los productos asociados y no agregue o retire elementos sin autorización.
5. Vuelva a la lista y revise el estado mostrado, sin asumir que ya se aplicó a una venta.

## Campos y validaciones observados

El formulario observado muestra descripción, fechas, monto mínimo y porcentaje de
descuento. La validación de rangos, fechas y reglas de aplicación requiere
revisión antes de continuar.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz presenta controles para registrar una campaña con periodo, monto mínimo y
porcentaje. La asociación de productos se presenta después de que la campaña ya
cuenta con un registro; ninguna de estas pantallas confirma su aplicación a una
operación concreta.

## Advertencias y casos límite

No comunique un descuento ni modifique productos asociados sin validación responsable.
Una campaña visible o con estado mostrado no prueba que sea aplicable al contexto actual.

## Problemas frecuentes y condiciones de detención

- Fechas, monto o porcentaje dudosos: corrija antes de registrar.
- Producto no visible: no lo incorpore mediante una alternativa no observada.
- Estado o aplicación inciertos: detenga la operación comercial y solicite revisión.

## Enlaces relacionados

- [Crear y editar productos del catálogo](../catalogo/gestionar-productos.md)
- [Seleccionar productos y revisar condiciones](../ventas/seleccionar-productos-y-revisar-condiciones.md)
