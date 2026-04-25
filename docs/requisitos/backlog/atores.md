# Atores do Sistema - ReservaIF 2.0

Detalhamento dos perfis de usuários e suas permissões dentro do ecossistema do ReservaIF 2.0, conforme definido no planejamento das Sprints 1 a 4.

---

## 1. Professor (Usuário Final)
O ator principal que utiliza os recursos para atividades pedagógicas. Resumindo, é ele quem solicita as reservas de salas de aula.
- **Principais Ações:**
    - Consultar disponibilidade de salas e equipamentos em tempo real.
    - Criar pedidos de reserva (HU02) e visualizar o cálculo automático de término.
    - **Reportar Problemas (HU06):** Notificar falhas técnicas (projetor, AC, etc.) diretamente pelo sistema.
    - Acompanhar o histórico e status de suas reservas (HU08).
    - Receber notificações de aprovação ou rejeição (HU09).

## 2. Coordenador (Gestor de Espaço)
Responsável por validar o uso dos recursos e monitorar a qualidade.
- **Principais Ações:**
    - **Aprovação/Rejeição (HU04):** Decidir sobre pedidos de reserva pendentes.
    - **Dashboard de Gestão (HU12):** Monitorar indicadores como o Tempo Médio de Reparo (TMR) e Taxa de Ocupação.
    - Receber alertas imediatos de novos pedidos (HU03).
    - Visualizar o histórico completo de decisões da equipe de gestão.

## 3. Equipe de Manutenção (Operacional)
Garante que o ambiente físico esteja apto para o uso.
- **Principais Ações:**
    - **Gestão de Reparos (HU07):** Visualizar e filtrar a lista de problemas reportados pelos professores.
    - **Checklist Preventivo (HU10):** Realizar vistorias periódicas nas salas.
    - **Bloqueio de Salas:** Alterar o status de uma sala para "Em Manutenção", impedindo novas reservas automaticamente em caso de falha crítica.

## 4. Administrador (Gestão de Sistema)
Responsável pela infraestrutura de dados e regras globais.
- **Principais Ações:**
    - **Cadastro de Recursos (HU08):** Registrar novas salas, blocos e equipamentos.
    - Gerenciar perfis de acesso e segurança (HU13).
    - **Relatórios Estratégicos (HU15):** Gerar dados consolidados de uso para a diretoria.
    - Configurar o "Horário Oficial" para evitar conflitos automáticos (HU05).

---

## Resumo de Permissões
| Funcionalidade | Professor | Coordenador | Manutenção | Admin |
|----------------|:---------:|:-----------:|:----------:|:-----:|
| Criar Reserva  | Sim       | Sim         | Não        | Sim   |
| Aprovar Pedido | Não       | Sim         | Não        | Sim   |
| Reportar Falha | Sim       | Sim         | Sim        | Sim   |
| Fazer Checklist| Não       | Não         | Sim        | Não   |
| Bloquear Sala  | Não       | Não         | Sim        | Sim   |
| Gerir Usuários | Não       | Não         | Não        | Sim   |

