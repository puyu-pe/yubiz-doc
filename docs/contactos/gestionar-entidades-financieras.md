# Gestionar entidades financieras

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Registrar, revisar, editar o desactivar entidades financieras que se ofrecen al
gestionar cuentas de proveedores, cuando la capacidad esté habilitada.

## Acceso condicional

Esta capacidad es condicional: su entrada, acciones y alcance dependen del módulo,
la configuración y la sesión del entorno. No supone disponibilidad universal.

## Requisitos y datos

- Tipo de entidad y nombre.
- Descripción, si ayuda a distinguir la entidad.
- Estado que corresponda al uso autorizado en la organización.

## Punto de partida

Abra la opción de entidades financieras solo cuando esté disponible en la
navegación de su sesión o desde el flujo autorizado de cuentas de proveedores.

## Pasos

1. Revise la lista para confirmar si la entidad ya está registrada.
2. Para crear una entidad, use la acción disponible e indique tipo y nombre.
3. Si corresponde, agregue una descripción que permita reconocerla sin incluir
   datos de cuentas ni personas.
4. Revise el estado antes de guardar o editar el registro.
5. Para dejar de usar una entidad, utilice la acción disponible solo después de
   confirmar el impacto sobre cuentas asociadas; no asuma eliminación definitiva.

## Campos y validaciones observados

El formulario revisado contiene tipo, nombre, descripción y estado. Tipo y nombre
son obligatorios. Los tipos observados incluyen banco, caja, cooperativa y otros;
el estado se presenta como activo o inactivo. La fuente revisada no confirma que
estas etiquetas ni opciones sean idénticas en todos los entornos.

## Resultado revisado en fuente

La entidad queda disponible para relacionarse con cuentas de proveedores. Al
retirarla de uso, el flujo revisado cambia su estado a inactivo. La actualización
registra una fecha de modificación en la fuente, sin que esta ficha infiera una
política de auditoría o aprobación.

## Advertencias y casos límite

No incluya números de cuenta, CCI, titulares ni datos de personas en la
descripción. Antes de inactivar una entidad, confirme si existen cuentas asociadas
y el procedimiento aplicable. Si esta opción no está visible, no intente crear
entidades desde un flujo alternativo.

## Problemas frecuentes y condiciones de detención

- Falta tipo o nombre: complete ambos antes de guardar.
- La entidad ya existe o no se distingue de otra: deténgase y revise el listado.
- No se puede confirmar el impacto de inactivarla: no continúe sin el
  procedimiento autorizado.
- Opción ausente: confirme la habilitación del módulo y la sesión disponible.

## Verificaciones pendientes en runtime

- Disponibilidad real de la capacidad condicional.
- Etiquetas, opciones de tipo, mensajes y permisos por sesión.
- Uso de entidades activas e inactivas en cuentas de proveedores desplegadas.

## Enlaces relacionados

- [Gestionar proveedores y sus cuentas bancarias](gestionar-proveedores.md)
- [Contactos](index.md)
