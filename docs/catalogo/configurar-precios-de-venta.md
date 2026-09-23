# Configurar precios de venta por tipo y establecimiento

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Revisar y configurar precios de venta asociados a un producto por tipo y, cuando
la configuración lo habilite, por establecimiento.

## Acceso condicional

La tabla de precios está dentro de la ficha de producto. La visibilidad por
establecimiento y los tipos de precio dependen de la configuración del entorno.

## Requisitos y datos

- Producto existente o ficha de producto en creación.
- Tipo de precio y establecimiento, cuando el formulario los muestre.
- Precio mayor que cero y comisión solo si corresponde al tipo configurado.

## Punto de partida

Abra el producto y seleccione la pestaña **Ventas** cuando esté disponible.

## Pasos

1. Revise el precio de venta general de la ficha antes de agregar variantes.
2. Compruebe si la tabla muestra establecimientos o si el entorno trabaja con un
   precio general.
3. Seleccione el tipo de precio disponible y complete el importe asociado.
4. Si aparece una comisión, revise su valor junto con el precio antes de guardar.
5. Guarde la ficha completa y vuelva a abrirla para comprobar los precios listados.
6. Para retirar una variante, use la acción disponible solo después de confirmar
   que no se necesita para operaciones en curso.

## Campos y validaciones observados

La tabla revisada muestra tipo, establecimiento, precio y porcentaje de comisión.
El formulario exige un precio de venta mayor que cero; cada precio de la tabla
también es obligatorio y debe ser mayor que cero. Cuando la configuración no
habilita precios por establecimiento, el precio general se sincroniza desde el
campo principal. La fuente no permite convertir estas condiciones en una regla
universal para todos los entornos.

## Resultado revisado en fuente

Al guardar, la ficha conserva los precios asociados al producto. En edición, los
precios configurados se vuelven a cargar con el producto y se actualizan junto con
sus demás datos.

## Advertencias y casos límite

No publique ni suponga una moneda, lista comercial, aprobación o política de
descuentos. Un establecimiento o tipo que no aparezca en la tabla debe tratarse
como una condición de configuración, no como un error que se pueda resolver con
otro flujo.

## Problemas frecuentes y condiciones de detención

- Precio vacío, cero o negativo: corríjalo antes de guardar.
- No aparece el tipo o establecimiento esperado: deténgase y confirme la
  configuración aplicable.
- Variantes duplicadas o no reconocibles: revise la tabla antes de agregar otra.
- No puede evaluar el impacto de retirar un precio: no continúe.

## Verificaciones pendientes en runtime

- Tipos, establecimientos y comisiones visibles para cada tenant.
- Reglas de sincronización entre precio general y precios por establecimiento.
- Uso de los precios configurados en ventas desplegadas.

## Enlaces relacionados

- [Crear y editar productos del catálogo](gestionar-productos.md)
- [Seleccionar productos y revisar condiciones](../ventas/seleccionar-productos-y-revisar-condiciones.md)
