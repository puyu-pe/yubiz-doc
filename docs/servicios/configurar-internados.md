# Configurar el módulo de internados

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Revisar y mantener los parámetros visibles del módulo de internados con una
instrucción operativa autorizada.

## Acceso condicional

El menú declarado incluye **Configuraciones**. Las categorías, estados y personas
mostrados dependen de los datos del entorno.

## Requisitos y datos

- Descripción y estado definidos para el parámetro que se va a mantener.
- Confirmación del impacto antes de modificar un valor existente.

## Punto de partida

En **Internado**, abra **Configuraciones** y ubique el grupo que necesita revisar.

## Pasos

1. Revise los estados de unidad, estados de servicio y categorías existentes.
2. Abra el registro correspondiente o use la acción de agregar disponible.
3. Complete descripción y estado; revise ambos valores antes de guardar.
4. Compruebe que la tabla muestra el valor esperado.
5. Si el cambio afecta una operación en curso, deténgase y valide el momento de
   aplicación antes de continuar.

## Campos y validaciones observados

La pantalla presenta estados de unidad, estados de servicio y categorías. El
guardado observado exige descripción y estado; permite crear o editar el registro
del grupo seleccionado.

## Resultado revisado en fuente

La fuente guarda el parámetro en una transacción y devuelve un mensaje de resultado.
La aplicación real del cambio en formularios y órdenes debe verificarse en entorno.

## Advertencias y casos límite

No cambie un estado o categoría sin conocer los registros que podrían usarlo. Los
operadores y su disponibilidad visible requieren verificación adicional.

## Problemas frecuentes y condiciones de detención

- Descripción o estado incompletos: complete ambos antes de guardar.
- No reconoce el grupo de configuración: deténgase y confirme la instrucción.
- Cambio sensible durante una operación: no continúe sin validación operativa.

## Verificaciones pendientes en runtime

- Etiquetas, acciones habilitadas, mensajes y efecto del cambio en el módulo.
- Disponibilidad y comportamiento de la sección de operadores.

## Enlaces relacionados

- [Registrar una orden de servicio o internado](registrar-internado.md)
- [Servicios](index.md)
