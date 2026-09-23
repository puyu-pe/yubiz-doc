# Registrar proveedores, costos e imágenes de un producto

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Completar en un producto los proveedores, costos e imágenes disponibles después
de que la ficha maestra se haya creado o al editar una ficha existente.

## Acceso condicional

Las secciones de compras y galería pertenecen a la ficha de producto. La galería
está deshabilitada al crear un producto y se habilita para un producto existente.

## Requisitos y datos

- Producto creado o identificado para edición.
- Proveedor existente y datos de compra autorizados.
- Archivo de imagen en formato admitido, solo si corresponde a la operación.

## Punto de partida

Abra el producto existente y seleccione **Compras** o **Galería** según la tarea.

## Pasos

1. En **Compras**, elija el proveedor disponible y complete el código de producto,
   precio y cantidad mínima cuando la tabla lo solicite.
2. Revise el costo principal del producto junto con los datos de cada proveedor.
3. Guarde la ficha completa para conservar las relaciones de compra.
4. Para una imagen, abra **Galería** en un producto existente y elija agregar.
5. Seleccione un archivo admitido, confirme su vista previa si aparece y guarde.
6. Si necesita cambiar la imagen principal o retirar una imagen, revise primero
   cuál se muestra en la ficha antes de confirmar la acción.

## Campos y validaciones observados

La tabla de compras revisada incluye proveedor, código de producto, precio y
cantidad mínima. El costo principal es obligatorio y no puede ser negativo. La
galería acepta archivos con extensiones JPG, JPEG o PNG; su control se habilita
solo para productos con identificador existente. La fuente revisada guarda una
imagen y permite actualizar, marcar una principal o retirarla; no confirma límites
de tamaño, resolución ni el resultado visual desplegado.

## Resultado revisado en fuente

Los proveedores y precios de compra se guardan junto con el producto. Las imágenes
guardadas se asocian al producto y una puede marcarse como principal. Retirar una
imagen elimina su relación en el flujo revisado; confirme el impacto antes de usar
esa acción.

## Advertencias y casos límite

No incluya cuentas, datos personales de proveedores ni imágenes sin autorización.
No afirme que un costo o imagen se propaga automáticamente a otras operaciones.
Si la galería no está disponible, cree o identifique primero el producto y vuelva
a comprobar la ficha.

## Problemas frecuentes y condiciones de detención

- Proveedor no disponible: confirme que el proveedor exista antes de repetir el flujo.
- Costo o cantidad mínima inválidos: corrija el valor antes de guardar.
- Archivo con formato no admitido: no intente cambiar su extensión; use un archivo
  apto y autorizado.
- No puede determinar cuál imagen es principal o qué se retirará: deténgase.

## Verificaciones pendientes en runtime

- Proveedores disponibles y campos de compra por sesión.
- Límites y mensajes de carga de imágenes.
- Visibilidad de la imagen principal y efecto de retirar una imagen desplegada.

## Enlaces relacionados

- [Gestionar proveedores y sus cuentas bancarias](../contactos/gestionar-proveedores.md)
- [Crear y editar productos del catálogo](gestionar-productos.md)
