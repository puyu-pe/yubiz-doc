# Gestionar marcas, categorías, medidas y modelos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Crear, revisar, editar o retirar de uso los datos maestros que describen un
producto: marcas, categorías, medidas y modelos o presentaciones.

## Acceso condicional

La disponibilidad del administrador de detalles depende del módulo y de la
sesión. No se asume que toda persona pueda crear o retirar datos maestros.

## Requisitos y datos

- Descripción clara para el detalle que se desea administrar.
- Código opcional, si se utiliza en la organización.
- Para categorías, datos adicionales de seguimiento; para modelos, unidad
  numérica, solo cuando esos campos sean pertinentes.

## Punto de partida

Desde el área de catálogo, abra la gestión de detalles y elija **Marca**,
**Medida**, **Modelo o presentación** o **Categoría**.

## Pasos

1. Cambie a la lista del tipo de detalle que necesita revisar.
2. Busque la descripción para comprobar que no exista un dato equivalente.
3. Use la acción disponible para agregar o editar e ingrese la descripción.
4. Complete código, datos adicionales de categoría o unidad de modelo solo si
   corresponden al dato que está creando.
5. Guarde y vuelva a la lista para confirmar que el detalle se pueda reconocer.
6. Si aparece una acción para retirar un detalle, deténgase y revise primero los
   productos que podrían depender de él.

## Campos y validaciones observados

Las cuatro fichas comparten código opcional y descripción. La categoría presenta
un campo adicional de datos de seguimiento; el modelo o presentación, una unidad
numérica opcional. En registros existentes, ciertos códigos de reserva aparecen
solo de lectura. La fuente revisada trata descripciones repetidas como un conflicto
al crear o modificar un detalle distinto.

## Resultado revisado en fuente

El detalle guardado queda disponible para seleccionarse en la ficha de producto.
La acción de retiro revisada no debe interpretarse como eliminación definitiva ni
como autorización para cambiar datos usados por productos existentes.

## Advertencias y casos límite

No cree variantes por diferencias de escritura sin revisar la lista. Una categoría,
marca o medida puede ser necesaria para guardar un producto; coordine el dato
maestro antes de iniciar la ficha del producto.

## Problemas frecuentes y condiciones de detención

- Descripción duplicada: deténgase y use o revise el detalle existente.
- Código bloqueado: no intente reemplazarlo por un valor alternativo sin validar
  su uso en el entorno.
- No está claro qué productos dependen del detalle: no lo retire de uso.
- Campo adicional sin significado operativo confirmado: déjelo pendiente de
  validación del entorno antes de inventar un valor.

## Verificaciones pendientes en runtime

- Acciones de alta, edición y retiro visibles para cada sesión.
- Reglas de duplicidad y comportamiento de los códigos de reserva.
- Uso de categorías, modelos y datos de seguimiento en productos desplegados.

## Enlaces relacionados

- [Crear y editar productos del catálogo](gestionar-productos.md)
- [Completar datos de compra e imágenes](completar-datos-de-compra-e-imagenes.md)
