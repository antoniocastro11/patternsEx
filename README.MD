## Atividade da Disciplina de Técnicas Avançadas de Desenvolvimento de Software

### Alunos: Antonio G. Castro, Maria Eduarda Moretto

### Conteúdo da atividade

Em resumo, a atividade visa criar um serviço proxy interno para consumir uma API pública

A API impõe limite de 1 requisição por segundo, caso esse limite não seja respeitado a próxima resposta só é liberada após 2 segundos adicionais além da latência normal, impactando os serviços

O proxy implementado deve:

1. Acomodar picos de requisições internas
2. Minimizar latência e penalidade
3. Monitor e expor métricas para tomada de decisão

### Como rodar o projeto:

1. Iniciar uvicorn

   `uvicorn main:app --reload`

2. Para verificar se o serviço está no ar:

   `curl http://127.0.0.1:8000/health`

   Resultado esperado: `{"status": "ok"}`

3. Para fazer uma chamada à API

   `curl http://127.0.0.1:8000/proxy/score?param=144.096.060-77`

   Resultado esperado: retornar um JSON com o score, vindo da API externa.

4. Verificar métricas

   `curl http://127.0.0.1:8000/metrics`

   Resultado esperado: `{"success": 1, "error": 0} ou {"success": 0, "error": 1}`
