# ReservaIF 2.0
> Sistema centralizado para reservas de salas e recursos do IFPI.

---

# 1. Identificação do Projeto
## Equipe
- **Guilherme Silva** (Product Owner)
- **Carlos Eduardo Fernandes** (Scrum Master)
- **Antônio Marcos Pires** (Desenvolvedor)
- **Christian Souza** (Desenvolvedor)
- **Lana Marina** (Desenvolvedora)

## Disciplina
Projeto Integrador

## Professor
Ely Miranda

---

# 2. Problema a ser Resolvido
A falta de um sistema centralizado para reservas de salas, resultando em conflitos de agendamento, lentidão na gestão de aprovações e falta de informações sobre o estado das salas de aula.

---

# 3. Objetivo do Projeto
Otimizar a gestão de salas e recursos, garantindo um processo de reserva rápido, livre de conflitos e sob controle da Coordenação.

---

# 4. Público-Alvo
- Professores, Coordenação, Setor de Manutenção e Administração dos Institutos Federais.

---

# 5. Tecnologias Utilizadas
| Área | Tecnologia |
|:---:|:---|
| Front-end | HTML, CSS |
| Back-end | Flask, Python |
| Banco | MySQL |
| Prototipação | Figma |
| Gestão | Miro |
-----------------------------

# 6. Requisitos de sistemas

# Atores 

* Professor
* Coordenador
* Manutenção
* Administrador
  
# Regras de Negócio

- Professor: pode consultar a disponibilidade de salas em um período, para evitar conflitos antes de reservar, pode preencher um formulário com cálculo automático de término, para submeter pedidos de reserva, quero que o sistema bloqueie reservas em horários de aulas regulares (Horário Oficial), pode reportar falhas (ex: projetor quebrado), para acionar a equipe de manutenção.

- Coordenador: recebe notificações imediatas (in-app/e-mail), para agir rapidamente sobre novos pedidos, tem acesso a uma interface para aprovar ou rejeitar pedidos, para controlar o uso das salas

- Manutenção: pode visualizar e filtrar problemas reportados, para agilizar os consertos, pode realizar checklists periódicos. Se um item falhar, a sala deve ser bloqueada automaticamente.

- Administrador: pode gerar relatórios de uso das salas para otimizar a distribuição de turmas.

# Backlog do Produto e Status de Entrega

| ID | Funcionalidade | Prioridade | Status |
|:---:|:---|:---:|:---:|
| **HU01** | Consulta de Disponibilidade | Alta | Planejado |
| **HU02** | Criação de Reserva (Cálculo de Término) | Crítica | ✅ Concluído |
| **HU03** | Notificação de Pedido (In-app/E-mail) | Crítica | Em andamento |
| **HU04** | Gestão de Pedidos (Aprovação/Rejeição) | Crítica | ✅ Concluído |
| **HU05** | Verificação de Conflito (Horário Oficial) | Crítica | Em andamento |
| **HU06** | Reporte de Problemas Técnicos | Alta | ✅ Concluído |
| **HU07** | Lista de Reparos para Manutenção | Média | Planejado |
| **HU08** | Cadastro de Salas e Equipamentos | Alta | ✅ Concluído |
| **HU09** | Notificações de Mudança de Status | Baixa | Planejado |
| **HU10** | Checklist Preventivo de Sala | Média | Planejado |
| **HU11** | Liberação Automática pós-uso | Crítica | Em andamento |
| **HU12** | Dashboard de Gestão (Indicadores) | Média | Planejado |
| **HU13** | Autenticação e Perfis de Acesso | Alta | Planejado |
| **HU14** | Recuperação de Senha | Baixa | Planejado |
| **HU15** | Relatórios Estratégicos de Uso | Baixa | Planejado |
| **HU16** | Histórico Detalhado da Reserva | Baixa | Planejado |

# Histórias de Usuário

---

## Gestão de Reservas (Core)
- **HU01:** Como **Professor**, quero **consultar a disponibilidade de salas**, para evitar conflitos de horário antes de solicitar uma reserva.
- **HU02:** Como **Professor**, quero **preencher um formulário de reserva**, para que o sistema calcule automaticamente o término e envie o pedido para análise.
- **HU03:** Como **Coordenador**, quero **receber notificações de novos pedidos**, para que eu possa agir rapidamente sobre as solicitações pendentes.
- **HU04:** Como **Coordenador**, quero **uma interface de aprovação/rejeição**, para controlar o uso dos espaços físicos da instituição.
- **HU05:** Como **Professor**, quero **que o sistema verifique o Horário Oficial**, para garantir que minha reserva não choque com aulas regulares.
- **HU11:** Como **Sistema**, quero **liberar a sala automaticamente após o uso**, para que a disponibilidade seja atualizada em tempo real.
- **HU16:** Como **Usuário**, quero **ver o histórico detalhado da reserva**, para saber quem aprovou e qual foi a justificativa em caso de rejeição.

## Manutenção e Infraestrutura
- **HU06:** Como **Professor**, quero **reportar falhas técnicas (ex: projetor quebrado)**, para que a equipe de manutenção seja acionada imediatamente.
- **HU07:** Como **Equipe de Manutenção**, quero **visualizar uma lista de reparos pendentes**, para organizar minha rotina de consertos.
- **HU08:** Como **Administrador**, quero **cadastrar salas e equipamentos**, para manter o inventário do campus atualizado no sistema.
- **HU10:** Como **Equipe de Manutenção**, quero **realizar checklists preventivos**, para garantir que as salas estejam em condições de uso antes das aulas.

## Segurança e Gestão
- **HU12:** Como **Coordenador**, quero **visualizar um dashboard de indicadores**, para analisar a taxa de ocupação e o tempo médio de reparo das salas.
- **HU13:** Como **Usuário**, quero **acessar o sistema via login e senha**, para garantir que apenas pessoas autorizadas realizem reservas.
- **HU14:** Como **Usuário**, quero **recuperar minha senha via e-mail**, para que eu possa retomar o acesso caso a esqueça.
- **HU15:** Como **Administrador**, quero **gerar relatórios estratégicos**, para auxiliar a diretoria na tomada de decisão sobre expansão de recursos.
- **HU09:** Como **Usuário**, quero **receber alertas de mudança de status**, para ser informado assim que minha reserva for aprovada ou rejeitada.

# 7. Modelagem do Sistema
# 8. Protótipos

# 9. Planejamento do Projeto

## Cronograma 
| Etapa | Período  |
|-------|----------|
| Levantamento | 25/04 a 26/04|
| Protótipos | 26/04 a 26/05 |
| Implementação | 25/05 a 26/05 |

## Sprints

| Sprints | Entregas |
|---------|----------|
| Sprint1 | Login + banco |
| Sprint2 | Dashboard 
| Sprint3 | Relatórioss |

## Gestão das Tarefas 
![trello](docs/planejamento/trello.png)

## Histórico de Entregas 

---------------------------------------------

---

# 10. Banco de Dados
# 11. Implementação
# 12. Evidências do Projeto

# 13. Itens Ainda Não Produzidos
> Conforme solicitado pelo professor, justificamos a ausência dos itens técnicos abaixo:

### Diagramas e Modelagem
Ainda não elaborados, pois a equipe focou na definição de escopo e visão do produto na Sprint 1.
**Previsão:** Sprint 2.

### Código Fonte
O repositório está sendo estruturado. A codificação iniciará após a validação dos protótipos.
**Previsão:** Sprint 3.

# 14. Como Executar o Projeto
