## Atividade da Disciplina de Técnicas Avançadas de Desenvolvimento de Software

### Alunos: Antonio G. Castro, Maria Eduarda Moretto

### Conteúdo da atividade

Em resumo, a atividade visa criar um serviço proxy interno para consumir uma API pública

A API impõe limite de 1 requisição por segundo, caso esse limite não seja respeitado a próxima resposta só é liberada após 2 segundos adicionais além da latência normal, impactando os serviços

O proxy implementado deve:

1. Acomodar picos de requisições internas
2. Minimizar latência e penalidade
3. Monitor e expor métricas para tomada de decisão
