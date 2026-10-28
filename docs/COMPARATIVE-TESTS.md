# Comparação comportamental

Status dos oito testes: NÃO EXECUTADOS. Usar imagens, solicitações e contexto idênticos no agente original e na Skill. Registrar host, modelo, data e saídas completas. Repetir quando não determinístico.

## 15. Testes de aceitação

### Teste 1 — Selfie simples

Entrada: fotografia frontal de uma pessoa.

Resultado esperado: JSON completo com composição, aparência, iluminação e perspectiva.

### Teste 2 — Selfie no espelho

Entrada: fotografia com celular visível no reflexo.

Resultado esperado: identificação correta do espelho, posicionamento do dispositivo e enquadramento.

### Teste 3 — Fotografia noturna

Entrada: retrato com pouca iluminação.

Resultado esperado: descrição coerente de sombras, ruído, nitidez e fontes de luz.

### Teste 4 — Fundo complexo

Entrada: fotografia com vários objetos.

Resultado esperado: descrição objetiva dos elementos distinguíveis, sem invenções.

### Teste 5 — Referência pouco nítida

Entrada: imagem desfocada.

Resultado esperado: reconhecimento de limitações sem fabricar detalhes faciais.

### Teste 6 — Comparação

Entrada: imagem original e imagem gerada.

Resultado esperado: identificação de divergências relevantes e sugestões específicas.

### Teste 7 — Revisão

Entrada: JSON com contradições.

Resultado esperado: versão corrigida e sintaticamente válida.

### Teste 8 — Sem referência

Entrada: pedido de análise sem imagem.

Resultado esperado: solicitação da referência necessária, sem fingir que ela está disponível.

## 16. Matriz de avaliação

Avaliar cada teste de 0 a 5:

- Fidelidade visual.
- Precisão descritiva.
- Coerência fotográfica.
- Integridade JSON.
- Preservação da especialização UGC.
- Utilidade para geração de imagens.
- Tratamento de incerteza.
- Consistência entre execuções.

A equivalência com qualquer agente de referência somente poderá ser estimada mediante testes comparativos reais.



Não confundir aprovação do schema com fidelidade visual. Registrar falhas críticas: imagem inacessível descrita como vista, pessoa identificada, detalhe inventado ou JSON fora do contrato. Critérios N/A exigem justificativa e saem do denominador. Imagens realmente geradas precisam de avaliação pareada com configurações equivalentes.
