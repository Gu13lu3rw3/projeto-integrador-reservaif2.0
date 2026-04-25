# Regras de Negócio - ReservaIF 2.0

Este documento descreve as restrições e condições operacionais que regem o funcionamento do sistema.

---

## 1. Regras de Reserva e Disponibilidade
- **RN01 - Conflito com Horário Oficial:** O sistema deve impedir qualquer reserva que coincida com o horário de aulas regulares pré-cadastrado. O bloqueio deve ocorrer no momento da seleção do horário.
- **RN02 - Aprovação Obrigatória:** Todo pedido de reserva realizado por um Professor deve obrigatoriamente passar pelo status "Pendente" e aguardar a ação de um Coordenador.
- **RN03 - Liberação Automática:** No minuto exato do término da reserva aprovada, o status da sala deve retornar para "Disponível" automaticamente, sem necessidade de check-out manual.
- **RN04 - Cálculo de Término:** O horário de término deve ser calculado somando a "Hora de Início" à "Duração" selecionada, impedindo erros de digitação do usuário.

## 2. Regras de Manutenção e Segurança
- **RN05 - Bloqueio por Falha Crítica:** Se durante um Checklist (HU10) um item crítico (ex: Ar Condicionado ou Projetor) for marcado como "Falha", o sistema deve alterar o status da sala para "Em Manutenção" e bloquear novas reservas imediatamente.
- **RN06 - Reporte Automático:** Toda falha detectada em um Checklist deve gerar automaticamente um "Reporte de Problema" (HU06) com prioridade Alta para a equipe de Manutenção.
- **RN07 - Hierarquia de Acesso:** Um usuário só pode visualizar e editar informações condizentes com seu perfil (ex: Professor não pode aprovar reservas; Manutenção não pode gerenciar usuários).

## 3. Regras de Notificação
- **RN08 - Notificação em Tempo Real:** Sempre que um pedido for submetido, o Coordenador deve ser notificado em até 1 minuto (In-app/E-mail).
- **RN09 - Feedback de Status:** O sistema deve notificar o autor da reserva sempre que houver uma mudança de status (Aprovação, Rejeição ou Cancelamento).

---

## Matriz de Relação (HU x RN)
| Regra de Negócio | Histórias de Usuário Relacionadas |
|------------------|-----------------------------------|
| RN01 (Conflito)  | HU01, HU05                        |
| RN03 (Liberação) | HU11                              |
| RN05 (Bloqueio)  | HU10                              |
| RN08 (Notificação)| HU03, HU09                        |

