# ReservaIF 2.0
> Sistema centralizado para reservas de salas e recursos do IFPI.

---

# 1. Identificação do Projeto
## Equipe
- **Guilherme Silva** (Product Owner)
- **Carlos Eduardo Fernandes** (Scrum Master)
- **Allana Marina** (Desenvolvedora)
- **Antônio Marcos Pires** (Desenvolvedor)
- **Christian Souza** (Desenvolvedor)

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
| Banco | MySQL Workbench |
| Prototipação | Figma |
| Gestão | Miro |

---

# 6. Requisitos do Sistema

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
| **HU01** | Consulta de Disponibilidade | Alta | ✅ Concluído |
| **HU02** | Criação de Reserva (Cálculo de Término) | Crítica | ✅ Concluído |
| **HU03** | Notificação de Pedido (In-app/E-mail) | Crítica | ✅ Concluído |
| **HU04** | Gestão de Pedidos (Aprovação/Rejeição) | Crítica | ✅ Concluído |
| **HU05** | Verificação de Conflito (Horário Oficial) | Crítica | ✅ Concluído |
| **HU06** | Reporte de Problemas Técnicos | Alta | ✅ Concluído |
| **HU07** | Lista de Reparos para Manutenção | Média | ✅ Concluído |
| **HU08** | Cadastro de Salas e Equipamentos | Alta | ✅ Concluído |
| **HU09** | Notificações de Mudança de Status | Baixa | ✅ Concluído |
| **HU10** | Checklist Preventivo de Sala | Média | ✅ Concluído |
| **HU11** | Liberação Automática pós-uso | Critíco |✅ Concluído |
| **HU12** | Dashboard de Gestão (Indicadores) | Média | ✅ Concluído |
| **HU13** | Autenticação e Perfis de Acesso | Alta | ✅ Concluído |
| **HU14** | Recuperação de Senha | Baixa | ✅ Concluído |
| **HU15** | Relatórios Estratégicos de Uso | Baixa | ✅ Concluído |
| **HU16** | Histórico Detalhado da Reserva | Baixa | ✅ Concluído |

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
- **HU09:** Como **Usuário**, quero **receber alertas de mudança de status**, para ser informado assim que minha reserva for aprovada ou rejeitada.
- **HU12:** Como **Coordenador**, quero **visualizar um dashboard de indicadores**, para analisar a taxa de ocupação e o tempo médio de reparo das salas.
- **HU13:** Como **Usuário**, quero **acessar o sistema via login e senha**, para garantir que apenas pessoas autorizadas realizem reservas.
- **HU14:** Como **Usuário**, quero **recuperar minha senha via e-mail**, para que eu possa retomar o acesso caso a esqueça.
- **HU15:** Como **Administrador**, quero **gerar relatórios estratégicos**, para auxiliar a diretoria na tomada de decisão sobre expansão de recursos.

# 7. Modelagem do Sistema

## Diagrama de Casos de Uso
![Casos de Uso](docs/modelagem/casos_de_uso.png)

## Fluxo de Telas
![Fluxo de Telas](docs/modelagem/fluxo_de_telas.png)


## Arquitetura
![Arquitetura](docs/modelagem/arquitetura.png)

## Modelo Entidade-Relacionamento
![Modelo ER](docs/modelagem/modelo-er.png)

## Diagrama de Classes
![Diagrama de Classes](docs/modelagem/diagrama_classes.png)

# 8. Protótipos

## Tela de Login
![Login](docs/prototipos/login.png)

## Dashboard
![Dashboard](docs/prototipos/dashboard_professor.png)
![Dashboard](docs/prototipos/dashboard_coordenador.png)
![Dashboard](docs/prototipos/dashboard_manutencao.png)
![Dashboard](docs/prototipos/problemas_manutencao.png)
![Dashboard](docs/prototipos/dashboard_administrador.png)

## Cadastro
![Cadastro](docs/prototipos/cadastro.png)

# 9. Planejamento do Projeto

## Cronograma 
| Etapa | Período  |
|-------|----------|
| Levantamento | 26/04 a 26/04|
| Protótipos | 27/04 a 26/05 |
| Implementação | 27/05 a 28/06 |

## Sprints

| Sprints | Entregas |
|---------|----------|
| Sprint1 | Login + banco |
| Sprint2 | Dashboard |
| Sprint3 | Demais funcionalidades |
| Sprint4 | Relatórios |

## Gestão das Tarefas 
![trello](docs/planejamento/kanban1.png)
![trello](docs/planejamento/kanban2.png)

## Histórico de Entregas 
- Entrega 1: Documentação inicial do README, brainstorm de todas as ideias para o projeto e protótipos parciais de telas.
- Entrega 2: Continuação do código parcial e aprimoramento das HUs existentes.
- Entrega 3: Implementação parcial (cerca de 60% do escopo total do código) e revisão de erros na documentação.
- Entrega 4: Implementação final (código completo) e última revisão de erros no projeto todo.

---

# 10. Banco de Dados
 ## Estrutura

 Arquivos disponíveis:
 -`database/ddl.sql`
 -`database/dml.sql`
 -`database/schema.sql`
 -`database/seeds.sql`
 
 ## Modelo Visual 
  ![Banco](database/modelo-er.png)

  ## Observações
  
  As tabelas `USUARIO`, `SALA`, `EQUIPAMENTO`, `RESERVA`, `HORARIO_OFICIAL`, `PROBLEMA`, `NOTIFICACAO` e `CHECKLIST` foram criadas para gerenciar as informações do sistema. As tabelas já contêm dados iniciais para testes e demonstração.

---
# 11. Implementação

## Backend
O backend foi desenvolvido em **Python com o framework Flask**, seguindo uma estrutura modular e organizada:
- **Arquitetura:** Padrão MVC (Model-View-Controller) com roteamento manual e explícito via `add_url_rule`.
- **Rotas:** Centralizadas no arquivo `routes/routes.py` para facilitar a manutenção e o controle de endpoints.
- **Regras de Negócio:** Implementação de lógica para cálculo automático de término de reserva (HU02), bloqueio automático de salas via checklist (HU10) e sistema de notificações reativo (HU09).

## Frontend
As interfaces foram construídas com **HTML5 e CSS3**, utilizando a identidade visual institucional (Branco e Verde):
- **Dashboard Principal:** Central de navegação para todos os perfis de usuário.
- **Módulo de Salas:** Interfaces para listagem e formulário de cadastro de novos recursos.
- **Módulo de Reservas:** Tela de solicitação com campos dinâmicos e visualização de status.
- **Módulo de Manutenção:** Telas para reporte de falhas técnicas e realização de checklists preventivos.

## Funcionalidades Concluídas
Todas as Histórias de Usuário (HUs) listadas no backlog foram implementadas e estão funcionais:

- **HU01 - Consulta de Disponibilidade** 
- **HU02 - Criação de Reserva (Cálculo de Término)**
- **HU03 - Notificação de Pedido (In-app/E-mail)**
- **HU04 - Gestão de Pedidos (Aprovação/Rejeição)**
- **HU05 - Verificação de Conflito (Horário Oficial)**
- **HU06 - Reporte de Problemas Técnicos** 
- **HU07 - Lista de Reparos para Manutenção** 
- **HU08 - Cadastro de Salas e Equipamentos** 
- **HU09 - Notificações de Mudança de Status** 
- **HU10 - Checklist Preventivo de Sala** 
- **HU11 - Liberação Automática pós-uso**
- **HU12 - Dashboard de Gestão (Indicadores)**
- **HU13 - Autenticação e Perfis de Acesso**
- **HU14 - Recuperação de Senha**
- **HU15 - Relatórios Estratégicos de Uso**
- **HU16 - Histórico Detalhado da Reserva**

---

# 12. Evidências do Projeto

Todas as funcionalidades foram implementadas e testadas. As evidências de funcionamento serão adicionadas em breve, após a conclusão dos testes finais e a preparação da documentação de entrega.

---

# 13. Como Executar o Projeto

Para executar o projeto localmente, siga os passos abaixo:

## Pré-requisitos
- **Python 3.x** instalado.
- **MySQL** instalado e em execução.
- **pip** (gerenciador de pacotes do Python).

## Configuração do Banco de Dados
1. Certifique-se de ter um servidor MySQL em execução.
2. Crie um banco de dados chamado `reservaif`.
3. Importe o esquema do banco de dados e os dados iniciais:
```bash
mysql -u seu_usuario -p reservaif < database/schema.sql
mysql -u seu_usuario -p reservaif < database/seeds.sql
```

## Configuração do Ambiente Python
1. Navegue até a pasta `backend` do projeto:
```bash
cd backend
```
2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

## Execução da Aplicação
1. Ainda dentro da pasta `backend`, inicie o servidor:
```bash
python app.py
```
2. O sistema estará disponível no seu navegador no endereço: [http://127.0.0.1:5000](http://127.0.0.1:5000 )

---

# 14. Próximos Passos
- **Testes de Estresse:** Validar o comportamento do sistema com múltiplas reservas simultâneas.
- **Documentação de API:** Criar uma documentação detalhada dos endpoints.
- **Refinamento de UI:** Ajustar detalhes visuais finais.
