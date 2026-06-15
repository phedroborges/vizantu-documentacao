# Automacoes da Vizantu

Status: em construcao
Atualizado em: 2026-06-15

## Objetivo

Registrar automacoes desejadas, oportunidades detectadas, requisitos, regras de negocio e status de aprovacao.

## Estrutura padrao

Para cada automacao, documentar:

1. Nome
2. Problema que resolve
3. Gatilho
4. Entradas
5. Regras
6. Saida esperada
7. Ferramentas envolvidas
8. Dependencias
9. Riscos
10. Status

## Automacoes registradas ate agora

### App de controle de entregas, alinhamento e saúde do cliente

1. **Nome:** Vizantu OS / painel de controle operacional da Vizantu
2. **Problema que resolve:** o ClickUp controla demandas e tarefas, mas não dá uma visão simples e executiva sobre captações, planejamentos, reuniões de alinhamento, tempo de resposta, resolução de problemas no WhatsApp e satisfação do cliente.
3. **Gatilho:** rotina semanal/mensal de acompanhamento de cada cliente, leitura de grupos de WhatsApp, atualização de entregas e consolidação de indicadores.
4. **Entradas:**
   - Clientes ativos da Vizantu.
   - Demandas e status do ClickUp.
   - Marcos de entrega por cliente: captações, planejamentos e reuniões de alinhamento.
   - Transcrições de reuniões/Google Meet salvas automaticamente no Google Docs/Drive.
   - Mensagens dos grupos de WhatsApp.
   - Pesquisas de NPS.
   - Sinais qualitativos de satisfação ou insatisfação captados nos grupos.
5. **Regras:**
   - O ClickUp continua sendo a esteira de demandas e produção.
   - O novo app deve complementar o ClickUp com visão de projeto, cadência e relacionamento.
   - A visualização precisa ser simples, baseada principalmente em data prevista e check de entregue/não entregue.
   - O app não deve criar uma nova camada de status operacional para as entregas. O controle principal deve responder: tinha uma entrega prevista para determinada data e ela foi entregue ou não.
   - As entregas conectadas ao planejamento podem ser reconhecidas a partir de tags no ClickUp, evitando duplicação manual do que já está sendo executado na esteira de demandas.
   - Reuniões com clientes devem ser registradas no sistema a partir do arquivo de transcrição no Docs/Drive, vinculadas ao cliente correto e transformadas em histórico consultável.
   - Cada cliente precisa ter uma visão própria de entregas e saúde.
6. **Saída esperada:**
   - Painel por cliente com checklist de marcos e datas.
   - Visão geral dos clientes mostrando entregas previstas, entregues e não entregues.
   - Histórico de reuniões por cliente, com link para a transcrição original, resumo, decisões, pendências e próximos passos.
   - Alertas de atraso, ausência de resposta, problema pendente e queda de satisfação.
   - Indicadores de SLA de atendimento e resolução no WhatsApp.
   - Histórico de NPS e leitura qualitativa dos grupos.
7. **Ferramentas envolvidas:**
   - ClickUp.
   - Google Meet.
   - Google Docs/Drive.
   - WhatsApp/grupos de clientes.
   - Formulário ou ferramenta de NPS.
   - Banco de dados do app.
   - Possível painel web interno.
8. **Dependencias:**
   - Definir a fonte técnica viável para leitura de grupos de WhatsApp.
   - Mapear clientes ativos e cadências esperadas.
   - Definir quais tags do ClickUp representarão entregas vinculadas ao planejamento.
   - Definir quais campos do ClickUp devem sincronizar.
   - Definir padrão de organização/nomeação dos arquivos de transcrição no Google Drive para vincular reunião ao cliente correto.
   - Definir responsáveis por atualizar checks manuais quando a automação ainda não existir.
9. **Riscos:**
   - Duplicar trabalho se o app tentar substituir o ClickUp em vez de complementá-lo.
   - Criar status demais e transformar o app em uma segunda ferramenta de gestão de tarefas.
   - Medir WhatsApp sem critério claro e gerar conclusões erradas sobre atendimento.
   - Criar painel complexo demais para a rotina da equipe.
   - Depender de integração instável com WhatsApp.
10. **Status:** necessidade registrada; desenho inicial do app documentado em `07-app-controle-operacional-vizantu.md`.
