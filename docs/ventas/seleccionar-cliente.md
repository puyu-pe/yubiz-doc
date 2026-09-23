# Seleccionar cliente

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Asociar un cliente a la venta antes de registrar productos y pagos.

## Acceso condicional

El formulario de venta y sus resultados de búsqueda están sujetos a la sesión,
rol y datos disponibles en el entorno.

## Requisitos y datos

- Contexto de establecimiento confirmado.
- Documento o dato de identificación del cliente.

## Punto de partida

En la pantalla de registro de venta, en la sección de datos del cliente, cuando
esté disponible para su cuenta.

## Pasos

1. Ubique **Datos cliente** y el control **DNI / RUC**.
2. Busque el cliente por su documento, nombre o referencia disponible y seleccione
   un único resultado.
3. Revise el documento y la descripción mostrados antes de continuar.
4. Si el control ofrece crear o completar un dato, confirme primero que ese flujo
   corresponde a la operación de su entorno.

## Campos y validaciones observados

El control admite una selección. Para un documento nuevo, la fuente revisada
solicita ocho u once dígitos numéricos; si el cliente seleccionado no tiene
documento o su dirección supera el límite tratado por el formulario, se solicita
corrección antes de continuar.

## Resultado revisado en fuente

La selección entrega el identificador y los datos del cliente al formulario de
venta; el formulario requiere un cliente antes de abrir el detalle de pago.

## Advertencias y casos límite

No continúe con un documento o dirección que el propio formulario marque para
corrección. La búsqueda externa y la creación de clientes no se consideran
confirmadas para todos los entornos.

## Problemas frecuentes y condiciones de detención

- Sin resultados: confirme el dato de identificación antes de intentar otro flujo.
- Documento incompleto o inválido: corríjalo antes de seleccionar al cliente.
- Datos que no corresponden a la operación: retire la selección y valide con el
  equipo responsable.

## Verificaciones pendientes en runtime

- Etiquetas, resultados y búsqueda externa disponibles.
- Reglas aplicadas a documento, dirección y creación de clientes.
- Permisos y comportamiento desplegado por cuenta.

## Enlaces relacionados

- [Elegir establecimiento](elegir-establecimiento.md)
- [Seleccionar productos y revisar condiciones](seleccionar-productos-y-revisar-condiciones.md)
