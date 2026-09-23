# Gestionar socios y aportes

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Registrar o revisar socios y sus aportes dentro del módulo especializado.

## Acceso condicional

El menú declarado incluye **Gestión de Socios** e **Informe**. La disponibilidad de estas opciones y los datos visibles deben confirmarse en el entorno.

## Requisitos y datos

- Nombre, aporte, porcentaje y color para un socio cuando el formulario los solicite.
- Identificación del socio antes de abrir su lista de aportes.

## Punto de partida

Abra **Gestión de Socios** desde el módulo especializado y busque primero el registro que necesita revisar.

## Pasos

1. Revise nombre, aporte, porcentaje y color en la lista.
2. Abra el socio existente o use la acción disponible para agregarlo.
3. Complete los campos requeridos y revise los valores antes de guardar.
4. Abra **Lista de Aportes** para consultar o registrar el detalle disponible.
5. Vuelva a la lista y confirme que el registro se muestra de forma reconocible.

## Campos y validaciones observados

La gestión observada requiere descripción, color, aporte y porcentaje; los dos últimos se tratan como valores numéricos. Al guardar un aporte, la fuente recalcula los porcentajes agregados de los socios.

## Resultado revisado en fuente

La fuente guarda aportes en una transacción y actualiza los porcentajes calculados. El resultado visible, los importes y el informe requieren verificación en entorno.

## Advertencias y casos límite

No cambie aportes o porcentajes si no puede verificar el registro correcto. Los valores financieros mostrados por el informe no constituyen una confirmación operativa.

## Problemas frecuentes y condiciones de detención

- Datos obligatorios incompletos: complete los datos o no guarde.
- Socio no identificado: deténgase antes de registrar un aporte.
- Total o porcentaje inesperado: revise el detalle y valide el contexto.

## Verificaciones pendientes en runtime

- Etiquetas, acciones habilitadas, mensajes y cálculo visible de porcentajes.
- Datos y resultados del informe anual o mensual.

## Enlaces relacionados

- [Módulos especializados](index.md)
