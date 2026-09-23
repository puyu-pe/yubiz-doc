# Crear y editar productos del catálogo

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Crear o actualizar la ficha maestra de un producto antes de utilizarlo en tareas
de venta, compra o inventario.

## Acceso condicional

La lista y el formulario de productos dependen del módulo y de la sesión. Los
campos disponibles pueden variar según la configuración del entorno.

## Requisitos y datos

- Nombre del producto, precio de venta, costo, seguimiento, stock mínimo y peso.
- Categoría, marca y medida para completar la ficha.
- Código interno o código de barras solo si se cuenta con datos autorizados.

## Punto de partida

En **Catálogo**, abra la lista de productos y elija la acción disponible para
agregar, o abra un registro existente para editarlo.

## Pasos

1. Escriba el nombre del producto y revise si ya existe uno equivalente.
2. Indique si puede comprarse o venderse, cuando las casillas estén disponibles.
3. Complete precio de venta, costo, seguimiento, stock mínimo y peso.
4. Abra los detalles adicionales para seleccionar marca, medida, modelo o
   presentación y categoría cuando correspondan.
5. Revise código interno y código de barras; déjelos sin completar solo si el
   flujo de su entorno permite generarlos.
6. Guarde y vuelva a abrir la ficha o la lista para comprobar que el producto
   esperado quedó identificado correctamente.

## Campos y validaciones observados

La ficha revisada incluye nombre, códigos, afectación tributaria, precio de venta,
costo, utilidad, observación, compra/venta, seguimiento, stock mínimo y peso. El
navegador exige nombre, precio mayor que cero, costo, seguimiento, stock mínimo y
peso no negativos. El guardado de fuente también exige categoría, marca y medida.
Al cambiar precio, costo o utilidad, el formulario recalcula campos relacionados.
Un código interno o de barras duplicado se rechaza; si queda vacío, la fuente
revisada intenta asignarlo automáticamente.

## Resultado revisado en fuente

El guardado válido crea o actualiza la ficha y conserva sus precios y proveedores
relacionados. En una creación, la fuente revisada prepara registros de producto
para los almacenes disponibles con cantidad inicial cero.

## Advertencias y casos límite

No use esta ficha para seleccionar un producto en una venta: esa operación es
distinta y se cubre en [seleccionar productos y revisar condiciones](../ventas/seleccionar-productos-y-revisar-condiciones.md).
El seguimiento puede quedar bloqueado al editar según el estado de stock; no
suponga que puede cambiarse después de crear el producto.

## Problemas frecuentes y condiciones de detención

- Producto, código interno o código de barras duplicado: revise el registro ya
  existente antes de crear otro.
- Falta categoría, marca o medida: complete los datos maestros necesarios.
- Precio no válido o costo, stock o peso negativos: corrija el valor antes de guardar.
- No puede confirmar el efecto del seguimiento: deténgase y valide el contexto
  operativo antes de modificarlo.

## Verificaciones pendientes en runtime

- Permisos, etiquetas y campos visibles para la sesión.
- Generación de códigos, mensajes de guardado y actualización de la lista.
- Efecto real de compra, venta y seguimiento en el entorno desplegado.

## Enlaces relacionados

- [Gestionar marcas, categorías, medidas y modelos](gestionar-detalles-de-producto.md)
- [Configurar precios de venta por tipo y establecimiento](configurar-precios-de-venta.md)
